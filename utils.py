#
#  Copyright (C) 2019 by
#  Divyansh Gupta, Harry Karwasra, Nandana Varshney, Nikhil Ramakrishnan
#
#  This project is licensed under the MIT License

import hashlib
import os
import struct
import time

logo = r'''
___________                             __________                __          
\__    ___/___   ____   ________________\______   \_______ __ ___/  |_  ____  
  |    |_/ __ \ /    \ /  ___/  _ \_  __ \    |  _/\_  __ \  |  \   __\/ __ \ 
  |    |\  ___/|   |  \\___ (  <_> )  | \/    |   \ |  | \/  |  /|  | \  ___/ 
  |____| \___  >___|  /____  >____/|__|  |______  / |__|  |____/ |__|  \___  >
             \/     \/     \/                   \/                         \/ 
'''

options = '''\
Select an option:
    1. Start a new session (do this on the first terminal)
    2. Join another session (do this to add another terminal to the party)
    3. Clear existing session(s).
    4. Modify database settings.

Your choice? \
'''

b = u"\u2022"
bullet = '\t[' + b + ']\t'

connect_db = "Establishing connection to database..."
session = "Setting up session for the host"
start_att = "Starting attack"
resume_att = "Resuming distributed attack"
clean_msg = "Clearing sessions"
no_sess = "I don't see any running sessions... Try creating a new one."
db_update_text = "Details updated. This will be vaild only for this" + \
                 "session. Update data in SQL.py to make permanent."

def gen_id():
    seed = str(struct.unpack('I', os.urandom(4)))
    t = str(time.time())
    txt = seed+t
    hash_object = str(hashlib.sha256(txt.encode('utf-8')).hexdigest())
    return hash_object[:8]

def get_logo():
    global logo
    return logo

def show_ops():
    global options
    return options

def attack_start():
    return bullet + start_att
def attack_resume(host,username):
    return bullet + resume_att + " for user '" + username + \
      "' on FTP host '" + host + "'"
def progress_start():
  return bullet + "Working..."
def db_connect():
    return bullet + connect_db
def sess_setup():
    return bullet + session
def clean_message():
    return bullet + clean_msg
def no_session():
    return bullet + no_sess
def status_update(passwd):
    return bullet + "Update: Last password tried was '" + passwd + \
                    "'. Working..."
def found_pass(host,username,passwd):
    st = bullet + "Password for user '" + username + "' on FTP host '" + \
         host + "' is '" + passwd + "'."
    return st
