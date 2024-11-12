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
    def __init__(self):
        self.artificial_arm = ArtificialArm()
        self.human_like_arm = HumanLikeArm()

    def move(self, is_human_like: bool = False):
        if is_human_like:
            self.human_like_arm.move()
        else:
            self.artificial_arm.move

    def stop(self, is_human_like: bool = False):
        if is_human_like:
            self.human_like_arm.stop()
        else:
            self.artificial_arm.stop()


if __name__ == "__main__":
    robot = Robot()
    robot.move(True)
    robot.stop(True)
