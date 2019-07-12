import random

class DressUpGame:
    def __init__(self):
        self.start()
        self.new_char=None

    def start(self):
        make_item()
        self.print_start_guide()  # 시작 안내문
        while self.get_action() != False:
            self.get_action()  # 뭘 할건지 물어보고 받음


        self.print_ending()     #엔딩

    def print_start_guide(self):  # 게임 설명
        print("****블링블링 내 캐릭터를 꾸며보자!****")
        choice = int(input("시작(1), 종료(2) "))
        if choice == 1:
            self.create_character()
        elif choice == 2:
            print("종료")
            exit()
        else:
            print("1,2만 하라고 했습니다 ㅡㅡ")
            exit()

    def print_ending(self):
        print("----The end----")
        exit()

    def create_character(self):
        self.new_char = Character()
        self.new_char.show_data()
        #self.new_char.set_money(2000)

    def gold(self):
        while True:
            print('돈을 벌고싶으면 "show me"를 입력 후 "the money"를 입력하세요 \n돈을 그만 벌고싶으면 "잘자요~"를 입력해 주세요')
            quest1 = input('첫번째 노동 : ')
            if quest1 == 'show me':
                quest2 = input('두번째 노동 : ')
                if quest2 == 'the money':
                    print('500원 적립')
                    self.new_char.set_money(500)
                    continue
                else:
                    print('절반 맞았는데 ㅎㅎ 틀렸어요~~화이팅^^')
            elif quest1 == '잘자요~':
                print('지갑에 %d 만큼 있네요 :)' % self.new_char.get_money())
                break
            else:
                print('틀렸어요~~화이팅^^')
                continue

    def get_equipment(self):
        if self.new_char.get_money() < 500:
            print('회장님 : 보증금에서 까드리면 될까요??')
        else:
            self.new_char.set_money(-500)
            number = random.randint(0, 15)
            random_box = itemlist[number]
            print("제발요........ " + str(isinstance(random_box, Items)))
            print(random_box.it_name, '가 나왔습니다.')

            if random_box.it_equipment == "top":
                self.new_char.put_item_into_bag(random_box, None, None, None)
            elif random_box.it_equipment == "bottom":
                self.new_char.put_item_into_bag( None,random_box, None, None)
            elif random_box.it_equipment == "hat":
                self.new_char.put_item_into_bag( None, None,random_box, None)
            elif random_box.it_equipment == "shoes":
                self.new_char.put_item_into_bag( None, None, None, random_box)
            else:
                print('뭔가 잘못 건드린거같아')

    def show_states(self):
        self.new_char.show_data()

    def equip(self):
        item = input("티, 바지, 모자, 신발 뭘 장착하시겠습니까 ")
        if item == "티":
            name = input("무슨 티? ")
            if self.new_char.set_total_equipment(name) != 0:
                print("장착 성공")
            else:
                print("장착 실패")
        elif item == "바지":
            name = input("무슨 바지? ")
            if self.new_char.set_total_equipment(None, name) != 0:
                print("장착 성공")
            else:
                print("장착 실패")
        elif item == "모자":
            name = input("어떤 모자? ")
            if self.new_char.set_total_equipment(None, None, name) != 0:
                print("장착 성공")
            else:
                print("장착 실패")
        elif item == "신발":
            name = input("어떤 신발? ")
            if self.new_char.set_total_equipment(None, None, None, name) != 0:
                print("장착 성공")
            else:
                print("장착 실패")
        else:
            print("그런건 없다.")

    def get_action(self):
        move=input("무엇을 실행하시겠습니까? (1 = 돈벌기, 2 = 옷 뽑기, 3 = 현재 내 매력 확인, 4. 옷 입히기) 1~4 또는 '나가기'를 입력해주세요")

        if move=='1':
            self.gold()
        elif move=='2':
            self.get_equipment()
        elif move =='3':
            self.show_states()
        elif move == '4':
            self.equip()
        elif move =='나가기':
            return False


