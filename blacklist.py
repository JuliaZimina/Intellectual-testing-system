groupStat[self.user.getGroup()][self.theme]=groupStat[self.user.group].get(self.theme, [0,0])
groupStat[self.user.getGroup()][self.theme][0]+=len(self.ex_quest)
groupStat[self.user.getGroup()][self.theme][1]+=self.answer.count(1)
if self.user.getLogin() not in userStat.keys():
    userStat[self.user.getLogin()]=[]
userStat[self.user.getLogin()].append[self.theme,result]



#логин;группа;математика;английский;физика
gradeStat={}
gradeStat[self.user.getLogin()]={"group":self.user.getGroup,self.theme:result}