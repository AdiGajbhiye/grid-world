import random
import subprocess
import time
import grid
import numpy as np

discountFactor = 0.9
livingReward = -0.4
weights = np.random.random_sample((4,4,4))
biases = np.random.random_sample((4,))
inp = np.zeros((4,4), dtype=np.int) 
out = np.zeros(4)
desired = np.zeros(4)
epsilon = 1

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

def backprop(action, desired):
    global inp, out
    loss = np.subtract(out[action], desired)
    i, j = world.getState()
    temp = np.subtract(1, out[action]) 
    temp = np.multiply(out[action], temp)
    weights[action][i][j] += np.multiply(loss, temp)


def shouldExplore():
    if random.random() < epsilon:
        return True
    return False

def train():
    forwardPass()
    # world.printWorld()
    # time.sleep(0.5)
    # subprocess.call(["clear"])
    while not world.isExit():
        if shouldExplore():
            action = random.randint(0,3)
        else:
            action = np.argmax(out)
        world.changeState(action)
        # world.printWorld()
        # world.printAction(action)
        # time.sleep(0.5)
        # subprocess.call(["clear"])
        forwardPass()
        desired = np.add(world.getReward(), np.multiply(discountFactor, np.max(out)))
        backprop(action, desired)


def main():
    global alpha, world, epsilon
    world = grid.GridWorld(livingReward)
    n = 0
    while epsilon > 0.1:
        print(epsilon, n)
        train()
        world.reset()
        n += 1
        if n >= 10000:
            epsilon -= 0.1
            n = 0
            np.save("weights", weights)
            np.save("biases", biases)

if __name__ == "__main__":
    main()
