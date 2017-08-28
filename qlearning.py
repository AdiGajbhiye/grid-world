import random
import subprocess
import time

states_action = [[None for i in range(4)] for i in range(4)]
stateMap = [[0 for i in range(4)] for i in range(4)]
Qvalues = [[[0 for i in range(4)] for i in range(4)] for i in range(4)]

discountFactor = 0.9
epsilon = 0.8  # how much exploration
livingReward = -0.1


def printMatrix(mat):
    for i in reversed(mat):
        for j in i:
            print("%+06.2f" % j, end=" ")
        print()
    print('-' * 50)


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


def initialzeNextState(i, j):
    return (withinBoundary(i - 1, j),
            withinBoundary(i + 1, j),
            withinBoundary(i, j - 1),
            withinBoundary(i, j + 1))


def initializeStateModel():
    for i in range(4):
        for j in range(4):
            states_action[i][j] = initialzeNextState(i, j)
    states_action[2][0] = ((1, 0), (3, 0), (2, 0), (2, 0))
    states_action[2][2] = ((1, 2), (3, 2), (2, 2), (2, 3))
    states_action[1][1] = ((0, 1), (1, 1), (1, 0), (1, 2))
    states_action[3][1] = ((3, 1), (3, 1), (3, 0), (3, 2))


def getReward(i, j):
    if (i, j) == (3, 3):
        return 10
    if (i, j) == (2, 3):
        return -10
    return livingReward


def getNextState(i, j, action):
    return states_action[i][j][action]


def printStateMap(i, j):
    global stateMap
    # time.sleep(0.5)
    subprocess.call(["clear"])
    stateMap[i][j] = 1
    printMatrix(stateMap)
    stateMap[i][j] = 0


def printQvalues():
    for i in reversed(Qvalues):
        for j in i:
            for action in j:
                print("%+06.2f" % action, end=" ")
            print(" ", end="@@")
        print()
    print('-' * 50)


def printPolicy():
    for i in reversed(range(0, 4)):
        for j in range(0, 4):
            action = Qvalues[i][j].index(max(Qvalues[i][j]))
            if action == 0:
                print(",", end=" ")
            if action == 1:
                print("^", end=" ")
            if action == 2:
                print("<", end=" ")
            if action == 3:
                print(">", end=" ")
        print()
    print('-' * 50)


def shouldExplore():
    if random.random() < epsilon:
        return True
    return False


def eGreedy(i, j):
    if shouldExplore():
        action = random.randint(0, 3)
    else:
        action = Qvalues[i][j].index(max(Qvalues[i][j]))
    nexti, nextj = getNextState(i, j, action)
    sample = getReward(nexti, nextj) + discountFactor * \
        max(Qvalues[nexti][nextj])
    Qvalues[i][j][action] = (1 - alpha) * \
        Qvalues[i][j][action] + alpha * sample
    return nexti, nextj


def train():
    stateMap[2][1] = 7
    currState = 0, 0
    while currState != (3, 3) and currState != (2, 3):
        currState = eGreedy(*currState)
        printStateMap(*currState)
        printQvalues()
        printPolicy()


def main():
    global alpha
    n = 1
    initializeStateModel()
    while True:
        alpha = 1 / n  # learning rate
        train()
        n += 1
        time.sleep(1)
        subprocess.call(["clear"])

if __name__ == "__main__":
    main()
