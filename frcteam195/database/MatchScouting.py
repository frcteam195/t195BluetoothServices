from frcteam195.database import sqlcmd


def get(event_id=None):
    cmd = "SELECT a.*, b.MatchNo MatchNo FROM MatchScouting a, Matches b " \
                         "WHERE a.EventID = {} and a.MatchID = b.MatchID " \
                         "ORDER BY MatchID, AllianceStationID".format(event_id)
    results = sqlcmd.get_list(cmd)
    return results

def put(key_val, payload):
    cmd_skeleton = 'UPDATE MatchScouting SET {} {}'
    set_fmt = "{} = {}"
    where_clause = ' WHERE MatchScoutingID = {}'.format(key_val)
    setlist = []
    set_str = ''
    for k,v in payload:
        s = set_fmt.format(k,v)
        setlist.append(s)
    set_str = ','.join(setlist)
    cmd = cmd_skeleton.format(set_str, where_clause)
    sqlcmd.put(cmd)