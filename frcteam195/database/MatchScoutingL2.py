from frcteam195.database import sqlcmd


def get(event_id=None):
    cmd = "SELECT a.*, b.MatchNo MatchNo FROM MatchScoutingL2 a, Matches b " \
          "WHERE a.EventID = {} and a.MatchID = b.MatchID " \
          "ORDER BY MatchNo".format(event_id)
    results = sqlcmd.get_list(cmd)
    return results

def put(key_val, payload):
    cmd_skeleton = 'UPDATE MatchScoutingL2 SET {} {}'
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