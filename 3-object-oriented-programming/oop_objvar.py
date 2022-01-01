class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("Initializing {}".format(name))
        Robot.population += 1

    def kill_robort(self):
        print("{} is being destroyed".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} roborts working".format(
                Robot.population))

    def say_hi(self):
        print("Greetings, my master calls me {}".format(self.name))

    @classmethod
    def robert_count(cls):
        print("We have {:d} robort(s)".format(cls.population))


robort = Robot("R2-D2")
robort.name
robort.say_hi()
robort.robert_count()

print("")
robort2 = Robot("C-3PO")
robort2.name
robort2.say_hi()
robort2.robert_count()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
robort.kill_robort()
robort2.kill_robort()

Robot.robert_count()
