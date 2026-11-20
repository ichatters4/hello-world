def get_greeting(name: str = "World") -> str:
    return f"Hello, {name}!"

def main() -> None:
    print(get_greeting())
