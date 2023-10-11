import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


class LorenzDinamics:
    def __init__(
            self,
            coord: list,
            params: list,
            interval: list,
            noise: list,
            step
    ) -> object:
        self.sigma = params[0]
        self.beta = params[1]
        self.ro = params[2]
        self.x0 = coord[0]
        self.y0 = coord[1]
        self.z0 = coord[2]
        self.t0 = interval[0]
        self.t1 = interval[1]
        self.xnoise = noise[0]
        self.ynoise = noise[1]
        self.znoise = noise[2]
        self.step = step
    
    def __call__(self, t: float, state: list) -> list:
        x = self.sigma * (state[1] - state[0]) + np.random.normal(0, self.xnoise, 1)[0]
        y = self.ro * state[0] - state[1] - state[0] * state[2] + np.random.normal(0, self.ynoise, 1)[0]
        z = state[0] * state[1] - self.beta * state[2] + np.random.normal(0, self.xnoise, 1)[0]
        return x, y, z
    
