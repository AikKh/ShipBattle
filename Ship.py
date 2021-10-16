class Ship():

    _size = 0
    _cordinate = []
    
    def __init__(self, size):
        self._size = size
        self._cordinate = []

    def addCordinate(self, cordinate):
        self._cordinate.append(cordinate)

    def printShip(self):
        for co in self._cordinate:
            print(co)

    def shipHit(self, cor_tuple):
        #print("Cordinate to check: " + str(cor_tuple))
        #print("Cordinates: " + str(self._cordinate))
        return cor_tuple in self._cordinate

    def getCordinates(self):
        return self._cordinate