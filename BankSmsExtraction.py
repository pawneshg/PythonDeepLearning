# -*- coding: utf-8 -*-
"""
Created on Sun Jun 03 21:11:54 2018

@author: admin
"""

"""
Ele sms data extraction 
"""
import json
import re


filename   =  "DataSets/sms_data.js"
jsonfile   =  "DataSets/sms_data_ext.txt"
resultfile =  "DataSets/Extracted_smsData.txt"

'''
(?!.*cake\.(?:milk|butter)) this is a negative lookahead, this will prevent matching if the string contains one of words you don't allow
'''

#regex for check bank message
RdetectMsg = re.compile(r"(?=.*[Aa]ccount.*|.*[Aa]/[Cc].*|.*[Aa][Cc][Cc][Tt].*|.*[Cc][Aa][Rr][Dd].*)(?=.*[Cc][Rr][Ee][Dd][Ii][Tt].*|.*[Cc][Rr][Ee][Dd][Ii][Tt]ed.*|.*[Dd]ebit*.*|.*[Dd]ebited*.*|.*deposited.*|.*withdrawn.*|.*spent.*)(?=.*[Ii][Nn][Rr].*|.*[Rr][Ss].*)")
#RdetectMsg = re.compile(r"(.*[Aa]ccount.*|.*[Aa]/[Cc].*|.*[Aa][Cc][Cc][Tt].*|.*[Cc][Aa][Rr][Dd].*)(.*[Cc]redit.*|.*[Dd][eE][Bb][Ii][Tt].*)(.*[Ii][Nn][Rr].*|.*[Rr][Ss].*)")

#regex for cardNo
#[0-9]*[Xx\*]*[0-9]*[Xx\*]+[0-9]{3,}
RcardNo = re.compile(r"([0-9]*[Xx\*]*[0-9]*[Xx\*]+[\s]*[0-9]{3,})|([Ee][Nn][Dd][Ii][Nn][Gg]\s[0-9]{3,})|([Aa]\/[Cc]\s[0-9\*-]{3,})")

#regex for amount
Ramount = re.compile(r"([Ii][Nn][Rr][\s]*[0-9\.,]+|[Rr][Ss][\.]*[\s]*[0-9\.,]+)")

#regex for tranxTime
RtranxTime = re.compile(r"([Oo][nN]\s[0-9-A-Z:/]+|Val\s[0-9A-Z-]+|[Oo][nN]\s[0-9A-Z-/]+)")

#regex for NonbankMsg
RNonbankMsg = re.compile(r"(.* wallet|Stmt|FREECHARGE|beneficiary|statement|Reward .*)")


with open(filename, 'r') as fp:
    data = fp.readlines()
    data[0] = "".join(x for x in data[0].partition("{")[1:])
with open(jsonfile, 'w') as fp:
    fp.writelines(data)
with open(jsonfile, "r") as fp:
    jsonData = json.loads(fp.read())
print jsonData.keys()

def isBankSms(msg):
    results = RdetectMsg.findall(msg)
    #global cnt 
    if results:
        return True
    else:
        return False

def RemoveNonBankMsg(msg):
    results = RNonbankMsg.findall(msg)
    if results:
        return True
    else:
        return False
    


with open(resultfile, 'w') as fp:
    fp.write('{a: ^2}{b: ^28}{c: ^28}{d: ^28}{e: ^28}{f: ^28}\n' \
             .format(a= 'S.No.', b = 'Sender ID/Number', c = 'Credit/Debit ', d = 'Amount', e = 'Tranx dateTime', f = 'Sms Received Time'))
        
    print len(jsonData["messages"])
    cnt = 0
    for ind, record in enumerate(jsonData["messages"]):
        index = None
        number = None #Done
        cardNo = None #Done
        amount = None #Done
        tranxTime = None #Done
        SmsTime = None #Done
        
        if isBankSms(record["text"]) and not RemoveNonBankMsg(record["text"]):
            cnt+=1
            index = cnt
            number = record["number"].split('-')[-1]
            cardNo = RcardNo.findall(record["text"])[0]
            cardNo = cardNo[0][-4:] or cardNo[1][-4:] or cardNo[2][-4:]
            amount = Ramount.findall(record["text"])
            amount = amount[0][3:].strip() if len(amount) > 0 else '-'
            SmsTime = record["datetime"]
            tranxTime = RtranxTime.findall(record["text"])
            tranxTime = tranxTime[0][3:].strip() if len(tranxTime) >0 else '-'
            fp.write('{a: ^2}{b: ^28}{c: ^28}{d: ^28}{e: ^28}{f: ^28}\n' \
             .format(a= index, b = number, c = cardNo, d = amount, e = tranxTime, f = SmsTime))


        
    
    