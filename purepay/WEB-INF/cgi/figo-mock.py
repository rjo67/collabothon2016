#!/usr/bin/env python -u

def green(text):
    return "<font color=\"green\">{}</font>".format(text)

def red(text):
    return "<font color=\"red\">{}</font>".format(text)

def p(text):
    return "<p class=sansserif>{}</p>".format(text)

def input(text):
    return p(green(text))

def output(text):
    return p(red("&nbsp;&nbsp;&nbsp;&nbsp;"+text))

def main():
    print ("Content-type: text/html\n\n")

    print ("<style> p.sansserif { font-family: Courier, Helvetica, sans-serif; } </style>")

    print (input("creating payment ..."))
    print (output("payment P1725045.57 created"))

    print (input("submitting payment"))
    print (output("task_token: YD7UD2s_Jh51W4-qmGT3b6AYnEymoa4XJlXZZQ1NyTJczrgbsD8sv2C-ueHpg9hCP5oaHzlyL3BpEH-WIVvBp8WmtcN1AMdI5G0poroK8uak"))
    print (output("Connecting to server "))
    print (output("... processing ... "))
    print (input("success"))


if __name__ == "__main__":
    main()
