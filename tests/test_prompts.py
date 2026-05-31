from src.prompts.explain_prompt import explain_prompt
from src.prompts.summarize_prompt import summarize_prompt
from src.prompts.idea_prompt import idea_prompt


print("=== EXPLAIN PROMPT ===")
print(
    explain_prompt.format(
        topic="machine learning"
    )
)

print("\n" + "=" * 50 + "\n")

print("=== SUMMARIZE PROMPT ===")
print(
    summarize_prompt.format(
        text="Artificial intelligence is transforming industries."
    )
)

print("\n" + "=" * 50 + "\n")

print("=== IDEA PROMPT ===")
print(
    idea_prompt.format(
        topic="fitness"
    )
)