from frcteam195.database import connect
import logging
import datetime
import sys


def get(cmd):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(cmd)
        columns = [column[0] for column in cursor.description]
        results = None
        for row in cursor.fetchall():
            results = dict(zip(columns, row))
        conn.close()
        return results
    except:
        if conn:
            conn.close()
        logging.error("Unexpected error: %s".format(sys.exc_info()[0]))
    pass


def get_list(cmd):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(cmd)
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        conn.close()
        return results
    except:
        if conn:
            conn.close()
        logging.error("Unexpected error: %s".format(sys.exc_info()[0]))
        pass


def put(cmd):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(cmd)
        conn.commit()
        if cursor.rowcount < 1:
            conn.close()
            logging.error(str(datetime.datetime.now()) + " No records were updated: cmd={0}".format(cmd))
            return ("failure")
        else:
            conn.close()
            logging.error(str(datetime.datetime.now()) + " {0} record(s) updated".format(cursor.rowcount))
            return ("success")
    except:
        if conn:
            conn.close()
        logging.error("Unexpected error: %s".format(sys.exc_info()[0]))
        pass
