import gspread
import time
gc = gspread.service_account(filename='')
sh = gc.open_by_url("")
worksheet = sh.worksheet("Sheet1")
l = len(worksheet.col_values(1))

def dispBIN():
    for i in range(2,l+1):
        print(worksheet.cell(i, 1).value, worksheet.cell(i, 2).value)

def addBook(name, price, q_avail, q_sold):
    BIN = "B00" + str(l)
    worksheet.update_cell(l+1, 1, BIN)
    worksheet.update_cell(l+1, 2, name)
    worksheet.update_cell(l+1, 3,  price)
    worksheet.update_cell(l+1, 4, q_avail)
    worksheet.update_cell(l + 1, 5, q_sold)

def editbookprice(BIN, new_price):
    cell = worksheet.find(BIN)
    worksheet.update_cell(cell.row, 3, new_price)

def editqavail(BIN, q_avail):
    cell = worksheet.find(BIN)
    worksheet.update_cell(cell.row, 4, q_avail)

def getBookName(BIN):
    cell = worksheet.find(BIN)
    return worksheet.cell(cell.row, 2).value

def getBookPrice(BIN):
    cell = worksheet.find(BIN)
    return worksheet.cell(cell.row, 3).value

def incqsold(BIN, qtysold):
    cell = worksheet.find(BIN)
    old = int(worksheet.cell(cell.row, 5).value)
    new = old+qtysold
    worksheet.update_cell(cell.row, 5, new)

def decqavail(BIN, qavail):
    cell = worksheet.find(BIN)
    old = int(worksheet.cell(cell.row, 4).value)
    new = old-qavail
    worksheet.update_cell(cell.row, 4, new)

def delRecord(BIN):
    cell = worksheet.find(BIN)
    worksheet.update_cell(cell.row, 2, 'No longer available.')
    worksheet.update_cell(cell.row, 3, 'No longer available.')
    worksheet.update_cell(cell.row, 4, 'No longer available.')
    worksheet.update_cell(cell.row, 5, 'No longer available.')



