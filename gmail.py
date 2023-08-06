import smtplib
from email.message import EmailMessage


def email_alert(dist,angle):
    body="Distance="+str(dist)+"\n"+"Angle="+str(angle)
    msg=EmailMessage()

    msg.set_content(body)

    msg['subject']="ALERT:UAV Detected"
    msg['to']=""
    

    user =""
    password=""
    msg['from']=user

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()

#email_alert(56,10)


