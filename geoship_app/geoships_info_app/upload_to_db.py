import pandas as pd
from openpyxl import load_workbook
import os
from django.conf import settings

path = settings.PATH_FILES


def parse_file_data(file):
    path_file = path+file
    print(path_file)
    wb = load_workbook(path_file)
    sheet = wb.worksheets[0]
    data = sheet.values
    df = pd.DataFrame(data).values[1:]


def parse_files(list_files):
    for file in list_files:
        parse_file_data(file)


def check_files():
    list_files = os.listdir(path)
    if len(list_files) >= 1:
        parse_files(list_files)
