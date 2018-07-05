import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMail():

	#From & To emails
	frmAddr = "tklaasee@gmail.com"
	toAddr = "tklaasee@gmail.com"
	#message
	msg = MIMEMultipart()
	
	msg['From']	 = frmAddr
	msg['To'] = toAddr
	msg['Subject'] = "Intruder Detected"
	
	body = "The following intruder was detected in your home."
	
	msg.attach(MIMEText(body, 'plain'))
	
	filename = "Intruder.jpg"
	attachment = open("Intruders/Intruder.jpg", "rb")
	
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attatchment; filename= %s" % filename)
	
	msg.attach(part)
	password = input('Enter your password: ')
	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com',  465)
		server.login(frmAddr, password)
		text = msg.as_string()
		server.sendmail(frmAddr, toAddr, text)
		server.close()
		print ('successfully sent mail')
	except:
		print ('failed to send mail')
