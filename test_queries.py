from frcteam195.database import Users, Config, MatchScouting, Teams
import json
import hashlib

#users = Users.get()
#for user in users:
#    print(user['FirstName'], user['LastName'])

#matches = MatchScouting.get(1)
#for match in matches:
#    print(match)

configs = Config.get('Team 195 Scout 1')
jconfig = json.dumps(configs).encode()
hash_object = hashlib.md5(jconfig).hexdigest()
print(hash_object)
if hash_object == "ef50a0aa7444fb905639e4c78819dbcd":
    print("They match!")

#print(configs)
#for config in configs:
#    print(json.dumps(config))

#ret_string = "{{'result': '{}', 'payload':{} }}"
#result = 'success'
#teams = Teams.get()
#for team in teams:
#    print(ret_string.format(result, teams))


