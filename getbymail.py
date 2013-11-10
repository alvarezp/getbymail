#!/usr/bin/env python2.7
######################################
# getbymail.py
#
# Author: Cadaver (cadaver@cadaver.me)
# Version: 20131109
# License: GNU GPL
#
#
######################################


import imaplib
import email
from email import Encoders
import urllib
import sys
import zipfile
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText

mailaccount = 'cron@gmail.com'
validsender = 'user@gmail.com>'
password = 'cronpasswd'
imapserver = imapserver  # 'imap.gmail.com'
smtpserver = smtpserver  # 'smtp.gmail.com:587'


def printmessage(fullmessage):
        mailmessage = email.message_from_string(fullmessage[0][1])
        print mailmessage['From'].split('<')[1]
        if mailmessage['From'].split('<')[1] == validsender:
            print 'Valid sender, following instructions:'
            print 'Full command', mailmessage['Subject']
            command = mailmessage['Subject'].split()[0]
            if command == 'downloadfile':
                target = mailmessage['Subject'].split()[1]
                print "Downloading file", target
                urllib.urlretrieve(target, target.split('/')[-1])
                zipfilename = target.split('/')[-1] + ".zip"
                zipf = zipfile.ZipFile(zipfilename, "w")
                zipf.write(target.split('/')[-1])
                zipf.close()
                os.remove(target.split('/')[-1])
            elif command == 'downloadpage':
                target = mailmessage['Subject'].split()[1]
                print "Downloading page", target
                targetfile = target.split('/')[-1] + '.html'
                urllib.urlretrieve(target, targetfile)
                zipfilename = target.split('/')[-1] + ".zip"
                zipf = zipfile.ZipFile(zipfilename, "w")
                zipf.write(targetfile)
                zipf.close()
                os.remove(targetfile)
            elif command == 'downloadsite':
                target = mailmessage['Subject'].split()[1]
                print "Downloading site", target
            elif command == 'shutdown':
                target = mailmessage['Subject'].split()[1]
                os.system('poweroff')
                print "Shutting down"
            elif command == "help":
                print "Sending help"
            else:
                print "invalid command"
                print command
                sys.exit()
        else:
            print 'Invalid sender, ignoring message'
            sys.exit()
        return zipfilename


def createmail(attachmentf):
        msg = MIMEMultipart()
        msg['From'] = mailaccount
        msg['To'] = validsender
        msg['Subject'] = attachmentf
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attachmentf, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment;\
         filename="%s"' % attachmentf)
        msg.attach(part)
#        msg.attach(MIMEText(file(attachmentf).read()))
        return msg


def sendmsg(msg):
        smtpserverc = smtplib.SMTP(smtpserver)
        smtpserverc.ehlo()
        smtpserverc.starttls()
        smtpserverc.ehlo()
        smtpserverc.login(mailaccount, password)
        smtpserverc.sendmail(mailaccount, validsender, msg.as_string())
        smtpserverc.close()

mail = imaplib.IMAP4_SSL(imapserver)
mail.login(mailaccount, password)
mail.select("inbox")
result, unreadmessages = mail.uid('search', None, 'UnSeen')
if unreadmessages == ['']:
    print "No messages"
    sys.exit(0)
cleanid = unreadmessages[0].split()[0]
lum = cleanid
result1, message = mail.uid('fetch', lum, "(RFC822)")
zipfilename = printmessage(message)
msg = createmail(zipfilename)
sendmsg(msg)
