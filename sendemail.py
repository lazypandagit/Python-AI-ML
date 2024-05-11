import smtplib
from email.message import EmailMessage as Email
from dotenv import dotenv_values


####steps to add env variables
# pip install "python-dotenv[cli]"
# $ dotenv set USER foo
# $ dotenv set EMAIL foo@example.org
# dotenv list
# from: https://pypi.org/project/python-dotenv/#getting-started
######

# loading variables from .env file
config = dotenv_values(".env")


def sendEmail(to: str, subject: str, body: str) -> None:
    # Docstrics for intelliSense

    """Sends Email to an mail address

    Args:
        to (str): _Email address of the recipient_
        subject (str): _Subject of the email_
        body (str): _Body of the email_
    """

    # Username and Password of the sender
    user: str = "ani1010200@gmail.com"
    password: str | None = config["EMAIL_APP_PASSWORD"]

    if password == None:
        print("Password not found in .env file \n Add Password")
        return None

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
