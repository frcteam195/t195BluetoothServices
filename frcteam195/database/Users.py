from frcteam195.database import sqlcmd


def get():
    results = sqlcmd.get_list("SELECT * FROM Users ORDER BY LastName, FirstName")
    return results
