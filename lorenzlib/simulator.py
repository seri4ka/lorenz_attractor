import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


class Simulator:
    def __init__(self, object: object, *args) -> object:
        self.lorenz = object
        self.args = args
    
    def data_maker(self):
        xt = self.lorenz.x0
        yt = self.lorenz.y0
        zt = self.lorenz.z0

        res = np.array([[xt, yt, zt, self.lorenz.t0]])

        for t in np.arange(self.lorenz.t0, self.lorenz.t1, self.lorenz.step):
            point = self.lorenz(
                t=self.lorenz.step,
                state=[
                    xt,
                    yt, 
                    zt
                    ]
            )
            xt += point[0] * self.lorenz.step
            yt += point[1] * self.lorenz.step
            zt += point[2] * self.lorenz.step
            res = np.append(res, [[xt, yt, zt, t]], axis=0)

        return res

    def run(self):
        return pd.DataFrame(self.data_maker(), columns = ['x_coord', 'y_coods', 'z_coords', 'time'])
    
    def plot(self, height=15, width=15):
        data = self.data_maker()
        x_cords = []
        y_cords = []
        z_cords = []
        for i in data:
            x_cords.append(i[0])
            y_cords.append(i[1])
            z_cords.append(i[2])
        
        fig = plt.figure(
            figsize=(
                height,
                width
            )
        )

        ax = fig.gca(projection='3d')
        ax.plot(x_cords, y_cords, z_cords, lw=1)
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_zlabel("Z Axis")
        ax.set_title("Lorenz Attractor")

        plt.show()

        return None
