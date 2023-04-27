import csv
import os
from typing import List

input_directory = 'output'
output_file = 'cleaned_data.csv'


## Keeps only the rows that have a Url attribute

def get_csv_files_in_directory(directory: str) -> List[str]:
    """Return a list of CSV files in the given directory"""
    csv_files = []
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            csv_files.append(os.path.join(directory, file))
    return csv_files


def clean_csv_file(input_file: str, output_file: str) -> None:
    """Clean the input CSV file and save the result to the output CSV file"""
    with open(input_file, 'r') as input_csv, open(output_file, 'a', newline='') as output_csv:
        reader = csv.DictReader(input_csv)
        writer = csv.DictWriter(output_csv, fieldnames=reader.fieldnames)

        for row in reader:
            if row.get('Url'):
                writer.writerow(row)


if __name__ == '__main__':
    # Get a list of CSV files in the input directory
    csv_files = get_csv_files_in_directory(input_directory)

    # Clean each CSV file and append the cleaned rows to the output CSV file
    for csv_file in csv_files:
        clean_csv_file(csv_file, output_file)
