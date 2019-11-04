import pandas as pd
from openpyxl import load_workbook
from itertools import islice

wb = load_workbook('20190801.xlsx')
sheet = wb.get_sheet_by_name('ais-kara-20190723132714597')
data = sheet.values


df = pd.DataFrame(data)
print(df.values[1:])
