import smtplib
from email.message import EmailMessage as Email


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
    password: str = "vbhjchmbjmiojmnc"

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
    print("Email sent")


if __name__ == "__main__":
    senderEMAIL: str = input("Enter sender's E-mail address: ")
    sendEmail(senderEMAIL, "Test email", "This is a test email \n Hello world")
