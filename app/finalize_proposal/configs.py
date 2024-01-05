import autogen
import chromadb
from functions.draft_proposal import store_final_proposal_schema
# set path to root directory

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4"],
    },
)
finalize_admin_config = {
        "task": "code",
        "docs_path": ["./draft_proposal.txt", "./image.json"],
        "chunk_token_size": 4000,
        "model": config_list[0]["model"],
        "client": chromadb.Client(),
        "collection_name": "final_proposal",
        "get_or_create": True,
    }

proposal_finalizer_config = {
    "cache_seed": 42,  # change the cache_seed for different trials
    "temperature": 0,
    "config_list": config_list,
    "timeout": 120,
    "functions": [ store_final_proposal_schema ]
}

group_chat_config = {
    "cache_seed": 42,  # change the cache_seed for different trials
    "temperature": 0,
    "config_list": config_list,
    "timeout": 120,
}