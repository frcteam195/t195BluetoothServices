from frcteam195.database import sqlcmd


def get(eventId):
    results = sqlcmd.get_list("SELECT a.AllianceStationID AllianceStationID, b.* FROM MatchScouting a, WordCloud b " \
                   "WHERE a.EventID = {} and a.MatchID = b.MatchID ORDER BY MatchID, AllianceStationID".format(eventId))
    return results
