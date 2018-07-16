import os
import numpy as np


if __name__ == "__main__":
    x = [-2.1, -1, 4.3]
    y = [3, 1.1, 0.12]
    z = np.vstack((x,y))
    print  np.cov(x,y)
    print  np.cov(z)
   
 
