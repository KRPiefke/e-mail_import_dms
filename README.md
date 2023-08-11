# Mail Attachment Import Script for Paperless DMS
Welcome to the Mail Attachment Import Script repository! This repository contains a simple script that automates the process of logging into a configurable email account, fetching emails, and extracting attachments from incoming mails. These attachments are then moved to a specified folder, which in this case is the import folder for the Paperless Document Management System (DMS).

## Script Overview
The script is designed to streamline the process of importing attachments from emails into your Paperless DMS import folder. It is written in Python, and it works as follows:

It connects to the configured email account using provided credentials.
It searches for incoming emails with attachments.
It downloads the attachments from these emails.
It moves the downloaded attachments to the designated import folder for the Paperless DMS.
It deletes the email.

Configure the script by editing the necessary variables in the the .env file. Update the email account details and the Paperless DMS import folder path.

Please ensure you have [insert any dependencies or prerequisites here, e.g., Python and required libraries] installed before running the script.

Important Notes
Security: Make sure to keep your credentials and sensitive information secure. Avoid hardcoding credentials directly into the script. Please use the .env file for this case.
Automation: You can schedule this script to run at specific intervals using tools like cron jobs (Linux) or Task Scheduler (Windows).
