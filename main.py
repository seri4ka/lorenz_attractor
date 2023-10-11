from lorenzlib.lorenz_attractor import LorenzDinamics as ld
from lorenzlib.simulator import Simulator as sim

l1 = ld(
    coord=[1, 2, 3],
    params=[10, 8/3, 28],
    interval=[0, 33],
    noise=[0.05, 0.02, 0.01],
    step=0.01
    )
l2 = ld(
    [2, 8, 1],
    [10, 8/3, 28],
    [0, 33],
    [0.07, 0.3, 0.01],
    0.01
    )

s1 = sim(l1)
s2 = sim(l2)

print(s2.run())
s2.plot()
