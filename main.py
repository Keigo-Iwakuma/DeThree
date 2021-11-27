import math
import numpy as np
from dethree import Variable, Function
from dethree.utils import plot_dot_graph


def f(x):
    y = x ** 4 - 2 * x ** 2
    return y


def gx2(x):
    return 12 * x ** 2 - 4


if __name__ == "__main__":
    x = Variable(np.array(2.0))
    iters = 10

    for i in range(iters):
        print(i, x)

        y = f(x)

        x.cleargrad()
        y.backward()

        x.data -= x.grad / gx2(x.data)