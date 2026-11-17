"""Split the lab's sample sequence into four sections."""

import argparse
import json
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "insulin_sequence.txt"


def split_sequence(sequence):
    sequence = sequence.strip().lower()
    if len(sequence) != 110 or any(letter not in "acdefghiklmnpqrstvwy" for letter in sequence):
        raise ValueError("Expected 110 amino-acid letters with no numbers or spaces.")
    return {
        "signal": sequence[:24],
        "b_chain": sequence[24:54],
        "c_peptide": sequence[54:89],
        "a_chain": sequence[89:],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DATA_FILE)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        sections = split_sequence(args.input.read_text(encoding="utf-8"))
        result = {name: {"sequence": value, "length": len(value)}
                  for name, value in sections.items()}
        output = json.dumps(result, indent=2) + "\n"
        if args.output:
            args.output.write_text(output, encoding="utf-8")
        else:
            print(output, end="")
    except (OSError, ValueError) as error:
        raise SystemExit(f"Could not process sequence: {error}") from error


if __name__ == "__main__":
    main()
