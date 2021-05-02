import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime

def check_price():
    is_avail = False
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    avail = soup.find(id="availability").get_text()
    if avail.strip() == "In stock.":
        is_avail = True
    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price = price[2:]
    converted_price = converted_price.replace(",", "")
    convert = float(converted_price)
    print(f"The price of the new iPhone 12 is {convert} and is Available : {is_avail}")
    if convert < float(70000):
        send_email(convert, is_avail)
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y %H:%M:%S")
    file_string = f"Price : {convert} Date : {current_date}\n"
    print(file_string)
    appendFile = open(r"iphone_price.txt", "a")
    appendFile.write(file_string)
    appendFile.close()


def send_email(convert, item_avail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('burner.email6878@gmail.com', 'rufkhduytttyyerv')
    subject = "Price Fell Down"
    if item_avail:
        body = f"The price of iphone is Rs. {convert} and is Available"
    else:
        body = f"The price of iphone is Rs. {convert} but is not Available"
    msg = f"Subject: {subject}\n\n{body}\nClick this link :{URL}"

    server.sendmail(
        'burner.email6878@gmail.com',
        'atharvkekare@gmail.com',
        msg
    )
    print("Email has been sent")
    server.quit()

URL = 'https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5WD9D6/ref=sr_1_1?dchild=1&keywords=iphone+12&qid' \
      '=1619925185&sr=8-1 '

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.93 Safari/537.36'}

check_price()
