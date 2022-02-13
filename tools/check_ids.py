#!/usr/bin/env python3

"""Read in a CSV file of ids and names and see if they are present."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import sys
import logging
import csv
import argparse

from fitfile import Manufacturer, GarminProduct


class IdFile():
    """Class for importing name, id pairs from a CSV file."""

    logger = logging.getLogger(__name__)

    def __init__(self, filename, delimiter=','):
        """Return an instance of IdFile."""
        self.filename = filename
        self.delimiter = delimiter

    def process_file(self, test_enum):
        """Import the file."""
        test_enum_ids = [item.value for item in test_enum]
        self.logger.info("Reading file: " + self.filename)
        with open(self.filename) as csv_file:
            read_csv = csv.DictReader(csv_file, delimiter=self.delimiter)
            for row in read_csv:
                id = int(row['id'])
                if id not in test_enum_ids:
                    print(f'{row["name"]} = {id}')


def main(argv):
    """Check if a CSV file of name, id pairs is present in the FIT enums."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--manufacturer", help="Check if name, id pairs are present in the manufacturer enum.")
    parser.add_argument("-p", "--product", help="Check if name, id pairs are present in the product enum.")
    args = parser.parse_args()

    if args.manufacturer:
        idfile = IdFile(args.manufacturer)
        idfile.process_file(Manufacturer)
    if args.product:
        idfile = IdFile(args.product)
        idfile.process_file(GarminProduct)


if __name__ == "__main__":
    main(sys.argv[1:])
