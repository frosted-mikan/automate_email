import random
import email, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_file = open("text.txt", "r")
list = []
for line in my_file:
    upper_word = line.strip()
    word = upper_word.lower()
    list.append(word)

weekly_word = random.choice(list)

first_letter = weekly_word[0]
website = "https://lifeprint.com/asl101/pages-signs/" + first_letter + "/" + weekly_word + ".htm"

intro = "Hello and Welcome to Weekly ASL Learning!\nThis week's word will be: " + weekly_word 
link = "\nLearn it here with our good ol' Bill Vicars: " + website
outro = "\n\nHave a great week!\n--Ambo"
body = intro + link + outro

# assign key email aspects to variables for easier future editing
subject = "Learn ASL!"
sender_email = "senderhere@gmail.com"
receiver_email = "receiverhere@gmail.com"
password = "passwordhere" #replace with password
# Create the email head (sender, receiver, and subject)
email = MIMEMultipart()
email["From"] = "Amber Huo"
email["To"] = receiver_email 
email["Subject"] = subject
# Add body and attachment to email
email.attach(MIMEText(body, "plain"))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_email, password) #login with mail_id and password
text = email.as_string()
session.sendmail(sender_email, receiver_email, text)
session.quit()

print('Mail Sent')