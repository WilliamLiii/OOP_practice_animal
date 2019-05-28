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
        return {'food_need':self.food_need, 'water_need':water_need}

    def report(self):
        # return a report of animal status
        return {'name':self._name, 'type':self._type, 'status':self._status, 'weight':self._weight, 'days growing':self._days_growing,'growth rate':self._growth_rate}

    def _update_status(self):

