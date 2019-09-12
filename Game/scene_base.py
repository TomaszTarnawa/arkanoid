from abc import ABC, abstractmethod


class SceneBase(ABC):
    def __init__(self):
        self.next = self

    @abstractmethod
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    @abstractmethod
    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    @abstractmethod
    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)
