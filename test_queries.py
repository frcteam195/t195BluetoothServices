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

str = {"AutoStartPos":4,"NumWheels":6,"NumDriveMotors":3,"WheelTypeID":2,"DriveTypeID":2,"MotorTypeID":2,"LanguageID":1,"Speed":8,"GearRatio":"10:1","NumGearSpeed":1,"RobotLength":36,"RobotWidth":36,"RobotHeight":36,"RobotWeight":136,"Pneumatics":1,"NumPreload":5,"AutoBallsScored":5,"MoveBonus":1,"AutoPickUp":1,"AutoStartPosID":4,"AutoSummary":"cool","TeleBallsScored":14,"MaxBallCapacity":5,"ColorWheel":1,"TeleDefense":0,"TeleDefenseEvade":1,"TeleStrategy":"score big","CanClimb":1,"CenterClimb":1,"CanMoveOnBar":1,"LockingMechanism":0,"ClimbHeightID":8}
print(type(str))
for k,v in str.items():
    print(k,type(v))