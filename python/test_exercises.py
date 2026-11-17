import tempfile
import unittest
from pathlib import Path

from caesar_cipher import decrypt, encrypt
from fleet_inventory import DATA_FILE as FLEET_FILE, load_vehicles
from insulin_sequences import DATA_FILE as SEQUENCE_FILE, split_sequence


class CipherTests(unittest.TestCase):
    def test_known_message(self):
        self.assertEqual(encrypt("Hello, world!", 3), "KHOOR, ZRUOG!")

    def test_round_trip_with_large_and_negative_shifts(self):
        for shift in (-55, -1, 0, 3, 26, 100):
            with self.subTest(shift=shift):
                self.assertEqual(decrypt(encrypt("Az 09!?", shift), shift), "AZ 09!?")

    def test_empty_message(self):
        self.assertEqual(encrypt("", 3), "")


class InventoryTests(unittest.TestCase):
    def test_duplicate_header_is_rejected(self):
        lines = FLEET_FILE.read_text().splitlines()
        content = lines[0] + ",mileage\n" + lines[1] + ",999\n"
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "vehicles.csv"
            path.write_text(content)
            with self.assertRaisesRegex(ValueError, "column once"):
                load_vehicles(path)

    def test_sample_rows_and_types(self):
        vehicles = load_vehicles(FLEET_FILE)
        self.assertEqual(len(vehicles), 4)
        self.assertEqual(vehicles[0]["model"], "Coupe")
        self.assertEqual(vehicles[-1]["mileage"], 0)
        self.assertIsInstance(vehicles[0]["year"], int)
        self.assertIsInstance(vehicles[0]["zeroSixty"], float)

    def test_bad_input(self):
        header = FLEET_FILE.read_text().splitlines()[0]
        cases = ["wrong,columns\na,b\n", header + "\na,b\n",
                 header + "\nx,Example,Car,wrong,1,2,3,4\n",
                 header + "\nx,Example,Car,2020,1,2,3,4,extra\n"]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "vehicles.csv"
            for content in cases:
                with self.subTest(content=content):
                    path.write_text(content)
                    with self.assertRaises(ValueError):
                        load_vehicles(path)


class SequenceTests(unittest.TestCase):
    def test_sections_reconstruct_input(self):
        sequence = SEQUENCE_FILE.read_text().strip()
        sections = split_sequence(sequence)
        self.assertEqual([len(value) for value in sections.values()], [24, 30, 35, 21])
        self.assertEqual("".join(sections.values()), sequence)
        self.assertEqual(sections["a_chain"], "giveqcctsicslyqlenycn")

    def test_uppercase_input(self):
        sequence = SEQUENCE_FILE.read_text()
        self.assertEqual(split_sequence(sequence.upper()), split_sequence(sequence))

    def test_invalid_sequence(self):
        for sequence in ("abc", "a" * 109, "a" * 109 + "1", "a" * 109 + " "):
            with self.subTest(sequence=sequence):
                with self.assertRaises(ValueError):
                    split_sequence(sequence)


if __name__ == "__main__":
    unittest.main()
