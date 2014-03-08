#!/usr/bin/python

import smtplib

sender = 'from@fromdomain.com'
receivers = ['kradlogan@gmail.com']

message = """From: James Frank <jamesfrank@crazyppl.org>
To: To Person <kradlogan@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP email test

This is the body.
"""

s = smtplib.SMTP('KradsKaliBox.kradskalibox.net', 25)
s.sendmail(sender, receivers, message)
s.quit()
