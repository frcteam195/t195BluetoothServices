from frcteam195.database import sqlcmd


def get():
    results = sqlcmd.get("SELECT distinct a.* FROM Teams a, MatchScouting b, Events c " +
                       "WHERE a.Team = b.Team and b.EventID = c.EventID and c.CurrentEvent = 1 " +
                         "ORDER BY a.Team")
    return results
