import smtplib
import tkinter


gmail_password=''
gmail_username=''


def callback():
    gmail_password = password.get()
    print(gmail_password)
    gmail_username = username.get()
    print(gmail_username)
    return gmail_password, gmail_username


sent_from = 'maciekgt54@gmail.com'
to = 'maciekgt540@gmail.com'
subject = 'test message fron pyth"n'
body = 'test msg from pthn'

email_text = '''
From: %s
To: %s
Subject: %s

%s
''' % (sent_from, to, subject, body)

body = tkinter.Tk()
body.title("Login")


try:
    canvas1 = tkinter.Canvas(width=400, height=300)
    canvas1.pack()

#    gmail_user = input('Gmail User')
#   print(gmail_user)
#    gmail_password = input('Gmail Password')
#    print(gmail_password)

    username = tkinter.Entry(body, bd=5, width=40)
    username.pack()

    password = tkinter.Entry(body, bd=5, width=40, show='x')
    password.pack()
    b = tkinter.Button(body, text='OK', command=callback)
    b.pack()

    body.mainloop()

#    while password.find('\\') is True:
#        password.replace('\\\\')
#        print(gmail_password)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(gmail_username, gmail_password)
    server.sendmail(sent_from, to, email_text)
#   server.sendmail('maciekgt54@gmail.com')
    server.close()
    print("Email sent")

except:
    print("Something went wrong!")



