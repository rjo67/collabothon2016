#!/usr/bin/env python -u

from figo import FigoSession, FigoConnection, Payment, TaskToken
import json
import time

def printflush(text):
    print (text, flush=True)

def red(text):
    return "<font color=\"red\">{}</font>".format(text)

def green(text):
    return "<font color=\"green\">{}</font>".format(text)

def h1(text):
    return "<h1>{}</h1>".format(text)

def p(text):
    return "<p>{}</p>".format(text)

def h2(text):
    return "<h2>{}</h2>".format(text)

def main():
    printflush ("Content-type: text/html\n\n")

    connection = FigoConnection("CoeBwcCv3itlm2EGTmIRVNpwfV9u1GoD3vZxnVDfhsq8", "S6Tmgm9UQowLonTv8fbZQ_1q4mKqF6jRgF4D0cejuNIM", "http://www.comdirect.de")

    tokens = connection.credential_login("oates1@gmail.com", "figotest")
    access_token = tokens['access_token']

    session = FigoSession(access_token)
    #for account in session.accounts:
    #    print(account.dump(), account.account_id)
    account_id = "A1725045.1"
    acct = session.get_account(account_id)
    #print (acct.dump())

    #print ("using account ", acct.account_id, "supported tans: ", acct.supported_tan_schemes)

    tan_scheme = "M1725045.2"   # should read this from acct.supported_tan_schemes

    payment_req = Payment(session)
    payment_req.account_id = acct.account_id
    payment_req.account_number = "4711951501"
    payment_req.amount = 2.3
    payment_req.bank_code = "20040000"
    payment_req.name = "rjo"
    payment_req.purpose = "PurePay"
    payment_req.type = "Transfer"

    printflush (h1("creating payment ..."))
    payment = session.add_payment(payment_req)
    printflush (p("payment " + payment.payment_id+ " created"))

    printflush (h1(green("submitting payment")))
    state = "myTxnState"
    task = session.submit_payment(payment, tan_scheme, state)
    #print ("task: ", task)
    task_id = task.split('=')[1]
    #print ("task_id: ", task_id)
    task_token = TaskToken('123') # ??
    task_token.task_token = task_id
    printflush (p("got task_token: " + task_token.task_token))
    # wait till server wants a tan response
    stop = False
    while not stop:
        task_state = session.get_task_state(task_token);
        printflush (p(red(task_state.message)))
        if "provide response" in task_state.message:
            stop = True
        else:
            time.sleep(1)
    # resubmit mit TAN
    printflush (h2("submitting TAN"))
    task_state = session.get_task_state(task_token, response='111111');
    #print (task_state)
    printflush (h1(green("success")))


if __name__ == "__main__":
    main()
