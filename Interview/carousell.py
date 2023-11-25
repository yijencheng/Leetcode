



class Users:
    def __init__(self, user_num):
        self.cur_user = None
        self.user_num = user_num
    
    def next_user(self):
        if not self.cur_user:
            self.cur_user=1
        else:
            self.cur_user+=1


class Board:
    def __init__(self, size):
        self.BOARD_SIZE = 5
        self.data = [
            [[0 for x in range(size)] for y in range(size)] 
        ]
    
    def place_is_valid(self, x, y):
        if self.data[x][y] == 0:
            return True
        else:
            return False
    
    def set_position(self, x,y, target):
        if not self.place_is_valid(x,y):
            return False
        self.data[x][y] = target
        return True

    def check_win(self):
        pass
        # self.check_row()
        # self.check_col()
        # self.check_left_diag()
        # self.check_right_diag()

    def print_row(self, x):
        for i in range(x):
            print("--%s,",self.data[x][i])
        
        print("\n")

    def is_row_match(self, x):
        same = True
        first_appear = None
        if sum(self.data[x]==0):return False # empty row

        for i in range(x):
            if self.data[x][i] == 0:continue

            if not first_appear:
                first_appear = self.data[x][i]
                continue

            if self.data[x][i] != first_appear:
                return False
        return True
    
    
    
    # def is_col_match(self, y):
    #     same = True
    #     tmp = self.data[0][y]
    #     for i in range(y):
    #         if self.data[i][y] !=tmp:
    #             return False
    #     return True
    


def main():
    print("game_start")
    board = Board(3)
    cur_user = 1


    while True:
        # print("Player %s, please enter your move ", u)
        pos = input()
        x, y = int(pos[0]), int(pos[1])
        print(x)
        print(y)

        board.set_position(x, y, cur_user)
        board.print_row(x)
        # print("is row %s match?: %s", 0, board.is_row_match(0))



        
        

  

if __name__ =="__main__":
    main()




