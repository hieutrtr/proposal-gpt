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

store_final_proposal_schema = {
            "name": "store_final_proposal",
            "parameters": {
                "type": "object",
                "properties": {
                    "final": {
                        "type": "string",
                        "description": (
                            "Enter the final of proposal in markdown format."
                        ),
                    }
                },
                "required": [
                    "final"
                ]
            },
            "description": "This is a function allowing bd_final to input the final proposal to store in markdown format.",
        }

def store_draft_proposal(draft):
    """
    Store draft of proposal in a local file.
    """
    # Exception
    if not isinstance(draft, str):
        raise TypeError("Draft of proposal must be a string.")
    # Function implementation...
    with open("./draft_proposal.txt", "w") as f:
        f.write(draft)
    # False case
    if not os.path.exists("./draft_proposal.txt"):
        return False
    return True

def store_final_proposal(final):
    """
    Store draft of proposal in a local file.
    """
    # Exception
    print("*"*100)
    print("*"*100)
    print("*"*100)
    print("Called store_final_proposal")
    if not isinstance(final, str):
        raise TypeError("Draft of proposal must be a string.")
    # Function implementation...
    with open("./final_proposal.md", "w") as f:
        f.write(final)
    # False case
    if not os.path.exists("./final_proposal.md"):
        return False
    return True
    