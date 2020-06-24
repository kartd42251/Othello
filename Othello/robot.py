from game_basic import*
class robot(game_basic):
    size = 10
    score = []
    def __init__(self):
        self.score = [[0 for _ in range(self.size)] for _ in range(self.size)]
    def predict_best_move(self,user):
        super(robot,self).push_array()
        for i in range(1,9):
            for j in range(1,9):
                print("hi")
                self.score[i][j]=super(robot,self).check_chess(i,j,user,"robot")
        for i in range (self.size):
            for j in range(self.size):
                if(j!=self.size-1):
                    print(self.score[i][j],end = " ")
                else:
                    print(self.score[i][j])

