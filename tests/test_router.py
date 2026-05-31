from src.routers.rule_router import route_request


tests = [
    "Explain machine learning",
    "Summarize AI is transforming industries",
    "Give me startup ideas about fitness"
]


for t in tests:

    print("\nINPUT:", t)
    print("OUTPUT:", route_request(t))
    print("-" * 50)