from typing import Any, Dict, List, Optional

from risk_atlas_nexus.blocks.inference import InferenceEngine
from risk_atlas_nexus.blocks.prompt_builder import (
    FewShotPromptBuilder,
    ZeroShotPromptBuilder,
)
from risk_atlas_nexus.blocks.prompt_response_schema import QUESTIONNAIRE_OUTPUT_SCHEMA
from risk_atlas_nexus.blocks.prompt_templates import QUESTIONNAIRE_COT_TEMPLATE
from risk_atlas_nexus.data import load_resource
from risk_atlas_nexus.toolkit.validator import validate


RISK_QUESTIONNAIRE_COT = load_resource("risk_questionnaire_cot.json")
RISK_QUESTIONNAIRE_COT_SCHEMA = load_resource("risk_questionnaire_cot_schema.json")


class AutoAssistRiskQuestionnaire:

    def __init__(
        self,
        inference_engine: InferenceEngine,
        risk_questionnaire: Optional[List[Dict[str, Any]]] = None,
        verbose: bool = True,
    ):
        self.inference_engine = inference_engine
        self.verbose = verbose

        # Validate format of user-provided `risk_questionnaire` if available
        if risk_questionnaire is None:
            self.risk_questionnaire = RISK_QUESTIONNAIRE_COT
        elif errors := validate(risk_questionnaire, RISK_QUESTIONNAIRE_COT_SCHEMA):
            raise Exception(
                f"The format of `risk_questionnaire` is incorrect. {errors}. Please refer to the example template provided at src/risk_atlas_nexus/data/templates/risk_questionnaire_cot.json"
            )
        else:
            self.risk_questionnaire = risk_questionnaire

    def generate_responses(self, usecase: str):

        # Prepare inference prompts based on whether the CoT examples are available.
        prompts = []
        for risk_question in self.risk_questionnaire:
            if (
                "cot_examples" not in risk_question
                or risk_question["cot_examples"] is None
                or len(risk_question["cot_examples"]) == 0
            ):
                prompts.append(
                    ZeroShotPromptBuilder(QUESTIONNAIRE_COT_TEMPLATE).build(
                        usecase=usecase,
                        question=risk_question["question"],
                    )
                )
            else:
                prompts.append(
                    FewShotPromptBuilder(QUESTIONNAIRE_COT_TEMPLATE).build(
                        usecase=usecase,
                        question=risk_question["question"],
                        cot_examples=risk_question["cot_examples"],
                    )
                )

        # Invoke inference service
        return self.inference_engine.generate(
            prompts,
            response_format=QUESTIONNAIRE_OUTPUT_SCHEMA,
            postprocessors=["json_object"],
            verbose=self.verbose,
        )
