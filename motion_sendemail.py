# Sending emails in raspbry pi with Motion
# vahid.mansomi

#!/user/bin/perl  

import smtplib
from datetime import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "user@gmail.com" #adres gmail khod ra be jaye user vared namayid
password = "password"       #password gmail khod ra be jaye password vared namayid
toaddrs  = "vahid.mansomi@gmail.com"  # adres gmail ke ghasd ersal email ra be an darid vared namayid
subject = "test send email"
######################################
# Email object
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddrs
msg['Subject'] = subject

######################################
# Email body
body = 'A motion has been detected.\nTime: %s' % str(datetime.now())
msg.attach(MIMEText(body, 'plain'))

######################################
# Connecting to SMTP server and sending the email
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect("smtp.gmail.com", 587)
smtp.starttls()
smtp.login(fromaddr, password)
text = msg.as_string()
smtp.sendmail(fromaddr, toaddrs, text)
smtp.quit()
#######################################
# Output
print "Message length is " + repr(len(msg))
print text

