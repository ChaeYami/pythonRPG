
import random
from time import sleep
from random import choices
from time import sleep

class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power


    def attack(self, other):
        damage = random.randint(self.power * 0.8, self.power * 1.2)
        other.hp = max(other.hp - damage, 0)

        print(f"\n .. {self.name}에게 공격 받음 | HP - {damage}")
        if other.hp == 0:
            self.power += 1000
            
            
            print(f"\n ... {other.name}을 처치했다!!")
        
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")


# ---------- 플레이어 이름 받아오기 ----------
global_name = input('\n용사님의 이름을 입력하세요 : ')

# ========================== 플레이어 ==========================


class Player(Character):
    def __init__(self, name, hp, power, mp, lv):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mp = mp
        self.mp = mp
        self.lv = lv

    def use_skill(self, other, skill_type):
        if skill_type == 'physical':
            damage = random.randint(self.power * 0.8, self.power * 1.2)
            mp_cost = 0
            
        elif skill_type == 'magic':
            damage = random.randint(self.power * 0.9, self.power * 1.5)
            mp_cost = 50
            
        elif skill_type == 'heal':
            damage = random.randint(self.power * 0.9, self.power * 1.5)
            exhausted_hp = 10000-self.hp
            heal_amount = int(exhausted_hp * 0.4)
            self.hp += heal_amount
            mp_cost = 100

        other.hp = max(other.hp - damage, 0)
        self.mp -= mp_cost # 스킬 사용시 마력 소모

        if skill_type == 'physical':
            print(f"\n .. 일반공격 | {other.name}에게 {damage}의 피해를 주었습니다!")
            
        elif skill_type == 'magic':
            print(
                f"\n .. 마법공격 | MP -50 | {other.name}에게 {damage}의 피해를 주었습니다!")
            
        elif skill_type == 'heal':
            print(
                f"\n .. 궁극기공격 | {other.name}에게 {damage}의 피해를 주었습니다! \n .. 체력을 {heal_amount}만큼 회복했습니다.({self.hp}/{self.max_hp})")
        print(f" .. 남은 마력: {self.mp}/{self.max_mp}")

        if other.hp == 0:
            self.power += 500
            self.lv += 1
            self.max_hp += 1000
            print(f"\n ... {other.name}을 처치했다!!")
            print(f"\n ... 레벨 1 증가 | 공격력 500 증가, 최대 체력 1000 증가.")
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")



# ========================== 몬스터 ==========================
class Monster(Character):

    def wait(self):
        print(f'\n .. {self.name}의 공격이 빗나갔다!!')



# ========================== 게임 진행 함수 ==========================


def create_monsters():  # 몬스터들을 저장
    global Hero
    Hero = Player(global_name, 10000, 2000, 300, 1)  # 마력 값 추가
    Monsters = {}
    
    Monsters['종민몬'] = Monster('종민몬', 2000, 2000)
    Monsters['탁근몬'] = Monster('탁근몬', 3000, 1000)
    Monsters['영우몬'] = Monster('영우몬', 4000, 2000)
    Monsters['진규몬'] = Monster('진규몬', 5000, 1000)

    return Hero, Monsters

# 플레이어와 몬스터들의 상태
def show_start(Player, Monsters):
    print(f"\n★ ★ {Player.name}용사님 등장!! ★ ★")
    print("-------------------------------------------------------------------")
    print(
        f"HP : {Player.hp}/{Player.max_hp} | MP : {Player.mp}/{Player.max_mp} | 공격력 : {Player.power} | LV : {Player.lv}")
    print("-------------------------------------------------------------------")
    print("\n야생의 몬스터들이 등장했다! \n")

    for key, name in Monsters.items():  # 몬스터들의 상태 표시

        print(
            f"{name.name} [ HP : {name.hp}/{name.max_hp} | 공격력 : {name.power}]  ")

# ---------- 플레이어 턴 ----------


def player_turn(Player, Monsters):
    # 공격 대상 선택하는 함수

    def use_mp(need,skill_type):
        if Player.mp < need:  # 마력이 부족한 경우
            print("\n ※ ※ 마력이 부족합니다! ※ ※")
            player_turn(Player, Monsters)
        else: # 사용가능 - 스킬 사용
            Player.use_skill(Monsters[other],skill_type)
            
    # 몬스터 딕셔너리에 없는 대상을 선택했을 시 예외 처리
    try:
        other = input('\n ... 마법 공격은 일반공격보다 좀 더 강하며 MP를 50 소모합니다. \n ... 궁극기는 마법 공격과 함께 체력을 회복합니다. 회복량은 소모된 HP에 비례합니다. MP를 100 소모합니다. \n\n ▶ 공격 대상을 선택하세요 (이름입력) : ')

        command = input(
            '\n ▶ 공격 방법을 선택하세요 (숫자 입력)\n [1. 일반공격 | 2. 마법공격 | 3. 궁극기] : ')

        if command == '1':
            use_mp(0,'physical')
        elif command == '2':
            use_mp(50,'magic')
                
        elif command == '3':
            use_mp(100,'heal')

        return Monsters
    
    except KeyError as e:  # 이미 죽은 몬스터를 선택했을 때
        print("선택한 대상이 이미 사망했거나 존재하지 않습니다. 다시 선택하세요")
        player_turn(Player, Monsters)

# ---------- 몬스터 사망 처리 ----------
def monster_death(Monsters):
    dead_monsters = []
    for key, name in Monsters.items():
        if name.hp <= 0:
            dead_monsters.append(key)
            

    for name in dead_monsters:
        del Monsters[name]
        
    

    if len(Monsters) <= 0:
        return Monsters, True
    else:
        return Monsters, False

# ---------- 몬스터 턴 ----------
def monster_turn(Player, Monsters):
    sleep(1)
    for key, value in Monsters.items():
        commands = ['attack', 'wait']
        weights = [0.7, 0.3]  # 회피 확률
        command = choices(commands, weights=weights)[0] 
        if command == 'attack':
            value.attack(Player)
        elif command == 'wait':
            value.wait()

    return Player

# ---------- 플레이어 생존 확인 ----------
def player_death(Player):
    if Player.hp <= 0:
        return True
    else:
        return False



# ========================== 실행 ==========================

def game():
    Hero, Monsters = create_monsters()

    while True:
        show_start(Hero, Monsters)
        # 플레이어 공격
        Monsters = player_turn(Hero, Monsters)
        sleep(1)
        # 몬스터 체력 확인
        Monsters, game_over = monster_death(Monsters)
        if game_over:
            print("\n================= 승리 =================")
            print("모든 몬스터를 물리쳤습니다! 게임 종료!")
            break

        # 몬스터 공격
        Hero = monster_turn(Hero, Monsters)
        # 주인공 체력 확인
        game_over = player_death(Hero)
        if game_over:
            print("\n================= 패배 =================")
            break
        sleep(1)

game()
