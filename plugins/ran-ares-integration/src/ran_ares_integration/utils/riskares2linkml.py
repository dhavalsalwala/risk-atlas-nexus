import os
from uuid import uuid4

import yaml
from linkml_runtime.dumpers import YAMLDumper

from ran_ares_integration.data import DATA_DIR
from ran_ares_integration.datamodel.risk_to_ares_ontology import (
    ARESConfig,
    AresIntent,
    ChatTemplate,
    Connector,
    DGTAttackGoal,
    DirectRequests,
    GenerateKwargs,
    GenerateParams,
    GenericAttackGoal,
    HumanJailbreak,
    InjectASCII,
    KeywordEvaluator,
    ModelConfig,
    READIEvaluator,
    RedTeaming,
    RiskToARES,
    RiskToARESMapping,
    TokenizerConfig,
)


direct_instructions_attack = RiskToARESMapping(
    **{
        "id": str(uuid4()),
        "name": "direct_instructions_attack",
        "description": None,
        "risk_id": "direct-instructions-attack",
        "ares_config": ARESConfig(
            **{
                "id": str(uuid4()),
                "name": "ares_default_config",
                "description": None,
                "target": {
                    "huggingface": Connector(
                        id=str(uuid4()),
                        type="ares.connectors.huggingface.HuggingFaceConnector",
                        model_configs=ModelConfig(
                            pretrained_model_name_or_path="Qwen/Qwen2-0.5B-Instruct",
                            torch_dtype="bfloat16",
                        ),
                        tokenizer_config=TokenizerConfig(
                            pretrained_model_name_or_path="Qwen/Qwen2-0.5B-Instruct",
                            padding_side="left",
                        ),
                        generate_kwargs=GenerateKwargs(
                            chat_template=ChatTemplate(
                                return_tensors="pt",
                                thinking=True,
                                return_dict=True,
                                add_generation_prompt=True,
                            ),
                            generate_params=GenerateParams(max_new_tokens=50),
                        ),
                        seed=42,
                        device="auto",
                    )
                },
                "red_teaming": RedTeaming(
                    **{
                        "id": str(uuid4()),
                        "description": None,
                        "intent": "owasp-llm-02",
                        "intent_config": {
                            "owasp-llm-02": AresIntent(
                                id=str(uuid4()),
                                description=None,
                                goal=GenericAttackGoal(
                                    **{
                                        "id": str(uuid4()),
                                        "base_path": "assets/attack_goal.json",
                                        "output_path": "assets/attack_goals.json",
                                    }
                                ),
                                strategy={
                                    "direct_requests": DirectRequests(
                                        **{
                                            "id": str(uuid4()),
                                            "input_path": "assets/attack_goals.json",
                                            "output_path": "assets/direct_requests.json",
                                        }
                                    )
                                },
                                evaluation=KeywordEvaluator(**{"id": str(uuid4())}),
                            )
                        },
                        "prompts": "assets/pii-seeds.csv",
                    }
                ),
            }
        ),
    }
)

encoded_interactions_attack = RiskToARESMapping(
    **{
        "id": str(uuid4()),
        "name": "encoded_interactions_attack",
        "description": None,
        "risk_id": "encoded-interactions-attack",
        "ares_config": ARESConfig(
            **{
                "id": str(uuid4()),
                "name": "ares_default_config",
                "description": None,
                "target": {
                    "huggingface": Connector(
                        id=str(uuid4()),
                        type="ares.connectors.huggingface.HuggingFaceConnector",
                        model_configs=ModelConfig(
                            pretrained_model_name_or_path="Qwen/Qwen2-0.5B-Instruct",
                            torch_dtype="bfloat16",
                        ),
                        tokenizer_config=TokenizerConfig(
                            pretrained_model_name_or_path="Qwen/Qwen2-0.5B-Instruct",
                            padding_side="left",
                        ),
                        generate_kwargs=GenerateKwargs(
                            chat_template=ChatTemplate(
                                return_tensors="pt",
                                thinking=True,
                                return_dict=True,
                                add_generation_prompt=True,
                            ),
                            generate_params=GenerateParams(max_new_tokens=50),
                        ),
                        seed=42,
                        device="auto",
                    )
                },
                "red_teaming": RedTeaming(
                    **{
                        "id": str(uuid4()),
                        "description": None,
                        "intent": "owasp-llm-02",
                        "intent_config": {
                            "owasp-llm-02": AresIntent(
                                id=str(uuid4()),
                                description=None,
                                goal=GenericAttackGoal(
                                    **{
                                        "id": str(uuid4()),
                                        "base_path": "assets/attack_goal.json",
                                        "output_path": "assets/attack_goals.json",
                                    }
                                ),
                                strategy={
                                    "probes.encoding.InjectROT13": InjectASCII(
                                        **{
                                            "id": str(uuid4()),
                                            "probe": "probes.encoding.InjectROT13",
                                            "input_path": "assets/attack_goals.json",
                                            "output_path": "assets/garak_InjectROT13.json",
                                        }
                                    ),
                                },
                                evaluation=KeywordEvaluator(**{"id": str(uuid4())}),
                            )
                        },
                        "prompts": "assets/pii-seeds.csv",
                    }
                ),
            }
        ),
    }
)

