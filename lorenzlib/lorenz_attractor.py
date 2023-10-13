import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


class LorenzDinamics:
    def __init__(
        self,
        lorenz_data: object
    ) -> object:
        self.sigma = lorenz_data.params[0]
        self.beta = lorenz_data.params[1]
        self.ro = lorenz_data.params[2]
        self.x0 = lorenz_data.coord[0]
        self.y0 = lorenz_data.coord[1]
        self.z0 = lorenz_data.coord[2]
        self.t0 = lorenz_data.interval[0]
        self.t1 = lorenz_data.interval[1]
        self.xnoise = lorenz_data.noise[0]
        self.ynoise = lorenz_data.noise[1]
        self.znoise = lorenz_data.noise[2]
        self.step = lorenz_data.step
    
    def __call__(self, t: float, state: list) -> list:
        x = self.sigma * (state[1] - state[0]) + np.random.normal(0, self.xnoise, 1)[0]
        y = self.ro * state[0] - state[1] - state[0] * state[2] + np.random.normal(0, self.ynoise, 1)[0]
        z = state[0] * state[1] - self.beta * state[2] + np.random.normal(0, self.xnoise, 1)[0]
        return x, y, z

