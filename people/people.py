"""
Class people
"""

from datetime import datetime

class People:
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, talking=False):
       self.name = name
       self.age = age
       self.eating = eating
       self.talking = talking

    def to_speak(self, topic):
        if self.eating:
            print(f'{self.name} cant talk while eating.')
            return

        if self.talking:
            print(f'{self.name} is already talking.')
            return

        print(f'{self.name} is talking about {topic}.')
        self.talking = True

    def stop_talking(self):
        if not self.talking:
            print(f'{self.name} not talking.')
            return

        print(f'{self.name} stopped talking.')
        self.talking = False

    def eat(self, food):
        if self.eating:
            print(f'{self.name} is already eating.')
            return

        if self.talking:
            print(f'{self.name} You cant eat while talking.')
            return

        print(f'{self.name} is eating {food}.')
        self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating.')
            return

        print(f'{self.name} stopped eating.')
        self.eating = False

    def get_birth_year(self):
        return self.current_year - self.age