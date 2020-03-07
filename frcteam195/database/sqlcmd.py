from frcteam195.database import connect
import logging
import datetime


def get(cmd):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(cmd)
    columns = [column[0] for column in cursor.description]
    results = None
    for row in cursor.fetchall():
        results = dict(zip(columns, row))
    conn.close()
    return results

def get_list(cmd):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(cmd)
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    conn.close()
    return results

def put(cmd):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(cmd)
    conn.commit()
    if cursor.rowcount < 1:
        conn.close()
        logging.error(str(datetime.datetime.now()) + " No records were updated: cmd={0}".format(cmd))
        return("failure")
    else:
        conn.close()
        logging.error(str(datetime.datetime.now()) + " {0} record(s) updated".format(cursor.rowcount))
        return("success")

