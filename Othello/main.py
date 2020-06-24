from game_basic import*
from robot import*
x = 0
y = 0
user = 1
shutdown = 0
robot = robot()
main = game_basic()
main.gamefield()
while shutdown == 0 :
    main.able(user)
    enter_error = 1
    set_pass = main.clear_dot()
    if(set_pass == 0):
        if(user==1):
            x,y = main.enter()
            enter_error = main.set_chess(x,y,user)
        else:
            x,y = main.predict_best_move(-1)
            enter_error = main.set_chess(x,y,user)
    if(enter_error > 0):
        print(shutdown)
        shutdown = main.checkwin()
        user *=-1
        
    else:
        print("error")
        




