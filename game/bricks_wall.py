from math import ceil, floor
from random import choice


class BricksWall:
    __y_min = 84
    __y_max = 473
    __x_max = 1118

    def __init__(self, factory):
        self.factory = factory

    def level_one(self):
        bricks = []
        color = ['red', 'green', 'blue']
        amount = 220
        rgb = ceil(amount * 0.6) - 12
        h_rgb = ceil(amount * 0.3) + 14
        v_hard = floor(amount * 0.1) - 2
        line = 0
        for y in range(315, 84, -21):
            pose = 43 * line
            skip_pose = [pose, pose + 43, pose + 86, self.__x_max - (pose + 43), self.__x_max - (pose + 86),
                         self.__x_max - (pose + 129)]
            line += 1
            for x in range(0, self.__x_max, 43):
                if x in skip_pose:
                    continue
                if rgb != 0:
                    bricks.append(self.factory.create_soft_rgb_brick(f'brick ({x},{y})', choice(color)))
                    rgb -= 1
                elif h_rgb != 0:
                    bricks.append(self.factory.create_hard_rgb_brick(f'brick ({x},{y})', choice(color)))
                    h_rgb -= 1
                elif v_hard != 0:
                    bricks.append(self.factory.create_v_hard_brick(f'brick ({x},{y})'))
                    v_hard -= 1
        return bricks
