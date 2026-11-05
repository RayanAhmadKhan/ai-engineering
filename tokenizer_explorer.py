import tiktoken

# Load the GPT-4o tokenizer encoding
encoding = tiktoken.get_encoding("o200k_base")


def tokenize(text: str) -> list[int]:
    """Convert input text into token IDs."""
    return encoding.encode(text)


def detokenize(token_ids: list[int]) -> str:
    """Convert token IDs back into text."""
    return encoding.decode(token_ids)


def inspect_tokens(text: str) -> None:
    """Display token-level information."""

    token_ids = tokenize(text)

    print("\nOriginal text:")
    print(text)

    print("\nToken information:")

    for index, token_id in enumerate(token_ids):
        token_bytes = encoding.decode_single_token_bytes(token_id)

        print(
            f"Position: {index} | "
            f"Token ID: {token_id} | "
            f"Bytes: {token_bytes!r}"
        )

    print("\nTotal tokens:", len(token_ids))

    reconstructed = detokenize(token_ids)

    print("\nReconstructed text:")
    print(reconstructed)

    print("\nRound-trip successful:", reconstructed == text)


def main():
    print("===== AI TOKENIZER EXPLORER =====")

    while True:
        text = input("\nEnter text (or type exit): ")

        if text.lower() == "exit":
            break

        inspect_tokens(text)


if __name__ == "__main__":
    main()