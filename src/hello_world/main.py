
def get_greeting(name: str = "World") -> str:
    return f"Hello, {name}!"

def main() -> None:
    """ Entry point"""
    print(get_greeting())

if __name__ == "__main__":
    main()
