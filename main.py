from lorenzlib.lorenz_attractor import LorenzDinamics as ld
from lorenzlib.simulator import Simulator as sim
from lorenzlib.data import LorenzData


params_l1 = LorenzData(
    coord = [1, 2, 3],
    params = [10, 8/3, 24],
    interval = [0, 33],
    noise = [8, 7, 9],
    step = 0.01
)

l1 = ld(params_l1)
s1 = sim(l1)

print(s1.run())
s1.plot()
