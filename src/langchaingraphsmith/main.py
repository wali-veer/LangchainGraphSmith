import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello, LangchainGraphSmith!")
    print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
