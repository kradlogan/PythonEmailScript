#!/usr/bin/python

import smtplib

sender=raw_input('Enter Sender email: ')
receivers=raw_input('Address email is being sent to: ')

fromwho=raw_input('Name of person its sent from: ')
towho=raw_input('Name of the person recieving this: ')
subject=raw_input('Subject: ')
body=raw_input('Body: ')

mymessage = "FROM: %s \nTO: %s\nMIME-Version: 1.0\nContent-type: text/html \nSUBJECT: %s\n%s" %(fromwho, towho, subject, body)

print mymessage
s = smtplib.SMTP('KradsKaliBox.kradskalibox.net', 25)
s.sendmail(sender, receivers, mymessage)
s.quit()
