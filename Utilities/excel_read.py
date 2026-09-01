import openpyxl

class NewExcelReader:
    def read_excel_cell(self,row_no,col_no):
        book=openpyxl.load_workbook("C:\\Users\\Jesma hussain\\Desktop\\pytest\\excel.xlsx")
        sheet=book["sign_up"]
        return sheet.cell(row=row_no,column=col_no).value