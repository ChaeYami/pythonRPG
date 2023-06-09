import random


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

        print(f"\033[38;2;255;108;108m\n .. {self.name}에게 공격 받음 | HP - {damage}\033[0m")
        if other.hp == 0:
            
            print(f"\033[38;2;193;51;51m\n ... {other.name}(이)가 쓰러졌습니다 8ㅅ8\033[0m")
        
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")


# ---------- 플레이어 이름 받아오기 ----------
global_name = input('\n용사님의 이름을 입력하세요 : ')



# ========================== 플레이어 ==========================


class Player(Character):
    def __init__(self, name, hp,power, mp, lv):
        self.name = name
        self.hp = hp
        self.max_hp = hp
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
            exhausted_hp = self.max_hp-self.hp
            heal_amount = int(exhausted_hp * 0.4)
            self.hp += heal_amount
            mp_cost = 100

        other.hp = max(other.hp - damage, 0)
        self.mp -= mp_cost # 스킬 사용시 마력 소모

        if skill_type == 'physical':
            print(f"\033[38;2;161;196;255m\n .. 일반공격 | {other.name}에게 {damage}의 피해를 주었습니다!\033[0m")
            
        elif skill_type == 'magic':
            print(
                f"\033[38;2;161;196;255m\n .. 마법공격 | MP -50 | {other.name}에게 {damage}의 피해를 주었습니다!\033[0m")
            
        elif skill_type == 'heal':
            print(
                f"\033[38;2;161;196;255m\n .. 궁극기공격 | {other.name}에게 {damage}의 피해를 주었습니다! \n .. 체력을 {heal_amount}만큼 회복했습니다.({self.hp}/{self.max_hp})\033[0m")
        print(f" .. 남은 마력: {self.mp}/{self.max_mp}")

        if other.hp == 0:
            self.lv += 1
            self.max_hp += 500
            self.power += 200
            print(f"\033[38;2;141;172;255m\n ... {other.name}을 처치했다!!\033[0m")
            print(f"\n ... 레벨 1 증가 | 공격력 증가, 최대 체력 증가.")
        else:
            print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")



# ========================== 몬스터 ==========================
class Monster(Character):
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp 
        self.max_hp = hp
        self.power = power 
        

    def wait(self):
        print(f'\n\033[38;2;255;156;166m .. {self.name}의 공격이 빗나갔다!!\033[0m')

