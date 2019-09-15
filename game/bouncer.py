class Publisher:
    def __init__(self):
        self.subscribers = None

    def get_subs(self):
        return self.subscribers

    def register(self, subs_obj):
        self.subscribers = {subs.get_event(): subs for subs in subs_obj}

    def unregister(self, if_event, event):
        if if_event == 'Dead':
            self.subscribers.pop(event)

    def dispatch(self, publish_event):
        for event in self.subscribers.keys():
            if event in publish_event:
                self.subscribers.update()


class Bouncer:
    def __init__(self, publish, brick, ball, platform):
        self.publisher = publish
        self.bricks = brick
        self.ball = ball
        self.platform = platform

    def register_all(self):
        self.publisher.register([self.bricks, self.ball, self.platform])

    def event_hit_brick(self):
        pos_ball = self.ball.get_pos()

        # for brick in self.bricks:
        #     if pos_ball == brick.get

