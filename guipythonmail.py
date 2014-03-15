#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import smtplib
import Tkinter
############################
#     First GUI project    #
#   Created by KradLogan   #
############################
 
def sendit():
	fromwho = sentry.get()
	towho = rentry.get()
	subject = subentry.get()
	body = btext.get("0.0",END)
	mymessage = "FROM: %s \nTO: %s\nMIME-Version: 1.0\nContent-type: text/html \nSUBJECT: %s\n%s" %(fromwho, towho, subject, body)
	try:
		#CHANGE THIS 'you.smptserver.net' to your smtp server address
		s = smtplib.SMTP('you.smtpserver.net', 25)
		s.sendmail(fromwho, towho, mymessage)
		s.quit()
		tkMessageBox.showinfo("Sent", "Your Email has been sent.")
		top.destroy()
	except:
		tkMessageBox.showinfo("Failed", "Email Failed to Send.")


top = Tkinter.Tk()
#This is the header title
top.wm_title("GUIPython Simple Mail Sender")
frame = Frame(top, height=430, width=420)
frame.pack()
#Entry for sender
slabel = Label(frame, text = "From: ")
sentry = Entry(frame, bd = 2)
#Entry for reciever
rlabel = Label(frame, text = "To: ")
rentry = Entry(frame, bd = 2)
#Entry for Subject
sublabel = Label(frame, text = "Subject: ")
subentry = Entry(frame)
#Multiline entry for Body
blabel = Label(frame, text = "Body: ")
btext = Text(frame, state=NORMAL, height= 10, width= 20)
#Attachment
#Send button
send = Button(frame, text="Send", command=sendit)
#Reset Button
#Exit Button
exit = Button(frame, text="Exit", command=lambda: top.destroy())

#Setting up the placement of everything.
#From
slabel.pack()
slabel.place(height=20, anchor=NW, x=10, y=10)
sentry.pack()
sentry.place(bordermode=OUTSIDE, height = 30, width= 400, y=30, x =10)
#TO
rlabel.pack()
rlabel.place(bordermode=OUTSIDE, height=20, y=60, x=10)
rentry.pack()
rentry.place(bordermode=OUTSIDE, height = 30, width= 400, y=80, x=10)
#Subject
sublabel.pack()
sublabel.place(bordermode=OUTSIDE, height=20, y=110, x=10)
subentry.pack()
subentry.place(bordermode=OUTSIDE, height=30, width=400, y=130, x=10)
#body
blabel.pack()
blabel.place(bordermode=OUTSIDE, height=20, y=160, x=10)
btext.pack()
btext.place(bordermode=OUTSIDE, height = 200, width= 400, y=180, x=10)
#send Button
send.pack()
send.place(bordermode=OUTSIDE, height = 40, width= 50, y=380, x=175)
#Exit button
exit.pack()
exit.place(bordermode=OUTSIDE, height = 40, width= 50, y=380, x =225)
top.mainloop()
