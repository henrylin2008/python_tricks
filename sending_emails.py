import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.starttls()  # start the smtp session

# password = getpass.getpass('Password: ')  # getpass module hides the password while you passing it in

email = input("Email: ")    # getpass.getpass("Email: ")
password = getpass.getpass("Password: ")  # app specific password
smtp_object.login(email, password)

from_address = email
to_address = "(recipient email address)"
subject = input("Enter the subject line: ")
message = input("Enter the body message: ")
msg = "Subject: " + subject + '\n' + message

smtp_object.sendmail(from_address, to_address, msg)

smtp_object.quit()  # Close the session


# Viewing Emails:
# import imaplib
# M = imaplib.IMAP4_SSL('imap.gmail.com')
# import getpass
# email = input("Email: ")  # getpass.getpass("Email: ")
# password = getpass.getpass("Password: ")
# M.login(email.password)
# M.list()  # list of email folders
# M.select('inbox') # ('OK', [b'23432'])
# ## Keywords:
# # 'BEFORE date', 'ON date', 'SINCE date', 'FROM some_string', 'TO some_string',
# # 'CC some_string' and/or 'BCC some_string', 'SUBJECT string', 'BODY string', 'TEXT "string with spaces"
# # 'SEEN', 'UNSEEN', 'ANSWERED', 'UNANSWERED', 'DELETED', 'UNDELETED'
# type, data = M.search(None, 'BEFORE 01-NOV-2011') # USE keywords above
# type, data = M.search(None, 'FROM user@email.com') # USE keywords above
# type, data = M.search(None, 'SUBJECT "subject/title"') # USE keywords above
# email_id = data[0]
# result, email_data = M.fetch(email_id, '(RFC822)')
# raw_email = email_data[0][1]
# raw_email_string = raw_email.decode('utf-8')
# import email
# email_message = email.message_from_string(raw_email_string
# for part in email_message.walk():
#     if part.get_content_type() == 'text/plain':   # or 'text/html'
#        body = part.get_payload(decode=True)
#        print(body)


# Send email with sendgrid
# import os
# import sendgrid
# from sendgrid.helpers.mail import Content, Email, Mail
#
# sg = sendgrid.SendGridAPIClient(
#     apikey=os.environ.get("SENDGRID_API_KEY")
# )
# from_email = Email("my@gmail.com")
# to_email = Email("your@gmail.com")
# subject = "A test email from Sendgrid"
# content = Content(
#     "text/plain", "Here's a test email sent through Python"
# )
# mail = Mail(from_email, subject, to_email, content)
# response = sg.client.mail.send.post(request_body=mail.get())
#
# # The statements below can be included for debugging purposes
# print(response.status_code)
# print(response.body)
# print(response.headers)
