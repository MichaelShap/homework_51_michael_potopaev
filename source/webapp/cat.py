from random import randint


class Cat:
    name = ''
    age = '1 год'
    happiness = 40
    hunger = 40
    sleep = False

    @classmethod
    def get_name(cls, request):
        cls.name = request.POST.get('name')

    @classmethod
    def asleep(cls):
        if not cls.sleep:
            cls.sleep = True

    @classmethod
    def feed(cls):
        if cls.sleep:
            pass
        else:
            cls.hunger += 15
            cls.happiness += 5
            cls.balance()

    @classmethod
    def play(cls):
        if cls.sleep:
            cls.happiness -= 5
            cls.sleep = False
            cls.balance()
        else:
            x = randint(1, 3)
            if x == 1:
                cls.hunger -= 10
                cls.happiness = 0
                cls.balance()
            else:
                cls.hunger -= 10
                cls.happiness += 15
                cls.balance()

    @classmethod
    def balance(cls):
        if cls.happiness < 0:
            cls.happiness = 0
        if cls.happiness > 100:
            cls.happiness = 100
        if cls.hunger < 0:
            cls.hunger = 0
        if cls.hunger > 100:
            cls.hunger = 100
            cls.happiness -= 30
            if cls.happiness < 0:
                cls.happiness = 0
