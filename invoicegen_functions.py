from PIL import Image, ImageDraw, ImageFont
import imghdr
import gspread
import time
from datetime import datetime
from booksheet_functions import *
gcb = gspread.service_account(filename='credentials.json')
shb = gcb.open_by_url("https://docs.google.com/spreadsheets/d/1Z49E0dyDrIcviyWq9JZS0xCpXioGy1EQ6pJ8odVY6aI/edit?usp=sharing")
worksheetb = shb.worksheet("Sheet1")
lb = len(worksheetb.col_values(1))
inv = "INV00" + str(lb)
img = Image.open('template.jpg')
title_font1 = ImageFont.truetype(r'C:\Windows\Fonts\bahnschrift.ttf', 30)
d1 = ImageDraw.Draw(img)

def genInvoice(cstmr_name, pyt_met, BIN1, b1qty, BIN2=None, b2qty=None, BIN3=None, b3qty=None, BIN4=None, b4qty=None, BIN5=None, b5qty=None):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    d1.text((410, 329), inv, fill="Black", font=title_font1)
    d1.text((255, 384), cstmr_name, fill="Black", font=title_font1)
    d1.text((380, 438), dt_string, fill="Black", font=title_font1)
    d1.text((420, 492), pyt_met, fill="Black", font=title_font1)
    total = int(B1(BIN1,b1qty))
    if(BIN2!=None):
        total = total + int(B2(BIN2, b2qty))
        if (BIN3 != None):
            total = total + int(B3(BIN3, b3qty))
            if (BIN4 != None):
                total = total + int(B4(BIN4, b4qty))
                if (BIN5 != None):
                    total = total + int(B5(BIN5, b5qty))
    d1.text((875, 1473), str(total), fill="Black", font=title_font1)
    fname = inv + ".jpg"
    img.show()
    img.save(fname)
    worksheetb.update_cell(lb + 1, 1, inv)
    worksheetb.update_cell(lb + 1, 2, cstmr_name)
    worksheetb.update_cell(lb + 1, 3, dt_string)
    worksheetb.update_cell(lb + 1, 4, total)
    worksheetb.update_cell(lb + 1, 5, pyt_met)

def B1(BIN1, b1qty):
    b1name = getBookName(BIN1)
    b1price = int(getBookPrice(BIN1))
    b1amt = b1qty*b1price
    d1.text((150, 700), b1name, fill="Black", font=title_font1)
    d1.text((700, 700), str(b1qty), fill="Black", font=title_font1)
    d1.text((800, 700), str(b1price), fill="Black", font=title_font1)
    d1.text((925, 700), str(b1amt), fill="Black", font=title_font1)
    b1str = "(" + str(b1name) + "," + str(b1qty) + "," + str(b1amt) + ")"
    worksheetb.update_cell(lb + 1, 6, b1str)
    incqsold(BIN1, int(b1qty))
    decqavail(BIN1, int(b1qty))
    return b1amt

def B2(BIN1, b1qty):
    b1name = getBookName(BIN1)
    b1price = int(getBookPrice(BIN1))
    b1amt = b1qty*b1price
    d1.text((150, 775), str(b1name), fill="Black", font=title_font1)
    d1.text((700, 775), str(b1qty), fill="Black", font=title_font1)
    d1.text((800, 775), str(b1price), fill="Black", font=title_font1)
    d1.text((925, 775), str(b1amt), fill="Black", font=title_font1)
    b1str = "(" + str(b1name) + "," + str(b1qty) + "," + str(b1amt) + ")"
    worksheetb.update_cell(lb + 1, 7, b1str)
    incqsold(BIN1, int(b1qty))
    decqavail(BIN1, int(b1qty))
    return b1amt

def B3(BIN1, b1qty):
    b1name = getBookName(BIN1)
    b1price = int(getBookPrice(BIN1))
    b1amt = b1qty * b1price
    d1.text((150, 850), b1name, fill="Black", font=title_font1)
    d1.text((700, 850), str(b1qty), fill="Black", font=title_font1)
    d1.text((800, 850), str(b1price), fill="Black", font=title_font1)
    d1.text((925, 850), str(b1amt), fill="Black", font=title_font1)
    b1str = "(" + str(b1name) + "," + str(b1qty) + "," + str(b1amt) + ")"
    worksheetb.update_cell(lb + 1, 8, b1str)
    incqsold(BIN1, int(b1qty))
    decqavail(BIN1, int(b1qty))
    return b1amt

def B4(BIN1, b1qty):
    b1name = getBookName(BIN1)
    b1price = int(getBookPrice(BIN1))
    b1amt = b1qty * b1price
    d1.text((150, 925), b1name, fill="Black", font=title_font1)
    d1.text((700, 925), str(b1qty), fill="Black", font=title_font1)
    d1.text((800, 925), str(b1price), fill="Black", font=title_font1)
    d1.text((925, 925), str(b1amt), fill="Black", font=title_font1)
    b1str = "(" + str(b1name) + "," + str(b1qty) + "," + str(b1amt) + ")"
    worksheetb.update_cell(lb + 1, 9, b1str)
    incqsold(BIN1, int(b1qty))
    decqavail(BIN1, int(b1qty))
    return b1amt

def B5(BIN1, b1qty):
    b1name = getBookName(BIN1)
    b1price = int(getBookPrice(BIN1))
    b1amt = b1qty * b1price
    d1.text((150, 1000), b1name, fill="Black", font=title_font1)
    d1.text((700, 1000), str(b1qty), fill="Black", font=title_font1)
    d1.text((800, 1000), str(b1price), fill="Black", font=title_font1)
    d1.text((925, 1000), str(b1amt), fill="Black", font=title_font1)
    b1str = "(" + str(b1name) + "," + str(b1qty) + "," + str(b1amt) + ")"
    worksheetb.update_cell(lb + 1, 10, b1str)
    incqsold(BIN1, int(b1qty))
    decqavail(BIN1, int(b1qty))
    return b1amt
