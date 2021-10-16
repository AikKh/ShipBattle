import numpy as np
import random
from Ship import Ship

class Board():

    def __init__(self, num):
        self._num = num
        self._matrix = np.zeros((10, 10), dtype=int)
        self._shipList = []
        

    _shipList = []
    _matrix = None

    def initialize(self):
        self.shipMaker(4, 1)
        self.shipMaker(3, 2)
        self.shipMaker(2, 3)
        self.shipMaker(1, 4)

    def printBord(self):
        print(self._matrix)

    def printBoardWithShips(self):
        matrixView = np.zeros((10, 10), dtype=int)
        for ship in self._shipList:
            for co in ship._cordinate:
                matrixView[co] = ship._size

        print(matrixView)

    def addShip(self, ship):
            self._shipList.append(ship)

    def printShips(self):
        for ship in self._shipList:
            ship.printShip()

    def getAroundCors(self, x, y):
        return [(x, y), (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)]

    def shipValidate(self, ship):

        for currentShip in self._shipList:
            for co in currentShip._cordinate:
                cordinates = self.getAroundCors(co[0], co[1])
                for cor in ship._cordinate:
                    if cor in cordinates:
                        return False

        return True

    def getCordinate(self, direction, x, y, i):
        if direction == 0:
            return (x, y - i)
        elif direction == 1:
            return (x + i, y)
        elif direction == 2:
            return (x, y + i)
        elif direction == 3:
            return (x - i, y)

        return None
    
    def checkBords(self, co_x, co_y, size, dir):

        if dir == 0:
            return co_y - size >= 0
        elif dir == 1:
            return co_x + size <= 9
        elif dir == 2:
            return co_y + size <= 9
        elif dir == 3:
            return co_x - size >= 0

        return False

    def shipMaker(self, size, count):

        createdShipsCount = 0
        while createdShipsCount <= count - 1:

            direction = random.randrange(0, 4)
            random_ship_x = random.randrange(0, 10)
            random_ship_y = random.randrange(0, 10)

            if self.checkBords(random_ship_x, random_ship_y, size, direction):
                
                ship = Ship(size)
                for i in range(0, size):
                    ship.addCordinate(self.getCordinate(direction, random_ship_x, random_ship_y, i))

                if self.shipValidate(ship):
                    self.addShip(ship)
                    createdShipsCount += 1


    def run(self, players_co_x, players_co_y):

        players_co_x = int(players_co_x)
        players_co_y = int(players_co_y)

        if self._matrix[(players_co_x, players_co_x)] != 0:
            print('This cordinate has already been, please repeat:')
            print()
            return 1

        print()

        for ship in self._shipList:
            #print("Cordinates: " + str(ship._cordinate))
            if ship.shipHit((players_co_x, players_co_y)):
                self._matrix[(players_co_x, players_co_y)] = ship._size
                self.printBord()
                print('Hit')
                return 2

        self._matrix[(players_co_x, players_co_y)] = 7
        self.printBord()
        print('Missed')
        return 3

    def bot_mind(self, x, y):
        pass

    def botForTest(self):
        for x in range(0, 10):
            for y in range(0, 10):
                self._matrix[x,y] = 1

    def bot(self):
        repeat = 0
        while repeat < 1 :
            miss_check = False
            bots_co_x = random.randint(0, 9)
            bots_co_y = random.randint(0, 9)
            print("Sorry")
            if self._matrix[(bots_co_x, bots_co_y)] != 0:
                continue

            for ship in self._shipList:
                if ship.shipHit((bots_co_x, bots_co_y)):
                    self._matrix[(bots_co_x, bots_co_y)] = ship._size
                    self.printBord()
                    print('Hit')
                    miss_check = True
                    repeat += 1
                    return True

            if miss_check == False: 
                self._matrix[(bots_co_x, bots_co_y)] = 7
                self.printBord()
                print('Missed')
                repeat += 1
                return False

    def isInLife(self):
        shipHit = 0
        for ship in self._shipList:
            for cor in ship._cordinate:
                if self._matrix[cor] != 0:
                    shipHit += 1
                    
        return shipHit < 20

