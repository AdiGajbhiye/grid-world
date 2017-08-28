class GridWorld():

    def __init__(self, livingReward):
        self.map = [[0 for i in range(4)] for i in range(4)]
        self.map[2][1] = 7
        self.i = 0
        self.j = 0
        self.livingReward = livingReward

    def withinBoundary(i, j):
        x, y = i, j
        if x < 0:
            x = 0
        if x > 3:
            x = 3
        if y < 0:
            y = 0
        if y > 3:
            y = 3
        return x, y

    def changeState(self, action):
        if (action == 0) and ((self.i, self.j) != (3, 1)):
            self.i, self.j = GridWorld.withinBoundary(self.i - 1, self.j)
        if (action == 1) and ((self.i, self.j) != (1, 1)):
            self.i, self.j = GridWorld.withinBoundary(self.i + 1, self.j)
        if (action == 2) and ((self.i, self.j) != (2, 2)):
            self.i, self.j = GridWorld.withinBoundary(self.i, self.j - 1)
        if (action == 3) and ((self.i, self.j) != (2, 0)):
            self.i, self.j = GridWorld.withinBoundary(self.i, self.j + 1)

    def getState(self):
        return self.i, self.j

    def isExit(self):
        if ((self.i, self.j) == (3, 3)) or ((self.i, self.j) == (2, 3)):
            return True
        return False

    def reset(self):
        self.i = 0
        self.j = 0

    def getReward(self):
        if (self.i, self.j) == (3, 3):
            return 10
        if (self.i, self.j) == (2, 3):
            return -10
        return self.livingReward

    def printWorld(self):
        self.map[self.i][self.j] = 1
        for i in reversed(self.map):
            for j in i:
                print(j, end=" ")
            print()
        self.map[self.i][self.j] = 0


def main():
    grid = GridWorld(-0.4)
    grid.printWorld()

if __name__ == "__main__":
    main()
