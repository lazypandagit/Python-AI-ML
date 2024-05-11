import smtplib
from email.message import EmailMessage as Email
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv
# loading variables from .env file
load_dotenv() 
 


def sendEmail(to: str,
              subject: str,
              body: str) -> None:
    # Docstrics for intelliSense

    """Sends Email to an mail address

    Args:
        to (str): _Email address of the recipient_
        subject (str): _Subject of the email_
        body (str): _Body of the email_
    """

    # Username and Password of the sender
    user: str = "ani1010200@gmail.com"
    password: str = os.getenv('EMAIL_APP_PASSWORD')

    # Constructing the email
    emailMsg = Email()
    emailMsg["from"] = user
    emailMsg["to"] = to
    emailMsg["subject"] = subject
    emailMsg.set_content(body)

    # SMTP Server setup
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(emailMsg)
    server.quit()
    print(f"Email sent to {to}")


if __name__ == "__main__":
    recipientEMAIL: str = input("Enter recipient's E-mail address: ")
    sendEmail(recipientEMAIL, "Test email", "This is a test email \n Hello world")
