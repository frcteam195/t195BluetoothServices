from frcteam195.database import Users, Config, MatchScouting, Teams, Words, WordCloud
import json
import hashlib
import datetime

#users = Users.get()
#for user in users:
#    print(user['FirstName'], user['LastName'])

#matches = MatchScouting.get(1)
#for match in matches:
#    print(match['Team'])

# configs = Config.get('Team 195 Scout 1')
# jconfig = json.dumps(configs).encode()
# hash_object = hashlib.md5(jconfig).hexdigest()
# print(hash_object)
# if hash_object == "ef50a0aa7444fb905639e4c78819dbcd":
#     print("They match!")

#print(configs)
#for config in configs:
#    print(json.dumps(config))

#ret_string = "{{'result': '{}', 'payload':{} }}"
#result = 'success'
#teams = Teams.get()
#for team in teams:
#    print(team)
#    print(ret_string.format(result, teams))

#wordCloud = WordCloud.get(1)
#for word in wordCloud:
#    print(word)

jj = '{"LastUpdate": 1583845194}'
xx = json.loads(jj)
print(xx['LastUpdate'])
