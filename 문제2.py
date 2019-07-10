import random
class user:
    def __init__(self,name):
        self.name=name
        self.power=random.randrange(6,8)
        self.wise=random.randrange(6,8)

        if self.power > self.wise:
            self.job="전사"
        elif self.power < self.wise:
            self.job="법사"
        else:
            self.job="궁수"

    def showData(self,name):
        print("캐릭터 이름 : %s"%self.name)
        print("캐릭터 정보 : 힘(%d), 지력(%d)"%(self.power,self.wise))
        print("캐릭터 직업 : %s"%self.job)



#main 부분
name = input("캐릭터의 이름을 입력하세요 : ")
mychar = user(name)
mychar.showData(name)