class HumanLikeArm:
    def move(self):
        print("HumanLikeArm is moving")

    def stop(self):
        print("HumanLikeArm is stopped")


class ArtificialArm:
    def move(self):
        print("ArtificialArm is moving")

    def stop(self):
        print("ArtificialArm is stopped")


class Robot:
    def __init__(self, arm):
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
