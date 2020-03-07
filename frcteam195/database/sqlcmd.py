from frcteam195.database import connect
import logging
import datetime
import sys
from mysql.connector import Error as MySQLError


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
    except MySQLError as merr:
        logging.info(str(datetime.datetime.now()) + " Unexpected error occurred {0}".format(merr))
        pass
    except:
        logging.info(str(datetime.datetime.now()) + " Unexpected error occurred {0}".format(sys.exc_info()[0]))
        pass
    finally:
        if conn:
            conn.close()


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
    except MySQLError as merr:
        logging.info(str(datetime.datetime.now()) + " Unexpected error occurred {0}".format(merr))
        pass
    except:
        logging.info(str(datetime.datetime.now()) + " Unexpected error occurred {0}".format(sys.exc_info()[0]))
        pass
    finally:
        if conn:
            conn.close()


def put(cmd):
    logging.debug(str(datetime.datetime.now()) + " No records were updated: cmd={0}".format(cmd))
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
    except MySQLError as merr:
        logging.info(str(datetime.datetime.now()) + " Unexpected error occurred {0}".format(merr))
        pass
    except:
        logging.info(str(datetime.datetime.now()) + " Unexpected error occurred {0}".format(sys.exc_info()[0]))
        pass
    finally:
        if conn:
            conn.close()
