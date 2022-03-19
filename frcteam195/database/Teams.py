from frcteam195.database import sqlcmd


def get():
    results = sqlcmd.get_list("SELECT distinct a.* FROM Teams a, CurrentEventTeams b " +
                       "WHERE a.Team = b.Team " +
                         "ORDER BY a.Team")
    return results

def put(key_val, payload):
    cmd_skeleton = 'UPDATE Teams SET {} {}'
    set_fmt = "{} = {}"
    where_clause = ' WHERE Team = {}'.format(key_val)
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