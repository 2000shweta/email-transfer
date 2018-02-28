import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.login("shwetakumari152000@gmail.com","password")
messg= "Hello manisha!"
s.sendmail("shwetakumari152000@gmail.com","manishakatiyar1111@gmail.com",messg)
s.quit()
