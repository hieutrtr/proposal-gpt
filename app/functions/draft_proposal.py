import logging
import os
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

store_draft_proposal_schema = {
  "name": "store_draft_proposal",
  "parameters": {
    "type": "object",
    "properties": {
      "draft": {
        "type": "string",
        "description": (
            "Enter the draft of proposal in text format."
        ),
      }
    },
    "required": [
      "draft"
    ]
  },
  "description": "This is a function allowing bd_draft to input the result as a draft of proposal to store in free text format.",
}

def store_draft_proposal(draft):
    """
    Store draft of proposal in a local file.
    """
    # Exception
    if not isinstance(draft, str):
        raise TypeError("Draft of proposal must be a string.")
    # Function implementation...
    with open("/root/projects/proposal-gpt/draft_proposal.txt", "w") as f:
        f.write(draft)
    # False case
    if not os.path.exists("/root/projects/proposal-gpt/draft_proposal.txt"):
        return False
    return True
    