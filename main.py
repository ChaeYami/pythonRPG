from character import *
from function import *
from time import sleep

# ========================== 실행 ==========================


def game():
    Hero, Monsters = create_monsters()

    while True:
        
        print("\n\n -------------------------------------------")
        print(f"\033[38;2;81;169;255m       ~용사님의 대모험~       ♥{global_name}용사님♥ \033[0m") 
        print(" -------------------------------------------")
        print("\033[38;2;206;149;255m         1. 튜토리얼")  
        print("         2. 전투")
        print("         3. 내 정보 보기")
        print("         4. 몬스터 도감")
        print("         5. 종료\033[0m")
        print(" -------------------------------------------")
  
        
        command = int(input(" ...  ▶ 숫자 선택 : "))
        
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
            
        elif command == 3:
            show_start(Hero, Monsters)
            
        elif command == 4:
            print("\n-----------------------------------------")
            print("\033[38;2;74;215;112m              ♥몬스터 도감♥\033[0m")
            print("-----------------------------------------")
            print("\n종민몬 [ HP : 2000/2000 | 공격력 : 2000]\n탁근몬 [ HP : 3000/3000 | 공격력 : 1000]\n영우몬 [ HP : 4000/4000 | 공격력 : 2000]\n진규몬 [ HP : 5000/5000 | 공격력 : 1500]")
            print("\n-----------------------------------------")
            
        elif command == 5:
            print("게임을 종료합니다.")
            break   
            
            
            
        else:
            print("잘못입력")
     
                
game()
