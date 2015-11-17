__author__ = 'Sawl_Stone'

class Vegetables:
    def __init__(self, name, veg_price_kg, cal):
        self.name = name
        self.veg_price_kg = veg_price_kg
        self.cal = cal

    def getVegName(self):
        return self.name

    def getPrice_gr(self):
        return self.veg_price_kg

    def getVegCal(self):
        return self.cal

class Sous:
    def __init__(self, name, sous_prise_kg, cal):
        self.name = name
        self.sous_prise_kg = sous_prise_kg
        self.cal = cal

    def getSousName(self):
        return self.name

    def getSousPrice(self):
        return self.sous_prise_kg

    def getSousCal(self):
        return self.cal

class Salad(Vegetables, Sous):
    def __init__(self, name):
        self.sal_name = name
        self.listIngridients = []
        self.listPrice = []
        self.listCal = []

    def addIngridients(self, ingridients):
        self.listIngridients.append(ingridients)

    def showIngridients(self):
        return self.listIngridients

    def salad_cal(self):
        pass

    def addCal(self, cal):
        self.listCal.append(cal)

    def addPrice(self, price):
        self.listPrice.append(price_kg)
        return self.listPrice
    

def main():
    Pomidor = Vegetables("Pomidor", 50, 20)
    Ogurec = Vegetables("Ogurec", 30, 15)
    Kapusta = Vegetables("Kapusta", 20, 10)

    Smetatna = Sous("Smetana", 30, 50)
    Oil = Sous("Oil", 25, 35)
    Maionez = Sous("Maionez", 15, 55)

    Salad_ovoshnoy = Salad("Ovoshnoy")
    Salad_ovoshnoy.addIngridients(Pomidor)
    Salad_ovoshnoy.addIngridients(Ogurec)
    Salad_ovoshnoy.addIngridients(Kapusta)
    Salad_ovoshnoy.addIngridients(Oil)
    ingrid = Salad_ovoshnoy.showIngridients()
    print("Salad Name", Salad_ovoshnoy.sal_name)
    for ing in ingrid:
        #sum_cal = sum(ing.cal)
        print(ing.name, ing.cal)
    #sum_cal = Pomidor.cal+Ogurec.cal+Kapusta.cal
    print(Salad_ovoshnoy.salad_cal())

main()