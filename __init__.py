from dotenv import load_dotenv
import imaplib
import email
import os


load_dotenv()

email_host = os.getenv('E_MAIL_HOST')
email_user = os.getenv('E_MAIL_USERNAME')
email_pass = os.getenv('E_MAIL_PASSWORD')
import_path = os.getenv('PAPERMERGE_IMPORT_PATH')

imap = imaplib.IMAP4_SSL(email_host, 993)

imap.login(email_user, email_pass)

imap.select('Inbox')

status, data = imap.search(None, 'ALL')

for email_num in data[0].split():
    _, data = imap.fetch(email_num, '(RFC822)')
    raw_email = data[0][1]

    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    for part in email_message.walk():
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join(import_path, fileName)
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(email_message).split(
                "Subject: ", 1)[1].split("\nTo:", 1)[0]
    imap.store(email_num, "+FLAGS", "\\Deleted")

imap.expunge()
