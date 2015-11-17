__author__ = 'Sawl_Stone'


#PhoneStation


class Tarif:
    def __init__(self, name, price, internet):
        self.name = name
        self.price = price
        self.internet = internet

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def setInternet(self, internet):
        self.internet = internet

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getInternet(self):
        return self.internet

class Client:
    def __init__(self, phoneNumber, clientName, tarif):
        self.phone = phoneNumber
        self.clientName = clientName
        self.tarif = tarif
        self.rest = 0

    def changeTarif(self, tarif):
        self.tarif = tarif

    def showTarif(self):
        return self.tarif

    def putMoney(self, money):
        self.rest = money

    def phone(self, minutes):
        totalSum = minutes * self.tarif.price
        self.rest -= totalSum


class Company:
    def __init__(self):
        self.listTarifs = []
        self.listClients = []

    def showTarifs(self):
        return self.listTarifs

    def addTarif(self, tarif):
        self.listTarifs.append(tarif)

    def removeTarif(self, tarif):
        self.listTarifs.remove(tarif)

    def addClient(self, client):
        self.listClients.append(client)

    def removeClient(self, client):
        self.listClients.remove(client)

    def sortTarifsByPrice(self):
        for i in range(0, len(self.listTarifs)):
            for j in range(i+1, len(self.listTarifs)):
                if(self.listTarifs[i].price > self.listTarifs[j].price):
                    self.listTarifs[i], self.listTarifs[j] = self.listTarifs[j], self.listTarifs[i]


def main():
    tarif1 = Tarif("Good", 1.2, 100)
    tarif2 = Tarif("Exellent", 1.1, 90)

    client1 = Client("111222333", "Vasya", tarif1)
    client2 = Client("333444555", "Petya", tarif2)
    client3 = Client("555666777", "Kolya", tarif1)

    comp = Company()

    comp.addTarif(tarif1)
    comp.addTarif(tarif2)

    comp.addClient(client1)
    comp.addClient(client2)
    comp.addClient(client3)
    comp.sortTarifsByPrice()
    tarifs = comp.showTarifs()
    for tarif in tarifs:
        print(tarif.price)

main()