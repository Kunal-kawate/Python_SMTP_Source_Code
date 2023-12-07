import smtplib

HOST = "smtp.gmail.com"
PORT = 587

FROM_EMAIL = "Sender_Mail_Here"
PASSWORD = 'Password'

TO_EMAIL = input("Mail to: ")
subject= input('Enter Mail Subject: ')
msg=input('Enter the Message: ')
MESSAGE = """Subject: {}
{}""".format(subject,msg)

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()