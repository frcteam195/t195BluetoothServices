from frcteam195.database import sqlcmd


def get(event_id=None, allianceStationId=None):
    if allianceStationId is not None:
        cmd = """SELECT a.*, b.MatchNo MatchNo FROM MatchScouting a, Matches b
                         WHERE a.EventID = {} AND a.MatchID = b.MatchID AND AllianceStationID = {}
                         ORDER BY MatchNo, AllianceStationID""".format(event_id, allianceStationId)
    else:
        cmd = """SELECT a.*, b.MatchNo MatchNo FROM MatchScouting a, Matches b
                         WHERE a.EventID = {} and a.MatchID = b.MatchID
                         ORDER BY MatchNo, AllianceStationID""".format(event_id)    
    results = sqlcmd.get_list(cmd)
    return results

def put(key_val, payload):
    cmd_skeleton = 'UPDATE MatchScouting SET {} {}'
    set_fmt = "{} = {}"
    where_clause = ' WHERE MatchScoutingID = {}'.format(key_val)
    setlist = []
    for k,v in payload.items():
        if isinstance(v, str):
            s = set_fmt.format(k, "'{}'".format(v))
        else:
            s = set_fmt.format(k,v)
        setlist.append(s)
    set_str = ','.join(setlist)
    cmd = cmd_skeleton.format(set_str, where_clause)
    return sqlcmd.put(cmd)

