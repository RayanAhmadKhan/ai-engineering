# Tokenizer Explorer

An interactive tokenizer explorer using OpenAI's `o200k_base` encoding. It
displays token IDs and their byte representations, then verifies that the text
can be reconstructed from the tokens.

## Run

Install the dependency and start the explorer:

```powershell
python -m pip install tiktoken
python tokenizer_explorer.py
```

Type `exit` to leave the interactive prompt.

## Test

```powershell
python -m unittest test_tokenizer_explorer.py
```
