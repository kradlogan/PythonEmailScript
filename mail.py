#!/usr/bin/python

import smtplib

sender = 'from@fromdomain.com'
receivers = ['reciever@recieve.net']

message = """From: James Frank <jamesfrank@crazyppl.org>
To: To Person <reciever@recieve.net>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP email test

This is the body.
"""

s = smtplib.SMTP('your.smtpserver.net', 25)
s.sendmail(sender, receivers, message)
s.quit()
