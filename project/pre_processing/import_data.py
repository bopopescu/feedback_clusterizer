
# ================ BEGIN Lybrary Imports: ==================#

import xlrd
import xlwt

# ================ END Lybrary Imports: ====================#

# Data workbook describe:

wb_data = xlrd.open_workbook("Reviews.xls") 

print("")
print("Data workbook describe: \n")
print("Number of sheets: ", wb_data.nsheets)
first_sheet_data = wb_data.sheet_by_index(0)
print("Number of rows: ", first_sheet_data.nrows)
print("Number of coluns: ", first_sheet_data.ncols)
