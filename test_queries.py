from frcteam195.database import Users, Config, MatchScouting, Teams
import json


users = Users.get()
for user in users:
    print(user['FirstName'], user['LastName'])

matches = MatchScouting.get(1)
for match in matches:
    print(match)

configs = Config.get('Team 195 Scout 1')
for config in configs:
    print(json.dumps(config))

ret_string = "{{'result': '{}', 'payload':{} }}"
result = 'success'
teams = Teams.get()
for team in teams:
    print(ret_string.format(result, teams))


