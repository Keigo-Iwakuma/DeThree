import numpy as np
from dethree import Variable
import dethree.functions as F
from dethree.utils import plot_dot_graph


if __name__ == "__main__":
    x = Variable(np.array([[1,2,3,],[4,5,6,]]))
    x = x.reshape(2, 3)
    x = x.T
    y = F.transpose(x)
    y.backward(retain_grad=True)
    print(x.grad)