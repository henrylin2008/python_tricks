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