from frcteam195.database import sqlcmd
import datetime
import json


def put():
    datime = int(datetime.datetime.timestamp(datetime.datetime.now()))
    sqlcmd.put("UPDATE TimeCode SET LastUpdate = {}".format(datime))


def get():
    ret = 0;
    results = sqlcmd.get("SELECT LastUpdate FROM TimeCode")
    if "LastUpdate" in results:
        ret = int(results['LastUpdate'])
    return ret