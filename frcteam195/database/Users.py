from frcteam195.database import sqlcmd


def get():
    results = sqlcmd.get("SELECT * FROM Users ORDER BY LastName, FirstName")
    return results
