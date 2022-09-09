from  dino_runner.components.power_up.power_up import PowerUp

from dino_runner.utils.constants import HEART, HEART_TYPE

class Heart_power_up(PowerUp):
    def __init__(self):
        self.image = HEART
        self.type = HEART_TYPE
        super(Heart_power_up,self).__init__(self.image, self.type)