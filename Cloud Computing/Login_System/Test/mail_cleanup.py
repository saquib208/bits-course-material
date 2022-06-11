import imaplib
import smtplib
import time
import imaplib
import email
import traceback

# account credentials and other configs
# replace with you Gmail username and password
username = "saquibelec208@gmail.com"
password = "mjpiqmbpwyykshcr"
folderToDeleteEmailsFrom = '"[Gmail]/All Mail"'
trashFolder = '[Gmail]/Trash'

# create IMAP4 with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
# authenticate
imap.login(username, password)

# list all the mailboxes present
print(f'list all the inbox-->>{imap.list()}')
# SECTION 1: select the mailbox to delete emails from
imap.select(folderToDeleteEmailsFrom)

print(f'list all the inbox-->>{imap.recent()}')
#gmail_search = 'category:promotions'
gmail_search='technews@techgig.com'
#gmail_search ='techgig'
#typ, [msg_ids] = imap.search(None, 'X-GM-RAW', gmail_search)
# print(f'Message type-->>{typ}')
# print(f'message id -->{msg_ids}')
# msg_count = len(msg_ids)
#print("Found message count: ", msg_count)

# status, messages = imap.search(None,"ALL" )
# print(f'Message type-->>{status}')
# print(f'message id -->{messages}')
imap.select(folderToDeleteEmailsFrom)
data = imap.search(None,'X-GM-RAW' ,gmail_search)

mail_ids = data[1]
id_list = mail_ids[0].split()
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])

for i in range(latest_email_id, first_email_id, -1):
    data = imap.fetch(str(i), '(RFC822)')
    for response_part in data:
        arr = response_part[0]
        if isinstance(arr, tuple):
            msg = email.message_from_string(str(arr[1], 'utf-8'))
            email_subject = msg['subject']
            email_from = msg['from']
            print('From : ' + email_from + '\n')
            print('Subject : ' + email_subject + '\n')


# if msg_count == 0:
#     print("No new messages matching the criteria to be deleted.")
# else:
#     if isinstance(msg_ids, bytes):
#         # if it's a bytes type, decode to str
#         msg_ids = msg_ids.decode()
#
#     # SECTION 2: imap store command allows us to batch perform an operation
#     # on a bunch of comma-separated msg ids
#     msg_ids = ','.join(msg_ids.split(' '))
#     print("Moving to Trash using X-GM_LABELS.")
#     imap.store(msg_ids, '+X-GM-LABELS', '\\Trash')
#
#     # SECTION 3: Once all the required emails have been sent to Trash,
#     # permanently delete emails marked as deleted from the selected folder
#     print("Emptying Trash and expunge...")
#     imap.select(trashFolder)
#     imap.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
#     imap.expunge()
#
# # SECTION 4: close the mailbox once the task is done
# print("Done. Closing connection & logging out.")
# imap.close()
# # logout
# imap.logout()