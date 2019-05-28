class Animal:
    """A generic animal"""
    def __init__(self, food_need, water_need, name):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = 1
        self.food_need = food_need
        self.water_need = water_need
        self._status = 'Baby'
        self._type = 'Generic'
        self._name = name

    def needs(self):
        # return animal grow needs
        return {'food_need':self.food_need, 'water_need':self.water_need}

    def report(self):
        # return a report of animal status
        return {'name':self._name, 'type':self._type, 'status':self._status, 'weight':self._weight, 'days growing':self._days_growing,'growth rate':self._growth_rate}

    def _update_status(self):
        # update animal status based on weight
        if self._weight >= 20:
            self._status = 'Old'
        elif self._weight >= 15:
            self._status = 'Mature'
        elif self._weight >= 10:
            self._status = 'Young'
        elif self.__weight >= 5:
            self._status = 'Baby'

    def grow(self, food, water):
        # grow by given some food and water
        if food >= self.food_need and water >= self.water_need:
            self._weight += self._growth_rate

def main():
    animal_1 = Animal(5, 3, 'Piger')
    print(animal_1.needs())
    print(animal_1.report())
    animal_1.grow(6, 6)
    print(animal_1.report())

if __name__ == '__main__':
    main()
