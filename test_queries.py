from frcteam195.database import Users, Config, MatchScouting, Teams, Words, WordCloud
import json
import hashlib

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

str = {"AutoStartPos":5,"AutoDidNotShow":0,"AutoMoveBonus":1,"AutoBallLow":0,"AutoBallOuter":0,"AutoBallInner":5,"AutoPenalty":0,"TeleBallLowZone1":0,"TeleBallOuterZone1":0,"TeleBallInnerZone1":0,"TeleBallOuterZone2":0,"TeleBallInnerZone2":0,"TeleBallOuterZone3":21,"TeleBallInnerZone3":4,"TeleBallOuterZone4":0,"TeleBallInnerZone4":0,"TeleBallOuterZone5":0,"TeleBallInnerZone5":0,"TeleWheelStage2Time":4,"TeleWheelStage2Status":1,"TeleWheelStage2Attempts":0,"TeleWheelStage3Time":0,"TeleWheelStage3Status":0,"TeleWheelStage3Attempts":0,"ClimbStatus":0,"ClimbHeight":0,"ClimbPosition":0,"ClimbMoveOnBar":0,"ClimbLevelStatus":1,"SummBrokeDown":0,"SummLostComm":0,"SummSubSystemBroke":0,"SummGroundPickup":0,"SummHopperLoad":0,"SummPlayedDefense":0,"SummDefPlayedAgainst":1}
print(type(str))
for k,v in str.items():
    print(k,v)