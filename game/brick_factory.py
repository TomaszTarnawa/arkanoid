class BrickFactory:
    def __init__(self, *args):
        self.rgb_bricks = 1.0
        self.hard_rgb_bricks = 2.0
        self.v_hard_brick = 3.0
        self.dict_bricks = {eval(f'self.{x}', {'y': x, 'self': self}): [] for x in self.__get_name_field_of_object()}
        for brick in args:
            text = str(brick).lower()
            if 'very' in text:
                self.dict_bricks[self.v_hard_brick].append(brick)
            elif 'hard' in text:
                self.dict_bricks[self.hard_rgb_bricks].append(brick)
            else:
                self.dict_bricks[self.rgb_bricks].append(brick)

    def __get_name_field_of_object(self): # funkcja z której jestem dumny :D
        expected_type = type(float())
        help_list_of_attributes = list(filter(lambda x: '__' not in x, dir(self)))
        field_list = []
        for i in help_list_of_attributes:
            if type(self.__getattribute__(i)) == expected_type:
                field_list.append(i)
        return field_list

    def create_soft_rgb_brick(self, sub_event, color):
        for brick in self.dict_bricks[self.rgb_bricks]:
            if color in brick.__name__.lower():
                return brick(sub_event)

    def create_hard_rgb_brick(self, sub_event, color):
        for brick in self.dict_bricks[self.hard_rgb_bricks]:
            if color in brick.__name__.lower():
                return brick(sub_event)

    def create_v_hard_brick(self, sub_event):
        return self.dict_bricks[self.v_hard_brick][0](sub_event)

