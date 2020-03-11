groupStat["18БИ1"]["Историяя"]=groupStat["18БИ1"].get("История", [0,0])
groupStat["18БИ1"]["Историяя"][0]=str(int(groupStat["18БИ1"]["Историяя"][0])+5)
print("There",groupStat)

if "user33" not in userStat.keys():
    userStat["user33"]=[]
userStat["user33"].append(["Математика","2"])
print(userStat)
#логин;группа;математика;английский;физика
gradeStat={}
if "user1" not in gradeStat.keys():
    gradeStat["user1"]={}
gradeStat["user1"].update({"group":"F","Математика":"33"})
gradeStat["user1"].update({"group":"G","Математика":"33","Физика":"33"})
gradeStat["user1"].update({"group":"F","Математикfffа":"33"})
print(gradeStat)