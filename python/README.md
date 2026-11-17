# Python exercises

These examples come from my AWS re/Start Python practice. I simplified the repeated scripts, added input checks and made file paths work from any working directory.

| File                                         | What I practised                                           |
| -------------------------------------------- | ---------------------------------------------------------- |
| [caesar_cipher.py](caesar_cipher.py)         | Functions, loops, strings and wrapping around the alphabet |
| [fleet_inventory.py](fleet_inventory.py)     | Reading CSV rows into dictionaries and converting numbers  |
| [insulin_sequences.py](insulin_sequences.py) | Reading a file, slicing strings and saving results as JSON |

Run the commands in the main README from the repository folder. The cipher also supports `--decrypt`:

```sh
python3 python/caesar_cipher.py "KHOOR" 3 --decrypt
```

The cipher keeps punctuation and converts English letters to uppercase.

The sequence exercise splits the supplied 110-character string into four sections with lengths 24, 30, 35 and 21. It prints JSON by default. Use `--output result.json` to save it.

The tests check round trips, file reading, numeric conversion and incorrect input. They can run without network access or extra packages.
