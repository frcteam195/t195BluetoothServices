from frcteam195.database import sqlcmd
import datetime


def put():
    datime = int(datetime.datetime.timestamp(datetime.datetime.now()))
    sqlcmd.put("UPDATE TimeCode SET LastUpdate = {}".format(datime))


def get():
    results = sqlcmd.get("SELECT LastUpdate FROM TimeCode")
    return results