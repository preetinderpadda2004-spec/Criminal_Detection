import pymysql
import re

def Connect():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='system',
        database='criminal_detection'
    )
    return conn

def email_valid(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(pattern, email) is None:
        return False
    else:
        return True

def mobile_valid(mobile):
    if mobile.isdigit() and len(mobile)==10:
        return True
    else:
        return False

