class Robot:
    """表示有一个带名字的机器人"""

    # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print('(Initializing {})'.format(self.name))

        # 当有机器人被创建时，机器人将增加人口数量
        Robot.population += 1

    def die(self):
        """挂掉了"""
        print('{} is begin desdroyed!'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one .'.format(self.name))
        else:
            print('There are still {:d} robots working'.format(
                self.population))

    def say_hi(self):
        print('my master call me :{}'.format(self.name))

    @classmethod
    def how_many(cls):
        print('now, we have {:d} robots'.format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()


print('\n\n')
droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print('\n\n')
print('destroy them')
droid1.die()
droid2.die()

Robot.how_many()
