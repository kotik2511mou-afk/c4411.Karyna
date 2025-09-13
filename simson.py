import random
brands_of_car = {
    "BMW":{"fuel":100,"strength":100,"consumption":6},
    "Lada":{"fuel":50,"strength":40,"consumption":10},
    "Volvo":{"fuel":70,"strength":150,"consumption":8},
    "Ferarri":{"fuel":80,"strength":120,"consumption":14}
}
job_list = {
    "lava developr":{"salary":50, "gladness_less":10},
    "phyton developer":{"salary":40, "gladness_less":3},
    "c++ developr": {"salary": 45, "gladness_less":25}
}

class Humen:
    def __init__(self, name='Humen' ,  job=None , car=None , home=None ):
        self.name = name
        self.job = job
        self.car = car
        self.home = home
        self.gladness = 50
        self.satiety = 50
        self.money = 100

    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_home(self):
        self.home = House()
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to.repair()
            return
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <=0:
            self.shopping("food")
        else:
            pass
    def work(self):
        pass
    def shopping(self,manage):
        pass
    def chill(self):
        self.gladness+=10
        self.home.mess+=5
    def clean_home(self):
      self.gladness-=5
      self.home.mess=0
    def to_repair(self):
        self.car.strength +=100
        self.money -= 50


    def days_indexes(self,day):
        print(f"the {day} of {self.name}life")
        print(f"Money -{self.money}")
        print

    def is_alive(self):
        pass
    def live (self,day):
        pass

class Auto:
    def __init__(self,brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.consumption = brand_list[self.brand]['consumption']
        self.strength = brand_list [self.brand]["strength"]

    def drive(self):
        if self.strength >0 and self.fuel >self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print("The car not move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self,job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]