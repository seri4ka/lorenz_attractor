from dataclasses import dataclass


@dataclass
class LorenzData:
    coord: list
    params: list
    interval: list
    noise: list
    step: float
