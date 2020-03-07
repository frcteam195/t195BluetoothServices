from frcteam195.database import sqlcmd


def get(eventId):
    results = sqlcmd.get_list("SELECT a.AllianceStationID AllianceStationID, b.* FROM MatchScouting a, WordCloud b " \
                   "WHERE a.EventID = {} and a.MatchID = b.MatchID ORDER BY MatchID, AllianceStationID".format(eventId))
    return results

def put(payload):
    cmd_skeleton = 'INSERT INTO WordID ({}) VALUES ({})'
    col_list = []
    val_list = []
    for k,v in payload.items():
        if isinstance(v, __builtins__.str):
            val_list.append("'{}'".format(v))
        else:
            val_list.append("{}".format(v))
        col_list.append(k)
    col_str = ','.join(col_list)
    val_str = ','.join(val_list)
    cmd = cmd_skeleton.format(col_str, val_str)
    return sqlcmd.put(cmd)
