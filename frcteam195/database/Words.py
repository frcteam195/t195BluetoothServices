from frcteam195.database import sqlcmd


def get():
    results = sqlcmd.get_list("SELECT * FROM WordID ORDER BY DisplayWordOrder")
    return results
