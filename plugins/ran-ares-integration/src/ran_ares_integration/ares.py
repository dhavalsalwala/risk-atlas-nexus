import os
from pathlib import Path
from typing import List

from ares.cli import evaluate
from jinja2 import Template
from linkml_runtime.dumpers import YAMLDumper
from linkml_runtime.loaders import yaml_loader

from ran_ares_integration.data import DATA_DIR
from ran_ares_integration.datamodel.risk_to_ares_ontology import RiskToARESMapping
from ran_ares_integration.prompt_templates import ARES_GOALS_TEMPLATE


def generate_ares_goals(cls, risk, inference_engine, verbose=True) -> List[dict]:
    """Identify potential risks from a usecase description

    Args:
        risk (Risk):
            A List of strings describing AI usecases
        inference_engine (InferenceEngine):
            An LLM inference engine to identify AI tasks from usecases.

    Returns:
        List[Dict]:
            Result containing a list of AI tasks
    """
    # Invoke inference service
    goals = inference_engine.generate(
        prompts=[
            Template(ARES_GOALS_TEMPLATE).render(
                risk_name=risk.name, risk_description=risk.description
            )
        ],
        response_format={
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"goal": {"type": "string"}, "label": {"type": "number"}},
                "required": ["goal", "label"],
            },
        },
        postprocessors=["json_object"],
        verbose=verbose,
    )

    print()
