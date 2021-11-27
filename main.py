import numpy as np
from dethree import Variable


if __name__ == "__main__":
    x = Variable(np.array([2.0]))
    y = (x + 3) ** 2
    y.backward()

    print(y)
    print(x.grad)