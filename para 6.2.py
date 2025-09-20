from ftplib import error_reply

try:
    print("start code")
    print(10/0)
    print("No error")
except NameError:
    print("we have a NemeError")
except ZeroDivisionError:
   print("we have 0divError ")

print("code after")
