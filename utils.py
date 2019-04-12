import os
import struct
import time
import hashlib

logo = '''\
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

Your choice? \
'''

def gen_id():
    seed = str(struct.unpack('I', os.urandom(4)))
    t = str(time.time())
    txt = seed+t
    hash_object = hashlib.sha256(txt.encode('utf-8')).hexdigest()
    return hash_object[:8]

def get_logo():
    global logo
    return logo

def show_ops():
    global options
    return options
    