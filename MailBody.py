import tkinter

body = tkinter.Tk(screenName='Input Password', baseName='Input Password')


email_password = tkinter.Entry(body, bd=3, width=40, show="x")
email_password.pack()

body.mainloop()
body.destroy()
