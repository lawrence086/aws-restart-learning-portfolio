"""Read a fictional vehicle inventory and print a short summary."""

import csv
from pathlib import Path


DATA_FILE = Path(__file__).parent / "data" / "car_fleet.csv"
NUMBER_FIELDS = {
    "year": int,
    "range": int,
    "topSpeed": int,
    "zeroSixty": float,
    "mileage": int,
}
REQUIRED_FIELDS = {"vin", "make", "model", *NUMBER_FIELDS}


def load_vehicles(path):
    vehicles = []
    with Path(path).open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        fieldnames = reader.fieldnames or []
        if len(fieldnames) != len(REQUIRED_FIELDS) or set(fieldnames) != REQUIRED_FIELDS:
            raise ValueError("The CSV must contain each expected vehicle column once.")
        for row in reader:
            if None in row or any(value is None or not value.strip() for value in row.values()):
                raise ValueError(f"Missing or extra values on CSV line {reader.line_num}.")
            vehicle = {name: value.strip() for name, value in row.items()}
            try:
                for name, convert in NUMBER_FIELDS.items():
                    vehicle[name] = convert(vehicle[name])
            except ValueError as error:
                raise ValueError(f"Invalid number on CSV line {reader.line_num}.") from error
            vehicles.append(vehicle)
    return vehicles


def main():
    try:
        vehicles = load_vehicles(DATA_FILE)
    except (OSError, ValueError) as error:
        raise SystemExit(f"Could not read inventory: {error}") from error
    print(f"Vehicles: {len(vehicles)}")
    for vehicle in vehicles:
        print(f"{vehicle['year']} {vehicle['make']} {vehicle['model']}: "
              f"mileage {vehicle['mileage']:,}")


if __name__ == "__main__":
    main()
