# ==========================================================
# FILE: main.py
# ----------------------------------------------------------
# PURPOSE:
# Main entry point of the application.
#
# WHY THIS EXISTS:
# Users should interact with one file only.
#
# FLOW:
#
# User Input
#       ↓
# Router
#       ↓
# Chain
#       ↓
# Model
#       ↓
# Response
#
# ==========================================================

from src.routers.rule_router import route_request


def main():

    print("=" * 50)
    print("LangChain Smart Prompt Orchestrator")
    print("=" * 50)

    while True:

        user_input = input("\nEnter request (or 'exit'): ")

        if user_input.lower() == "exit":
            print("\nGoodbye.")
            break

        response = route_request(user_input)

        print("\nResponse:")
        print(response)


if __name__ == "__main__":
    main()