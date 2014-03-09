#!/usr/bin/python

import smtplib

sender=raw_input('FROM email address: ')
receivers=raw_input('TO email address: ')
print "Simple Email Sender"
fromwho=raw_input('FROM: ')
towho=raw_input('TO: ')
subject=raw_input('Subject: ')
#Body can use HTML tags.
body=raw_input('Body: ')

mymessage = "FROM: %s \nTO: %s\nMIME-Version: 1.0\nContent-type: text/html \nSUBJECT: %s\n%s" %(fromwho, towho, subject, body)

print mymessage
s = smtplib.SMTP('KradsKaliBox.kradskalibox.net', 25)
s.sendmail(sender, receivers, mymessage)
s.quit()
