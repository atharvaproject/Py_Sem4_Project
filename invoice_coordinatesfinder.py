from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import imghdr

img = Image.open('template.jpg')

title_font1 = ImageFont.truetype(r'C:\Windows\Fonts\bahnschrift.ttf', 30)

d1 = ImageDraw.Draw(img)
# (x,y) coordinates determine the position of text.
d1.text((410, 329), "INV00100", fill="Black", font=title_font1)
d1.text((255, 384), "John Doe", fill="Black", font=title_font1)
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
d1.text((380, 438), dt_string, fill="Black", font=title_font1)
d1.text((420, 492), 'CASH', fill="Black", font=title_font1)

d1.text((150, 700), 'The A.B.C. Murders', fill="Black", font=title_font1)
d1.text((700, 700), '2', fill="Black", font=title_font1)
d1.text((800, 700), '300', fill="Black", font=title_font1)
d1.text((925, 700), 'Rs. 600', fill="Black", font=title_font1)
d1.text((150, 775), 'Murder on the Orient Express', fill="Black", font=title_font1)
d1.text((700, 775), '2', fill="Black", font=title_font1)
d1.text((800, 775), '300', fill="Black", font=title_font1)
d1.text((925, 775), 'Rs. 600', fill="Black", font=title_font1)
d1.text((150, 850), 'Death on the Nile', fill="Black", font=title_font1)
d1.text((700, 850), '2', fill="Black", font=title_font1)
d1.text((800, 850), '300', fill="Black", font=title_font1)
d1.text((925, 850), 'Rs. 600', fill="Black", font=title_font1)
d1.text((150, 925), 'The Mysterious Affair at Styles', fill="Black", font=title_font1)
d1.text((700, 925), '2', fill="Black", font=title_font1)
d1.text((800, 925), '300', fill="Black", font=title_font1)
d1.text((925, 925), 'Rs. 600', fill="Black", font=title_font1)
d1.text((150, 1000), 'The Murder of Roger Ackroyd', fill="Black", font=title_font1)
d1.text((700, 1000), '2', fill="Black", font=title_font1)
d1.text((800, 1000), '300', fill="Black", font=title_font1)
d1.text((925, 1000), 'Rs. 600', fill="Black", font=title_font1)
d1.text((875, 1473), 'Rs. 3000', fill="Black", font=title_font1)

img.show()
img.save('temporary.jpg')