class Character:
   def __init__(self):
       self.name = input("캐릭터 이름을 입력하시오. ")
       self.total_equipment = dict() # { ‘상의’: 찬란한 도깨비의 티셔츠}.update(키) }
       self.bag = { 'TOP': list(), 'BOTTOM': list(), 'HAT': list(), 'SHOES': list() }
       self.CHARM_XP = 0 # 전체 매력 총합
       self.charisma = 0
       self.cuteness = 0
       self.sexy = 0
       self.money = 0


   # GET & SET METHOD ###########################################################################


   def show_data(self):
       print("이름 : %s\n 매력 : %d\n 카리스마 : %d\n 귀여움 : %d\n 섹시함 : %d\n 보유머니 : %d"
             %(self.name, int(self.CHARM_XP), int(self.charisma), int(self.cuteness), int(self.sexy), int(self.money)))

   def set_money(self,money):
       self.money+=money

   def set_CHARM_XP(self):
       self.CHARM_XP = (0.5 * self.charisma) + (0.3 * self.cuteness) + (0.2 * self.sexy)


   def set_charisma(self, charisma):
       self.charisma = charisma

   def set_cuteness(self, charisma):
       self.charisma = charisma

   def set_sexy(self, charisma):
       self.charisma = charisma

   def put_item_into_bag(self, top_item=None, bottom_item=None, hat_item=None, shoes_item=None):
       if top_item is not None:
           self.bag['TOP'].append(top_item.it_name)
       if bottom_item is not None:
           self.bag['BOTTOM'].append(bottom_item.it_name)
       if hat_item is not None:
           self.bag['HAT'].append(hat_item.it_name)
       if shoes_item is not None:
           self.bag['SHOES'].append(shoes_item.it_name)

   def find_item(self, item_name):
       for i in range(len(itemlist)):
           if itemlist[i].it_name == item_name:
               return itemlist[i]
       return None

   def set_total_equipment(self, top_item=None, bottom_item=None, hat_item=None, shoes_item=None):
       if top_item is not None:
           if top_item in self.bag['TOP']:
               self.total_equipment.update(TOP=top_item)
               item = self.find_item(top_item)
               if item != None:
                   self.charisma += int(item.it_charisma)
                   self.cuteness += int(item.it_cute)
                   self.sexy += int(item.it_sexy)
                   self.set_CHARM_XP()
               else:
                   print("이런 티 없음")
                   return 0
           else:
               print("이런 티 없음")
               return 0

       if bottom_item is not None:
           if bottom_item in self.bag['BOTTOM']:
               self.total_equipment.update(BOTTOM=bottom_item)
               item = self.find_item(bottom_item)
               if item != None:
                   self.charisma += int(item.it_charisma)
                   self.cuteness += int(item.it_cute)
                   self.sexy += int(item.it_sexy)
                   self.set_CHARM_XP()
               else:
                   print("이런 바지 없음")
                   return 0
           else:
               print("이런 바지 없음")
               return 0

       if hat_item is not None:
           if hat_item in self.bag['HAT']:
               self.total_equipment.update(HAT=hat_item)
               item = self.find_item(hat_item)
               if item != None:
                   self.charisma += int(item.it_charisma)
                   self.cuteness += int(item.it_cute)
                   self.sexy += int(item.it_sexy)
                   self.set_CHARM_XP()
               else:
                   print("이런 모자 없음")
                   return 0
           else:
               print("이런 모자 없음")
               return 0

       if shoes_item is not None:
           if shoes_item in self.bag['SHOES']:
               self.total_equipment.update(SHOES=shoes_item)
               item = self.find_item(shoes_item)
               if item != None:
                   self.charisma += int(item.it_charisma)
                   self.cuteness += int(item.it_cute)
                   self.sexy += int(item.it_sexy)
                   self.set_CHARM_XP()
               else:
                   print("이런 신발 없음")
                   return 0
           else:
               print("이런 신발 없음")
               return 0


   def get_money(self):
       return self.money

   def get_CHARM_XP(self):
       return self.CHARM_XP

   def get_charisma(self):
       return self.charisma

   def get_cuteness(self):
       return self.cuteness

   def get_sexy(self):
       return self.sexy

   def get_bag_items(self):
       return self.bag


   ##############################################################################################

   # PRINT METHOD ###########################################################################

   def print_bag(self):
       print(self.bag)

   def print_total(self):
       print(self.total_equipment)

#아이템의 개수
itemlist=[k for k in range(0,16)]


class Items:

    def __init__(self,it_name, it_equipment, it_cute, it_sexy, it_charisma):
        self.it_name = it_name
        self.it_equipment = it_equipment
        self.it_cute = it_cute
        self.it_sexy = it_sexy
        self.it_charisma = it_charisma



def make_item():

    with open('itemlist.txt', 'r') as file:
        line = None
        item_attribute=[]
        while line != '':
            line = file.readline()
            item_attribute.append(line.strip('\n'))
        item_attribute.pop()


        for i in range(0,16):
            item_attribute_solo = item_attribute[i].split(', ')

            itemlist[i]=Items(*item_attribute_solo)

        print("꾸엑…….. " + str(isinstance(itemlist[0], Items)))

#main
g=DressUpGame()