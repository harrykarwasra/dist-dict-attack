#
#  Copyright (C) 2019 by
#  Divyansh Gupta, Harry Karwasra, Nandana Varshney, Nikhil Ramakrishnan
#
#  This project is licensed under the MIT License

from scapy.all import *
import re


logo = r'''
___________                             __________                __          
\__    ___/___   ____   ________________\______   \_______ __ ___/  |_  ____  
  |    |_/ __ \ /    \ /  ___/  _ \_  __ \    |  _/\_  __ \  |  \   __\/ __ \ 
  |    |\  ___/|   |  \\___ (  <_> )  | \/    |   \ |  | \/  |  /|  | \  ___/ 
  |____| \___  >___|  /____  >____/|__|  |______  / |__|  |____/ |__|  \___  >
             \/     \/     \/                   \/                         \/ 
'''
welcome_text = '''
                    Welcome to TensorBrute Attack Analyzer.
'''
report_text = '''\
----------------------------TBAA Analysis Report-----------------------------\
'''
endline = '''\
-----------------------------------------------------------------------------\
'''
count = 0

attempts = {}
user_att = {}
seqs = []
anomalies = []

users = set()

single_threshold = 5
terminal_threshold = 3

class anomaly:
    def __init__(self,username,attempts):
        self.username = username
        self.attempts = attempts

class session:
    def __init__(self,ip,ack,username):
        self.ip = ip
        self.ack = ack
        self.username = username[:-5]
        self.ack331 = None
        self.ackpass = None

    def add331(self,ack):
        self.ack331 = ack

    def addpass(self,ack):
        self.ackpass = ack

def is_ftp(pkt):
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        if pkt[TCP].dport == 21 or pkt[TCP].sport == 21:
            return True
    return False

def checkAttempt(seq,ip):
    '''Detect posible anomaly in attempts'''
    threshold = 5

    global anomalies,user_att
    if seq.username in user_att:
        count = user_att[seq.username]
        if count > threshold:
            an = anomaly(seq.username,count)
            anomalies.append(an)
 


def ftp_scan(pkt):
    global seqs,attempts,user_att,users
    data = pkt[Raw].load
    data = str(data)

    if 'USER ' in data:
        username = data.split('USER ')[1].strip()
        sess = session(pkt.src,pkt.ack,username)
        seqs.append(sess)

    elif '331 ' in data:
        for seq in seqs:
            if pkt.seq == seq.ack:
                seq.add331(pkt.ack)
                break

    elif 'PASS ' in data:
        for seq in seqs:
            if pkt.seq == seq.ack331:
                seq.addpass(pkt.ack)
                break

    elif '530 ' in data:
        for i in range(len(seqs)):
            seq = seqs[i]
            if pkt.seq == seq.ackpass:
                ip = pkt[IP].dst

                if seq.username in attempts:
                    data = attempts[seq.username]
                    if ip in data:
                        data[ip] += 1
                    else:
                        data[ip] = 1
                else:
                    data = {}
                    data[ip] = 1
                    attempts[seq.username] = data

                if seq.username in user_att:
                    user_att[seq.username]+=1
                else:
                    user_att[seq.username]=1
                users.add(seq.username)
                del seqs[i]
                break

    elif '230 ' in data:
        for i in range(len(seqs)):
            seq = seqs[i]
            if pkt.seq == seq.ackpass:
                ip = pkt[IP].src
                checkAttempt(seq,ip)
                del seqs[i]
                break


def method_filter_HTTP(pkt):
    global count
    if is_ftp(pkt):
        count+=1
        ftp_scan(pkt)
    else:
        return




sniff(offline="test.pcap",prn=method_filter_HTTP, store=0)

print(logo)

print(welcome_text)
print(report_text)
print(count,"FTP packets in total.\n")
print("Confirmend Breach Report:")
if len(anomalies)==0:
    print("No confirmed breaches found.")
for an in anomalies:
    print("\tUser account: ", an.username)
    print("\tNumber of failed attempts before successful attempt: ",an.attempts)

print("\nAttempted Attacks Report:")
if len(attempts)==0:
    print("No attempted breaches found.")


for user,data in attempts.items():
    multi_attack = False
    single_attack = False
    attack_ip = None

    # count number of single attacks
    single_count = 0

    for ip,tries in data.items():
        if tries > single_threshold:
            single_attack = True
            attack_ip = ip
            single_count += 1

    if single_count > 1:
        multi_attack = True

    print("\n\n\tUSER:",user)
    if not (multi_attack or single_attack):
        print("\tNo suspected attacks.")
    elif multi_attack:
        print("\tSuspected distributed attack from the following IPs:")
        print("\n\tIP\t\tAttempts\n")
        for ip,count in data.items():
            print("\t",ip,"\t",count,sep='')
    elif single_attack:
        print("\tSuspected single source attack from IP",attack_ip)

print(endline)
