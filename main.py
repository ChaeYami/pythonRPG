from character import *
from play import *
from time import sleep

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
