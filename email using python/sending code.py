import smtplib 
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("example@gmail.com", "password")
server.sendmail("example@gmail.com",
                 "concept1@gmail.com",
                 "hello, how are you?")
server.quit()
