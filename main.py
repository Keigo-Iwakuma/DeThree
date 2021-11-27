import numpy as np
from dethree import Variable
import dethree.functions as F
from dethree.utils import plot_dot_graph


if __name__ == "__main__":
    x = Variable(np.array(2.0))
    y = x ** 2
    y.backward(create_graph=True)
    gx = x.grad
    x.cleargrad()

    z = gx ** 3 + y
    z.backward()
    print(x.grad)