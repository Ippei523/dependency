from abc import ABC, abstractmethod


class IArm(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class HumanLikeArm(IArm):
    def move(self):
        print("HumanLikeArm is moving")

    def stop(self):
        print("HumanLikeArm is stopped")


class ArtificialArm(IArm):
    def move(self):
        print("ArtificialArm is moving")

    def stop(self):
        print("ArtificialArm is stopped")


class Robot:
    def __init__(self, arm: IArm):
        self.arm = arm

    def move(self):
        self.arm.move()

    def stop(self):
        self.arm.stop()


if __name__ == "__main__":
    arm = ArtificialArm()
    # arm = HumanLikeArm()

    robot = Robot(arm=arm)
    robot.move()
    robot.stop()
