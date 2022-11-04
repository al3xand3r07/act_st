import smtplib
from email.mime.text import MIMEText
import getpass


def sendMail(user,pwd,to,subject,text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        smtpServer.ehlo()
        smtpServer.starttls()
        smtpServer.ehlo()
        smtpServer.login(user, pwd)
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
    except Exception as err:
        print("[-] Sending Mail Failed."+str(err))

user = 'yosafataguirrehernandez3773@gmail.com'
pwd = getpass.getpass()
msg = """
    Hola...!!!
    
    Es un gusto volverte a saludar.
    Este es un correo de prueba de la practica 8
    
    Saludos"""
asunto = 'Re: Important'
receiver = 'yosafat.aguirrehrnd@uanl.edu.mx'
sendMail(user, pwd, receiver,
         asunto, msg)