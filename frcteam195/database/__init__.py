import mysql.connector as mariadb
import json

DEFAULT_CONFIG_FILE = "frcteam195_database.json"

def connect(config_file = None):
    if None == config_file:
        config_file = DEFAULT_CONFIG_FILE
    try:
        f = open(config_file)
        config = json.loads(f.read())

        item = config['config']

        conn = mariadb.connect(user=item['user'],
                               passwd=item['cred'],
                               host=item['host'],
                               database=item['database'])
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    return conn