social_hacking_attack = RiskToARESMapping(
    **{
        "id": str(uuid4()),
        "name": "social_hacking_attack",
        "description": None,
        "risk_id": "social-hacking-attack",
        "ares_config": ARESConfig(
            **{
                "id": str(uuid4()),
                "name": "ares_default_config",
                "description": None,
                "target": {
                    "huggingface": Connector(
                        id=str(uuid4()),
                        type="ares.connectors.huggingface.HuggingFaceConnector",
                        model_configs=ModelConfig(
                            pretrained_model_name_or_path="Qwen/Qwen2-0.5B-Instruct",
                            torch_dtype="bfloat16",
                        ),
                        tokenizer_config=TokenizerConfig(
                            pretrained_model_name_or_path="Qwen/Qwen2-0.5B-Instruct",
                            padding_side="left",
                        ),
                        generate_kwargs=GenerateKwargs(
                            chat_template=ChatTemplate(
                                return_tensors="pt",
                                thinking=True,
                                return_dict=True,
                                add_generation_prompt=True,
                            ),
                            generate_params=GenerateParams(max_new_tokens=50),
                        ),
                        seed=42,
                        device="auto",
                    )
                },
                "red_teaming": RedTeaming(
                    **{
                        "id": str(uuid4()),
                        "description": None,
                        "intent": "owasp-llm-02",
                        "intent_config": {
                            "owasp-llm-02": AresIntent(
                                id=str(uuid4()),
                                description=None,
                                goal=GenericAttackGoal(
                                    **{
                                        "id": str(uuid4()),
                                        "base_path": "assets/attack_goal.json",
                                        "output_path": "assets/attack_goals.json",
                                    }
                                ),
                                strategy={
                                    "human_jailbreak": HumanJailbreak(
                                        **{
                                            "id": str(uuid4()),
                                            "input_path": "assets/attack_goals.json",
                                            "output_path": "assets/human_jailbreak.json",
                                            "jailbreaks_path": "assets/human_jailbreaks.json",
                                        }
                                    ),
                                },
                                evaluation=KeywordEvaluator(**{"id": str(uuid4())}),
                            )
                        },
                        "prompts": "assets/pii-seeds.csv",
                    }
                ),
            }
        ),
    }
)

specialized_tokens_attack = RiskToARESMapping(
    **{
        "id": str(uuid4()),
        "name": "specialized_tokens_attack",
        "description": None,
        "risk_id": "specialized-tokens-attack",
        "ares_config": ARESConfig(
            **{
                "id": str(uuid4()),
                "name": "ares_default_config",
                "description": None,
                "target": {
                    "huggingface": Connector(
                        id=str(uuid4()),
                        type="ares.connectors.huggingface.HuggingFaceConnector",
                        model_configs=ModelConfig(
                            pretrained_model_name_or_path="Qwen/Qwen2-0.5B-Instruct",
                            torch_dtype="bfloat16",
                        ),
                        tokenizer_config=TokenizerConfig(
                            pretrained_model_name_or_path="Qwen/Qwen2-0.5B-Instruct",
                            padding_side="left",
                        ),
                        generate_kwargs=GenerateKwargs(
                            chat_template=ChatTemplate(
                                return_tensors="pt",
                                thinking=True,
                                return_dict=True,
                                add_generation_prompt=True,
                            ),
                            generate_params=GenerateParams(max_new_tokens=50),
                        ),
                        seed=42,
                        device="auto",
                    )
                },
                "red_teaming": RedTeaming(
                    **{
                        "id": str(uuid4()),
                        "description": None,
                        "intent": "owasp-llm-02",
                        "intent_config": {
                            "owasp-llm-02": AresIntent(
                                id=str(uuid4()),
                                description=None,
                                goal=GenericAttackGoal(
                                    **{
                                        "id": str(uuid4()),
                                        "base_path": "assets/attack_goal.json",
                                        "output_path": "assets/attack_goals.json",
                                    }
                                ),
                                strategy={
                                    "direct_requests": DirectRequests(
                                        **{
                                            "id": str(uuid4()),
                                            "input_path": "assets/attack_goals.json",
                                            "output_path": "assets/direct_requests.json",
                                        }
                                    ),
                                    "human_jailbreak": HumanJailbreak(
                                        **{
                                            "id": str(uuid4()),
                                            "input_path": "assets/attack_goals.json",
                                            "output_path": "assets/human_jailbreak.json",
                                            "jailbreaks_path": "assets/human_jailbreaks.json",
                                        }
                                    ),
                                    "probes.encoding.InjectROT13": InjectASCII(
                                        **{
                                            "id": str(uuid4()),
                                            "probe": "probes.encoding.InjectROT13",
                                            "input_path": "assets/attack_goals.json",
                                            "output_path": "assets/garak_InjectROT13.json",
                                        }
                                    ),
                                },
                                evaluation=KeywordEvaluator(**{"id": str(uuid4())}),
                            )
                        },
                        "prompts": "assets/pii-seeds.csv",
                    }
                ),
            }
        ),
    }
)

with open(
    os.path.join(DATA_DIR, "knowledge_graph", "risk_to_ares_mappings.yaml"),
    "+tw",
    encoding="utf-8",
) as output_file:
    print(
        YAMLDumper().dumps(
            RiskToARES(
                mappings=[
                    direct_instructions_attack,
                    encoded_interactions_attack,
                    social_hacking_attack,
                    specialized_tokens_attack,
                ]
            )
        ),
        file=output_file,
    )
