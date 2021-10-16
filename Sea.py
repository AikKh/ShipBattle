import time
from Board import Board

class Sea():       

    currentBord = 1
    board1 = None
    board2 = None

    def __init__(self):
        self.board1 = Board(1)
        self.board2 = Board(2)

    def intro(self):
        print('Ship Battle')
        print()
        b_or_h = str(input('Human or bot?\n(h or b)\n'))
        return b_or_h

    def inputValidator(self, x, y, board, currentBord):

        if y == 'ships' and x == 'print':
            if currentBord == 1:
                print('Second players ships')
                self.board2.printBoardWithShips()
                print()
                return False
            elif currentBord == 2:
                print('First players ships')
                self.board1.printBoardWithShips()
                print()
                return False

        co_x = -1
        co_y = -1

        try:
            co_x = int(x)
            co_y = int(y)
        except:
            print('Only nubers, please repeat:')
            return False

        if co_x not in range(0, 10) or co_y not in range(0, 10):
            print("You can use only numers with 0 to 9, please repeat:")
            return False
            
        return True

    def justInput(self, bordNum):
        if bordNum == 1:
            print('Scorpion')
        elif bordNum == 2:
            print('SubZero')

        x = input('Y cordinate:')
        y = input('X cordinate:')

        return (x, y)

    def getCurrentBord(self):
        if self.currentBord == 1:
            return self.board1

        if self.currentBord == 2:
            return self.board2

        return None

    def checkInLife(self):

            if not self.board1.isInLife():
                print("Scorpion wins")
                time.sleep(2)
                print("Fatality")
                return False

            elif not self.board2.isInLife():
                print("SubZero wins")
                time.sleep(2)
                print("Fatality")
                return False

            return True

    def startGame(self):

        self.board1.initialize()
        self.board2.initialize()

        #self.board1.printBoardWithShips();
        
        answer = self.intro()

        #self.board1.printBord()

        while self.checkInLife():
            
            if answer == 'h':

                co = self.justInput(self.currentBord)

                if not self.inputValidator(co[0], co[1], self.getCurrentBord(), self.currentBord):
                    continue

                result = self.getCurrentBord().run(co[0], co[1])

                if result == 1 or result == 2:
                    continue

                if self.currentBord == 1:
                    self.currentBord = 2
                else:
                    self.currentBord = 1

                print()

            elif answer == 'b':
                print('Bots turn\nBot: (~‾▿‾)~')
                #time.sleep(2)
                while self.board2.botForTest():
                    print('Bot: ლ(^o^ლ)')
                    time.sleep(0.5)
                    continue
                print('Bot: (ರ╭╮ರ)')
                print()

            
                

sea = Sea()
sea.startGame()