#!/usr/bin/python3
"""
This module contains a function that reads data from a CSV file
and converts it into a JSON file format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.

    Args:
        csv_filename (str): The name of the CSV file to read from.

    Returns:
        bool: True if the conversion is successful, False otherwise.
    """
    try:
        # CSV faylını oxuyuruq və sətirləri lüğət (dict) kimi yığırıq
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        # Məlumatları data.json faylına yazırıq
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
