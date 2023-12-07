# Python SMTP Module
Sending mail from Python using SMTP Module. Python provides smtplib module, which defines an SMTP client session object that can be used to send mails to any Internet machine with an SMTP or ESMTP listener daemon.

# Python SMTP Source Code

This repository contains a Python script for sending emails using the `smtplib` module. The script establishes a connection to an SMTP server, logs in with the provided credentials, and sends an email to the specified recipient.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your machine.
- An email account with an SMTP server (e.g., Gmail) that allows you to send emails programmatically.

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Kunal-kawate/Python_SMTP_Source_Code.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Python_SMTP_Source_Code
    ```

3. Open the `SMTP.py` file and update the following variables with your email and server information:

    ```python
    HOST = "smtp.gmail.com"
    PORT = 587

    FROM_EMAIL = "Sender_Mail_Here"
    PASSWORD = 'Password'
    ```

## Usage

Run the script using the following command:

```bash
python SMTP.py
```

The script will prompt you to enter the recipient's email address, the email subject, and the message. After providing the necessary information, the script will attempt to send the email and display status information for each step of the process.

**Note:** If you are using Gmail, make sure to enable "Less secure app access" in your account settings or use an "App Password" for the script to log in successfully.

## Disclaimer

This script is provided as-is and may require adjustments based on your specific email server and security settings. Use it responsibly and ensure compliance with the terms of service of your email provider. Made with Love | KunyaThing
