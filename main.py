from lorenzlib.lorenz_attractor import LorenzDinamics as ld
from lorenzlib.simulator import Simulator as sim


params_l1 = {
    'coord': [1, 2, 3],
    'params': [10, 8/3, 28],
    'interval': [0, 33],
    'noise': [0.05, 0.02, 0.01],
    'step': 0.01
}
params_l2 = {
    'coord': [2, 5, 3],
    'params': [10, 81/57, 43],
    'interval': [0, 56],
    'noise': [0.05, 0.02, 0.01],
    'step': 0.01
}

# l1 = ld(**params_l1)
l2 = ld(**params_l2)

# s1 = sim(l1)
s2 = sim(l2)

# print(s1.run())
# s1.plot()

print(s2.run())
s2.plot()
