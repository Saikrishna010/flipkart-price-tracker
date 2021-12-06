PRODUCT=" URL of filpkart url"
# example
# https://www.flipkart.com/apple-iphone-12-black-64-gb/p/itma2559422bf7c7?pid=MOBFWBYZU5FWK2VP&lid=LSTMOBFWBYZU5FWK2VPUYA8BN&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=hp_banner_1_7.bannerX3.BANNER_1RVMY8JNLOQZ&fm=neo%2Fmerchandising&iid=ab55aeb9-5cf9-4930-b476-83b70dadd82b.MOBFWBYZU5FWK2VP.SEARCH&ppt=hp&ppn=homepage&ssid=tx3kvwc7f40000001638786009304
CURRENT_PRICE="current price"
# example
# 55999
DEAL_PRICE="at which price you want buy it"
# example
# 50000

# for gmail it is smtp.gmail.com if your email is diffrent with 
#  a simple google search your could find yours
SMTP_SERVER= "your email smpt server"
# example
# smpt.gmail.com
EMAIL="your email"
# example
# example@email.com
PASSWORD="your email password"
#example
# mypassword123
DESTINATION="email address of which you want to send message"
# example
# tomyfriend@email.com


from sendMail import Mail
from scraper import Scraper

# scraper object
scraper= Scraper()
# mail object
mail=Mail()
# storing return values of price and name
current_price, product_name=scraper.start_scarp(PRODUCT)

# checking for the price  drop
if current_price <= DEAL_PRICE:
  # if price droped calling send_email function
  mail.send_email(product_name, current_price, PRODUCT, EMAIL, PASSWORD, SMTP_SERVER, DESTINATION)
  

