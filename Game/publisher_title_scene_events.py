class Publisher:
    def __init__(self):
        self._subscribers = None
        self._pressed_keys = None

    def get_events(self, events, pressed_keys):
        self._subscribers = {event: set() for event in events}
        self._pressed_keys = pressed_keys

    def register(self, subscriber):
        try:
            for event in subscriber.get_events():
                self._subscribers[event].add(subscriber)
        except (AttributeError, KeyError):
            pass

    def unregister(self, event, subscriber):
        self._subscribers[event].remove(subscriber)

    def dispatch(self, event, message):
        for subscriber in self._subscribers[event]:
            subscriber.update(message)