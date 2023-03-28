from character import *
from play import *
from time import sleep

# ========================== 실행 ==========================



def game():
    Hero, Monsters = create_monsters()

    while True:
        
        print(" -------------------------------------------")
        print("                 용사님의 대모험         ") 
        print(" -------------------------------------------")
        print("     1. 튜토리얼")  
        print("     2. 전투")
        print("     3. 내 정보 보기")
        
         
        
        command = int(input("숫자 선택"))
        
        if command == 1:
            skill_info()
        
        elif command == 2:
            while True:
                show_start(Hero, Monsters)
                show_monster(Hero, Monsters)
                # 플레이어 공격
                Monsters = player_turn(Hero, Monsters)
                sleep(1)
                # 몬스터 체력 확인
                Monsters, game_over = monster_death(Monsters)
                if game_over:
                    # player_lv+=1
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
            
            
            
        
        else:
            print("잘못입력")

            
                
                
                
                
game()
