from frcteam195.database import sqlcmd


def get(computer_name=None):
    cmd = "SELECT a.AllianceStationID, a.AllianceStation AllianceStation, c.ComputerTypeID ComputerTypeID " \
            "FROM AllianceStations a, Computers c " \
            "WHERE a.AllianceStationID = c.AllianceStationID " \
            "AND c.ComputerName = '{0}'".format(computer_name)
    results = sqlcmd.get(cmd)
    cmd = ("SELECT EventID, EventName, EventLocation from Events " +
                   "WHERE CurrentEvent = 1")
    results2 = sqlcmd.get(cmd)
    results.update(results2)
    return results







