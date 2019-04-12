import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def mysql_connect(dbhost,dbuser='root',dbpasswd='',dbname='pass_dict'):
    conn = mysql.connector.connect(
    host=dbhost,
    user=dbuser,
    passwd=dbpasswd,
    database=dbname
    )
    return conn

def start_session(conn, id, host, username):
    csr = conn.cursor()
    sql = "INSERT INTO sessions (id,host,username) VALUES (%s, %s, %s)"
    val = (id, host, username)
    csr.execute(sql, val)
    conn.commit()
    if(csr.rowcount == 1):
        csr.close()
        return True
    csr.close()
    return False

def get_password(conn):
    # Make sure we are in transaction mode
    conn.autocommit(False)
    csr = conn.cursor()
    try:
        # Get a password
        csr.execute("SELECT id,pass FROM passwords WHERE used = 0 ORDER BY RAND() LIMIT 1")
        res = csr.fetchone()
        # Now update the value to show pass is used
        sql = "UPDATE passwords SET used = 1 WHERE id = %s"
        val = (res[0])
        csr.execute(sql, val)
        conn.commit()
        csr.close()
        return res[1]
    except mysql.connector.Error:
        conn.rollback()
    csr.close()
    return None

def password_found(conn, id, password):
    csr = conn.cursor()
    sql = "UPDATE sessions SET found = 1, password = %s WHERE id = %s"
    val = (password, id)
    csr.execute(sql, val)
    conn.commit()
    if(csr.rowcount == 1):
        csr.close()
        return True
    csr.close()
    return False

def is_session_running(conn, id):
    csr = conn.cursor()
    sql = "SELECT found FROM sessions WHERE id = %s"
    val = (id)
    csr.execute(sql, val)
    res = csr.fetchone()
    if res[0] == 1:
        csr.close()
        return False
    csr.close()
    return True

def close_connection(conn):
    if(conn.is_connected()):
        conn.close()
