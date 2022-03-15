from frcteam195.database import sqlcmd


def get():
    results = sqlcmd.get_list("SELECT b.* FROM Events a, WordCloud b " \
                   "WHERE a.CurrentEvent = 1 AND a.EventID = b.EventID ORDER BY EventID, MatchID, Team, WordID")
    return results

def put(payload):
    ret = 'failure'
    cmd_skeleton = 'REPLACE WordCloud ({}) VALUES ({})'
    for row in payload:
        col_list = []
        val_list = []
        for k,v in row.items():
            if isinstance(v, str):
                val_list.append("'{}'".format(v))
            else:
                val_list.append("{}".format(str(v)))
            col_list.append(k)
        col_str = ','.join(col_list)
        val_str = ','.join(val_list)
        cmd = cmd_skeleton.format(col_str, val_str)
        ret = sqlcmd.put(cmd)
        if ret == 'failure':
            break
    return ret
