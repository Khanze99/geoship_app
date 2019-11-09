import pandas as pd
from openpyxl import load_workbook
import os
import datetime
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from .models import Vessel, History

path = settings.PATH_FILES


def parse_file_data(file):
    path_file = path+file
    wb = load_workbook(path_file)
    sheet = wb.worksheets[0]
    data = sheet.values
    df = pd.DataFrame(data).values[1:]
    for data in df:
        date = datetime.datetime.combine(data[1], data[2])
        code = data[0]
        lat = data[3]
        lon = data[4]
        name = data[5]
        try:
            vessel = Vessel.objects.get(code=code)
        except ObjectDoesNotExist:
            vessel = Vessel.objects.create(name=name, code=code)
        obj = History.objects.create(vessel=vessel, lat=lat, lon=lon, geo_date=date)
        print(obj.vessel.name)


def parse_files(list_files):
    for file in list_files:
        parse_file_data(file)


def check_files():
    list_files = os.listdir(path)
    if len(list_files) >= 1:
        parse_files(list_files)
    else:
        return "No files"
