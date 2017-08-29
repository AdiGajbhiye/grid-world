import subprocess
import time
import grid
import numpy as np

livingReward = -0.4
inp = np.zeros((4,4), dtype=np.int) 
out = np.zeros(4)

def sigmoid(x):
    return (1/(1+np.exp(-x)))
    
def forwardPass():
    global inp, out
    np.copyto(inp, world.map)
    inpRe = inp.reshape((16,))
    for i in range(4):
        temp = np.dot(weights[i].reshape((16,)), inpRe)
        temp = np.add(temp, biases[i])
        out[i] = sigmoid(temp)


def testModel():
    forwardPass()
    world.printWorld()
    time.sleep(1)
    subprocess.call(["clear"])
    while not world.isExit():
        action = np.argmax(out)
        print(action)
        world.changeState(action)
        world.printWorld()
        world.printAction(action)
        time.sleep(1)
        subprocess.call(["clear"])
        forwardPass()


def printPolicy():
    for i in reversed(range(4)):
        for j in range(4):
            if (i, j) == (2, 1):
                continue
            world.setState(i, j)
            forwardPass()
            action = np.argmax(out)
            if action == 0: print(",", end=" ")
            if action == 1: print("^", end=" ")
            if action == 2: print("<", end=" ")
            if action == 3: print(">", end=" ")
        print()


def main():
    global world, weights, biases
    world = grid.GridWorld(livingReward)
    weights = np.load("weights.npy")
    biases = np.load("biases.npy")
    # testModel()
    printPolicy()

if __name__ == "__main__":
    main()
