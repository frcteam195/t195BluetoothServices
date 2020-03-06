from frcteam195.database import sqlcmd


def get():
    results = sqlcmd.get_list("SELECT distinct a.* FROM Teams a, MatchScouting b, Events c " +
                       "WHERE a.Team = b.Team and b.EventID = c.EventID and c.CurrentEvent = 1 " +
                         "ORDER BY a.Team")
    return results

def put(key_val, payload):
    cmd_skeleton = 'UPDATE Teams SET {} {}'
    set_fmt = "{} = {}"
    where_clause = ' WHERE Team = {}'.format(key_val)
    setlist = []
    set_str = ''
    for k,v in payload:
        s = set_fmt.format(k,v)
        setlist.append(s)
    set_str = ','.join(setlist)
    cmd = cmd_skeleton.format(set_str, where_clause)
    sqlcmd.put(cmd)