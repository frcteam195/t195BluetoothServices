from frcteam195.database import sqlcmd


def get(event_id=None):
    cmd = "SELECT a.*, b.MatchNo MatchNo FROM MatchScouting a, Matches b " \
                         "WHERE a.EventID = {} and a.MatchID = b.MatchID " \
                         "ORDER BY MatchID, AllianceStationID".format(event_id)
    results = sqlcmd.get(cmd)
    return results
