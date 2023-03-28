from character import *
from play import *
from random import choices
from time import sleep

# ========================== 게임 진행 함수 ==========================


def create_monsters():  # 몬스터들을 저장
    global Hero
    
    Hero = Player(global_name, 10000,2000, 300, 1)  # 마력 값 추가
    Monsters = {}
    
    Monsters['종민몬'] = Monster('종민몬', 2000, 2000)
    Monsters['탁근몬'] = Monster('탁근몬', 3000, 1000)
    Monsters['영우몬'] = Monster('영우몬', 4000, 2000)
    Monsters['진규몬'] = Monster('진규몬', 5000, 1500)

    return Hero, Monsters

# 플레이어와 몬스터들의 상태
def show_start(Player, Monsters):
    print(f"\n★ ★ {Player.name}용사님 등장!! ★ ★")
    print("-------------------------------------------------------------------")
    print(
        f"HP : {Player.hp}/{Player.max_hp} | MP : {Player.mp}/{Player.max_mp} | 공격력 : {Player.power} | LV : {Player.lv}")
    print("-------------------------------------------------------------------")
    
    
def show_monster(Player, Monsters):
    print("\n야생의 몬스터들이 등장했다! \n")

    for key, name in Monsters.items():  # 몬스터들의 상태 표시

        print(f"{name.name} [ HP : {name.hp}/{name.max_hp} | 공격력 : {name.power}]  ")
        
        
        
        
def skill_info():
    print("\n마법 공격은 일반공격보다 좀 더 강하며 MP를 50 소모합니다. \n ... 궁극기는 마법 공격과 함께 체력을 회복합니다. 회복량은 소모된 HP에 비례합니다. MP를 100 소모합니다. \n\n")

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
        other = input('\n ...  ▶ 공격 대상을 선택하세요 (이름입력) : ')

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

