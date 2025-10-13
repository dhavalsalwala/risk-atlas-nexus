from risk_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import (
    EuAiRiskCategory,
)


LIST_OF_STR_SCHEMA = {
    "type": "object",
    "properties": {
        "harm": {
            "type": "array",
            "items": {
                "enum": [
                    "Physical health/safety",
                    "Financial loss",
                    "Physical property",
                    "Intangible property",
                    "Infrastructure",
                    "Natural environment",
                    "Social or political systems",
                    "Other tangible harms",
                ]
            },
        },
        "explanation": {"type": "string"},
    },
    "required": ["harm", "explanation"],
}

LIKELYHOOD_OUTPUT = {
    "type": "object",
    "properties": {"likelihood": {"type": "number"}},
    "required": ["likelihood"],
}

LIST_OF_GOAL_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {"goal": {"type": "string"}, "label": {"type": "number"}},
        "required": ["goal", "label"],
    },
}

QUESTIONNAIRE_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {
            "type": "string",
            "enum": ["Yes", "No", "Maybe"],
        },
        "explanation": {"type": "string"},
    },
    "required": [
        "answer",
        "explanation",
    ],
}

DOMAIN_TYPE_SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {
            "type": "string",
            "enum": [
                "Customer service/support",
                "Technical",
                "Information retrieval",
                "Strategy",
                "Code/software engineering",
                "Communications",
                "IT/business automation",
                "Writing assistant",
                "Financial",
                "Talent and Organization including HR",
                "Product",
                "Marketing",
                "Cybersecurity",
                "Healthcare",
                "User Research",
                "Sales",
                "Risk and Compliance",
                "Design",
                "Other",
            ],
        },
        "explanation": {"type": "string"},
    },
    "required": [
        "answer",
        "explanation",
    ],
}

RISK_CATEGORY_SCHEMA = {
    "type": "object",
    "properties": {
        "Description": {"type": "string"},
        "Classification": {
            "type": "string",
            "enum": [
                EuAiRiskCategory.EXCLUDED.value,
                EuAiRiskCategory.PROHIBITED.value,
                EuAiRiskCategory.HIGH_RISK_EXCEPTION.value,
                EuAiRiskCategory.HIGH_RISK.value,
                EuAiRiskCategory.LIMITED_OR_LOW_RISK.value,
            ],
        },
        "AIActText": {"type": "string"},
        "Reasoning": {"type": "string"},
    },
    "required": [
        "Description",
        "Classification",
        "AIActText",
        "Reasoning",
    ],
}
