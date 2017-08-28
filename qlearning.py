import random
import subprocess
import time
import grid

Qvalues = [[[0 for i in range(4)] for i in range(4)] for i in range(4)]

discountFactor = 0.9
epsilon = 0.8  # how much exploration
livingReward = -0.4


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


def eGreedy():
    i, j = world.getState()
    if shouldExplore():
        action = random.randint(0, 3)
    else:
        action = Qvalues[i][j].index(max(Qvalues[i][j]))
    world.changeState(action)
    nexti, nextj = world.getState()
    sample = world.getReward() + discountFactor * \
        max(Qvalues[nexti][nextj])
    Qvalues[i][j][action] = (1 - alpha) * \
        Qvalues[i][j][action] + alpha * sample


def train():
    while not world.isExit():
        eGreedy()
        # printQvalues()
        # printPolicy()
        # time.sleep(1)
        # subprocess.call(["clear"])


def main():
    global alpha, world
    n = 1
    world = grid.GridWorld(livingReward)
    while True:
        alpha = 1 / n  # learning rate
        train()
        printQvalues()
        printPolicy()
        time.sleep(1)
        subprocess.call(["clear"])
        world.reset()
        n += 1

if __name__ == "__main__":
    main()
