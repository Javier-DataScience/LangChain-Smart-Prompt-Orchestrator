from src.chains.explain_chain import explain_chain
from src.chains.summarize_chain import summarize_chain
from src.chains.idea_chain import idea_chain


print("\n=== EXPLAIN CHAIN ===")
print(
    explain_chain(
        "machine learning"
    )
)

print("\n=== SUMMARIZE CHAIN ===")
print(
    summarize_chain(
        "Artificial intelligence is transforming industries."
    )
)

print("\n=== IDEA CHAIN ===")
print(
    idea_chain(
        "fitness"
    )
)