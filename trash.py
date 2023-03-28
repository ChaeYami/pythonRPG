






class Monster(Character):
    # def cure(self):
    #     self.hp += 1000
    #     print(f'{self.name}가 자신의 체력을 1000만큼 회복했습니다. 현재 체력 : {self.hp}')
    #     return self.hp

    def wait(self):
        print(f'{self.name}의 공격이 빗나갔다!!')





# def check_mdead(Monsters):
#     # 이번 턴에서 죽은 몬스터가 있는지 확인
#     dead_monsters = []
#     for key, value in Monsters.items():
#         if value.hp <= 0:
#             dead_monsters.append(key)
#     # 죽은 몬스터는 몬스터 명단에서 삭제
#     for i in dead_monsters:
#         del Monsters[i]
#     # 남은 몬스터가 없다면 승리 출력, 있다면 몬스터 그대로 리턴해주기
#     if len(Monsters) <= 0:
#         return Monsters, True
#     else:
#         return Monsters, False


    # ---------- 마법공격 ----------
    # def magic_attack(self, other):
    #     # if self.mp < 50:  # 마력이 부족한 경우 --> 전역함수로 옮겨버림
    #     #     print("\n마력이 부족합니다!")
    #     #     return

    #     magic_damage = random.randint(self.power * 0.9, self.power * 1.5)
    #     other.hp = max(other.hp - magic_damage, 0)
    #     self.mp -= 50  # 마력 소모
    #     print(f"\n .. 마법공격 | MP -50 | {self.name}>>{other.name}에게 {magic_damage}피해! ")
    #     print(f" .. 남은 마력: {self.mp}/{self.max_mp}")
    #     if other.hp == 0:
    #         print(f"\n ... {other.name}을 처치했다!!")
    #     else:
    #         print(f"\n{other.name} : {other.hp}/{other.max_hp}HP")

    # # ---------- 궁극기 : 공격과 동시에 체력 회복 ----------
    # def heal_attack(self, other):
    #     # if self.mp < 50:  # 마력이 부족한 경우 --> 전역함수로 옮겨버림
    #     #     print("\n ※ ※ 마력이 부족합니다! ※ ※")
    #     #     return

    #     healing_damage = random.randint(self.power * 0.9, self.power * 1.5)
    #     other.hp = max(other.hp - healing_damage, 0)
    #     exhausted_hp = 10000-self.hp

    #     self.hp += exhausted_hp*0.4  # 소모된 체력에 비례해서 치유됨. 소모 체력이 0이면 치유되지 않음
    #     self.mp -= 100
    #     print(f"\n .. 궁극기공격 | {self.name}>>{other.name}에게 {healing_damage}피해! \n .. 체력을 {exhausted_hp*0.4}만큼 회복했습니다.({self.hp}/{self.max_hp})")

    #     print(f" .. 남은 마력: {self.mp}/{self.max_mp}")
    #     if other.hp == 0:
    #         print(f"\n ... {other.name}을 처치했다!!")
    #     else:
    #         print(f"\n{other.name} : {other.hp}/{other.max_hp} [HP]")


# def monster_turn(Player, Monsters):
#     # print("\n==============================================")

#     sleep(3)
#     for key, value in Monsters.items():
#         commands = ['cure', 'attack', 'stay']
#         command = choice(commands)
#         if command == 'cure':
#             value.cure()
#         elif command == 'attack':
#             value.attack(Player)
#         elif command == 'stay':
#             value.stay()
#     return Player


# Hero, Monsters = create_monsters()

# while True:
#     show_start(Hero, Monsters)
#     # print("\n==============================================")
#     Monsters = player_turn(Hero, Monsters)
#     sleep(1)
#     Monsters, ismdead = monster_death(Monsters)
#     if ismdead:
#         print('\n승리!!!')
#         break
#     Hero = monster_turn(Hero, Monsters)
#     ispdead = player_death(Hero)
#     if ispdead:
#         print("\n패배!!!")
#         break
#     sleep(1)
