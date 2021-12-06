# if your email example@yahoo.com it's smtpserver is smtp.att.yahoo.com'
import smtplib
from email.message import EmailMessage

# intilization of Mail class
class Mail:

    def send_email(self, name, price, product, EMAIL, PASSWORD, SMTP_SERVER,DESTINATION):
        self.msg = EmailMessage()
        self.msg['Subject'] = f'Price Drop For {name}'
        self.msg['From'] = EMAIL
        self.msg['To'] = DESTINATION
        self.msg.set_content(f'Price Dropped to ₹{price} \nVisit  {product}')
        

        with smtplib.SMTP(SMTP_SERVER) as self.connection:
            self.connection.starttls()
            self.connection.login(EMAIL, PASSWORD)
            self.connection.send_message(self.msg)





