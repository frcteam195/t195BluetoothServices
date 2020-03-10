from frcteam195.database import connect
import logging
import datetime
from mysql.connector import Error as MySQLError
import sys


def Main():
    datime = datetime.datetime.timestamp(datetime.datetime.now())
    cmd = "UPDATE time_code SET last_update = {}".format(datime)
    conn = None
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


if __name__ == '__main__':
    Main()
