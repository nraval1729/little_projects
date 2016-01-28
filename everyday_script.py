#!/usr/bin/python

import sqlite3
import datetime
import smtplib

def send_email(sender, passwd, receiver, subject, body):

    gmail_sender = sender
    gmail_passwd = passwd
    FROM = sender
    TO = receiver if type(receiver) is list else [receiver]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)
        server.sendmail(FROM, TO, message)
        server.close()
        # print 'Successfully sent the mail'
    except:
        print "Failed to send mail"


def main():
	todays_date = datetime.date.today().strftime("%d/%m")        #in the format of dd/mm as per indian convention to make it easy for baa

	# todays_date = '06/10'

	todays_date_tuple = (todays_date + '%', ) #added % so that the year becomes irrelevant

	conn = sqlite3.connect('info.db')

	cursor = conn.cursor()

	cursor.execute("SELECT * FROM contact_info WHERE Birth_Date LIKE ?", todays_date_tuple)

	birthday_block = "The following people have birthdays today:\n\n"
	
	for row_index, row in enumerate(cursor):
		for attribute in row:
			birthday_block += attribute
			birthday_block += ", "
		birthday_block += '\n'
	birthday_block += '\n'

	cursor.execute("SELECT * FROM contact_info WHERE Anniversary_Date LIKE ?", todays_date_tuple)

	anniversary_block = "The following people have anniversaries today:\n\n"

	for row_index, row in enumerate(cursor):
		for attribute in row:
			anniversary_block += attribute
			anniversary_block += ", "
		anniversary_block += '\n'
	anniversary_block += '\n'

	conn.commit()

	sender = 'foo@foobar.com'
	passwd = 'FoOBAr'
	receivers = ['foo@foobar.com', 'foobar@foobar.com', 'barfoo@foobar.com']
	body = birthday_block + anniversary_block
	subject = "Your daily birthday/anniversary reminder!"

	send_email(sender, passwd, receivers, subject, body)

	conn.close()

if __name__ == "__main__":
	main()
