import autogen
import chromadb
# set path to root directory

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4"],
    },
)
retrieval_admin_config = {
        "task": "code",
        "docs_path": "./draft_proposal.txt",
        "chunk_token_size": 1000,
        "model": config_list[0]["model"],
        "client": chromadb.Client(),
        "collection_name": "draft_proposal",
        "get_or_create": True,
    }

visualizer_config = {
    "cache_seed": 42,  # change the cache_seed for different trials
    "temperature": 0,
    "config_list": config_list,
    "timeout": 120,
}

designer_config = {
    "cache_seed": 42,  # change the cache_seed for different trials
    "temperature": 0,
    "config_list": config_list,
    "timeout": 120,
}

group_chat_config = {
    "cache_seed": 42,  # change the cache_seed for different trials
    "temperature": 0,
    "config_list": config_list,
    "timeout": 120,
}