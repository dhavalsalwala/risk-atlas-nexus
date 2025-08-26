import os
from uuid import uuid4

from linkml_runtime.dumpers import YAMLDumper

from risk_atlas_nexus.ares import ARES_DIR
from risk_atlas_nexus.ares.ares_ontology import (
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
    RiskGroupToARESConfig,
    RiskGroupToARESConfigList,
    TokenizerConfig,
)


prompt_attacks_config = RiskGroupToARESConfig(
    **{
        "id": str(uuid4()),
        "name": "prompt_attacks",
        "description": None,
        "risk_attack_group": "ibm-risk-atlas-robustness-prompt-attacks",
        "config": ARESConfig(
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
                                evaluation=READIEvaluator(**{"id": str(uuid4())}),
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
    os.path.join(ARES_DIR, "risk_group_ares_mapping.yaml"),
    "+tw",
    encoding="utf-8",
) as output_file:
    print(
        YAMLDumper().dumps(RiskGroupToARESConfigList(mappings=[prompt_attacks_config])),
        file=output_file,
    )
