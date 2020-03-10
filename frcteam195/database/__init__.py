import mysql.connector as mariadb
import json
import logging
import datetime
import sys

DEFAULT_CONFIG_FILE = "frcteam195_database.json"

def connect(config_file = None):
    conn = None
    if None == config_file:
        config_file = DEFAULT_CONFIG_FILE
    try:
        with open(config_file) as f:
            config = json.loads(f.read())
            item = config['config']
            logging.info(str(datetime.datetime.now()) + " Using database {0} on {1}".format(item['database'], item['host']))

            conn = mariadb.connect(user=item['user'],
                               passwd=item['cred'],
                               host=item['host'],
                               database=item['database'])
    except OSError as err:
        print("OS error: {0}".format(err))
        logging.error(str(datetime.datetime.now()) + " OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
        logging.error(str(datetime.datetime.now()) + " Could not convert data to an integer")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        logging.error(str(datetime.datetime.now()) + " Unexpected error: {0}".format(sys.exec_info()[0]))
        raise

    return conn
