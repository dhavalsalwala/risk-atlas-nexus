import json
from itertools import compress
from typing import List

from risk_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from risk_atlas_nexus.blocks.inference import TextGenerationInferenceOutput
from risk_atlas_nexus.blocks.prompt_response_schema import (
    LIKELYHOOD_OUTPUT,
    LIST_OF_STR_SCHEMA,
)
from risk_atlas_nexus.blocks.prompt_templates import (
    RISK_IDENTIFICATION_TEMPLATE,
    RISK_IDENTIFICATION_TEMPLATE_2,
)
from risk_atlas_nexus.blocks.risk_detector import RiskDetector


class GenericRiskDetector(RiskDetector):

    def detect(self, usecases: List[str]) -> List[List[Risk]]:
        prompts = [
            self.prompt_builder(prompt_template=RISK_IDENTIFICATION_TEMPLATE).build(
                cot_examples=self._examples,
                usecase=usecases[0],
                risks=json.dumps(self._risks, indent=2),
            )
        ]

        # Invoke inference service
        inference_responses: List[TextGenerationInferenceOutput] = (
            self.inference_engine.generate(
                prompts,
                response_format=LIST_OF_STR_SCHEMA,
                postprocessors=["json_object"],
            )
        )

        return inference_responses
