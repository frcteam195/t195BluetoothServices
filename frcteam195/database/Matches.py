from frcteam195.database import sqlcmd


def get(matchId=None):
    if matchId is not None:
        cmd = """SELECT m.EventID, m.MatchID, m.MatchNo, m.RedTeam1, m.RedTeam2, m.RedTeam3,
                         m.BlueTeam1, m.BlueTeam2, m.BlueTeam3
                         FROM Matches m, Events e
                         WHERE e.EventID = m.EventID AND m.MatchID = {} AND e.CurrentEvent = 1
                         ORDER BY m.MatchNo""".format(matchId)
    else:
        cmd = """SELECT m.EventID, m.MatchID, m.MatchNo, m.RedTeam1, m.RedTeam2, m.RedTeam3,
                         m.BlueTeam1, m.BlueTeam2, m.BlueTeam3
                         FROM Matches m, Events e
                         HERE e.EventID = m.EventID AND e.CurrentEvent = 1
                         ORDER BY m.MatchNo"""
    results = sqlcmd.get_list(cmd)
    return results

