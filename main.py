import random

# print("hello world")
# for i in range(5):
#     print(i)

class game:
    """
    this is the class of the tic tac toe game
    """
    state = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]
    turn = 0
    isOver = False

    def __init__(self):
        pass
    def display(self):
        for row in self.state:
            # print(row, " ")
            for index, column in enumerate(row):
                # print(index+1, " ", end=" ")
                # print("\n") 
                print(column, " ", end=" ")
            print("\n")
    def getState(self):
        return self.state
    def play(self):
        choice = ""
        res = -1
        while res == -1 :
            choice = input("jouez ? : ")
            if choice == "00": 
                self.isOver = True
                break
            res = self.place(choice, 'X')

        if self.checkWin():
            if self.checkWin != 101 :
                self.isOver = True
                print('You won !')
            else : 
                self.isOver = True
                print('Draw :(')
    
    def computerPlay(self):
        res = -1
        while res == -1 :
            choice = random.choice(["a", "b", "c"]) + random.choice(["1", "2", "3"])
            res = self.place(choice, 'O')
        if self.checkWin():
            if self.checkWin() != 101 : 
                self.isOver = True
                print('Computer won !')
            else : 
                self.isOver = True
                print('Draw :(')

    def place(self, choice, playType):
        if(choice == "a1"):
            if self.state[0][0] != "-":
                return -1
            self.state[0][0] = playType 
        elif(choice == "a2"):
            if self.state[0][1] != "-":
                return -1
            self.state[0][1] = playType 
        elif(choice == "a3"):
            if self.state[0][2] != "-":
                return -1
            self.state[0][2] = playType 
        elif(choice == "b1"):
            if self.state[1][0] != "-":
                return -1
            self.state[1][0] = playType 
        elif(choice == "b2"):
            if self.state[1][1] != "-":
                return -1
            self.state[1][1] = playType 
        elif(choice == "b3"):
            if self.state[1][2] != "-":
                return -1
            self.state[1][2] = playType 
        elif(choice == "c1"):
            if self.state[2][0] != "-":
                return -1
            self.state[2][0] = playType 
        elif(choice == "c2"):
            if self.state[2][1] != "-":
                return -1
            self.state[2][1] = playType 
        elif(choice == "c3"):
            if self.state[2][2] != "-":
                return -1
            self.state[2][2] = playType 
        else:
            return -1
        return 0
    def checkWin(self) :
        temp = self.getState()
        if temp[0][0] != "-": #check if win from the top left point
            if temp[0][0].__eq__(temp[0][1]) and temp[0][0].__eq__(temp[0][2]):
                return True
            elif temp[0][0].__eq__(temp[1][0]) and temp[0][0].__eq__(temp[2][0]):
                return True
            else:
                pass
            
        if temp[2][2] != "-": #check if win from the bottom right point
            if temp[2][2].__eq__(temp[2][1]) and temp[2][2].__eq__(temp[2][0]):
                return True
            elif temp[2][2].__eq__(temp[1][2]) and temp[2][2].__eq__(temp[0][2]):
                return True
            else:
                pass
        
        if temp[1][1] != "-": #check if win from the middle point
            if temp[1][1].__eq__(temp[0][1]) and temp[1][1].__eq__(temp[2][1]):
                return True
            elif temp[1][1].__eq__(temp[1][0]) and temp[1][1].__eq__(temp[1][2]):
                return True
            elif temp[1][1].__eq__(temp[0][2]) and temp[1][1].__eq__(temp[2][0]):
                return True
            elif temp[1][1].__eq__(temp[0][0]) and temp[1][1].__eq__(temp[2][2]):
                return True
            else:
                pass
        
        
        for row in temp: # check id draw or not
            if not "-" in row: # check every row if there is no space left
                spaceLeftInRow = False 
            else: #if yes = no draw
                spaceLeftInRow = True
                break
        if not spaceLeftInRow :
            return 101
        return False



test = game()
test.display()
while not test.isOver :
    test.play()
    test.display()
    if test.isOver:
        break
    test.computerPlay()
    test.display()
    if test.isOver:
        break
