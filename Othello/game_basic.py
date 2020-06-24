class game_basic():
    size = 10
    array2D =[]
    score = []
    direction = {0:(1,0),1:(-1,0),2:(0,1),3:(0,-1),4:(1,1),5:(-1,-1),6:(1,-1),7:(-1,1)}
    def __init__(self):
        self.array2D = [[" " for _ in range(self.size)] for _ in range(self.size)]
        self.score = [[-1 for _ in range(self.size)] for _ in range(self.size)]
    def gamefield(self):
        for i in range (self.size):
            self.array2D[0][i]='W'
            self.array2D[9][i]='W'
            self.array2D[i][0]='W'
            self.array2D[i][9]='W'
        self.array2D[4][4] = "X"
        self.array2D[5][5] = "X"
        self.array2D[4][5] = "O"
        self.array2D[5][4] = "O"     
    def checkwin(self):
        cnt_X = 0
        cnt_O = 0
        cnt_dot = 0
        for i in range (1,9):
            for j in range(1,9):
                if(self.array2D[i][j] == "X"):
                    cnt_X += 1
                elif(self.array2D[i][j] == "O"):
                    cnt_O += 1
                elif(self.array2D[i][j] == " "):
                    cnt_dot += 1
        if(cnt_dot == 0 or cnt_O == 0 or cnt_X ==0):
            if(cnt_X>cnt_O):
                print("X win")
            elif(cnt_X<cnt_O):
                print("O win")
            else:
                print("tie")
            return 1
        else:
            return 0
    def check_chess(self,x,y, user,mode):
        Sum = 0
        divergence = 0
        if(user == 1):
            symbol = "O" 
            symbol_2 = "X"
        else:
            symbol = "X"
            symbol_2 = "O"
        for i in range(8):
            for j in range(1,8):
                (v_x,v_y) = self.direction.get(i)
                if(self.array2D[x][y]!= " "):
                    break
                if(self.array2D[x+j*v_x][y+j*v_y] == "W" or self.array2D[x+j*v_x][y+j*v_y] == " "or self.array2D[x+j*v_x][y+j*v_y] == "." ):
                    break
                if(self.array2D[x+j*v_x][y+j*v_y] != symbol):
                    Sum += j -1
                    if(mode == "set"):
                        for k in range(1,j):
                            self.array2D[x+k*v_x][y+k*v_y] = symbol_2
                    elif(mode == "robot" and Sum > 0):
                        for k in range(1,j):
                            divergence += self.count_square(x+k*v_x,y+k*v_y,user)
                        return divergence
                    break
        if(mode == "set"):
            return Sum         
        elif(mode == "able"):
            return Sum  
        elif(mode == "robot" and divergence == 0):
            return -1
    def gamefield_print(self):
         for i in range (self.size):
            for j in range(self.size):
                if(j!=self.size-1):
                    print(self.array2D[i][j],end = " ")
                else:
                    print(self.array2D[i][j])
    def enter (self):
        y = x = 0
        y = int(input('x'))
        x = int(input('y')) 
        while(9 < x or x < 0 or 9 < y or y < 0):
            y = int(input('x'))
            x = int(input('y'))
        return x,y 
    def able(self,user):
        for i in range(1,9):
            for j in range (1,9):
                permit = self.check_chess(j,i,user,"able")
                if(permit>0):
                    self.array2D[j][i] = "."
        self.gamefield_print()
    def clear_dot(self):
        set_pass = 1
        cnt = 0
        for i in range(1,9):
            for j in range (1,9):
                if(self.array2D[j][i] != "O" and self.array2D[j][i] != "X"):
                    self.array2D[j][i] = " "
                    set_pass = 0
                if(self.array2D[j][i]=="."):
                    cnt += 1
        if(set_pass == 1):
            return 1
        elif(set_pass == 2):
            return 2
        else :
            return 0
    def set_chess(self,x,y,user):
        if(user == 1):
            symbol = "X" 
        else:
            symbol = "O"
        judgement = self.check_chess(x,y,user,"set")
        if judgement > 0 :
            self.array2D[x][y] = symbol
            return 1
        else:
            return 0
    def push_array(self):
        return self.array2D
    def count_square(self,x,y,user):
        cnt = 0
        for k in range (0,8):
            (v_x,v_y) = self.direction.get(k)
            if(self.array2D[x+v_x][y+v_y] == " "):
                cnt += 1
        return cnt    
    def predict_best_move(self,user):
        for i in range (1,9):
            for j in range(1,9):
                if(j!=8):
                    print(self.score[i][j],end = " ")
                else:
                    print(self.score[i][j])
        max_score = 1000
        max_x = 0
        max_y = 0
        for i in range(1,9):
            for j in range(1,9):
                self.score[i][j]=self.check_chess(i,j,user,"robot")
                if(-1<self.score[i][j]<max_score):
                    max_score = self.score[i][j]
                    max_x = i
                    max_y = j
        for i in range (1,9):
            for j in range(1,9):
                if(j!=8):
                    print(self.score[i][j],end = " ")
                else:
                    print(self.score[i][j])
        return max_x,max_y
        
