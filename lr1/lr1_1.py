import random

class Stek:
    def __init__(self, rozmir):
        self.rozmir = rozmir
        self.stek = []
    
    def pusta(self):
        return len(self.stek) == 0
    
    def kilkist(self):
        return len(self.stek)
    
    def verh(self):
        if not self.pusta():
            return self.stek[-1]
        return None
    
    def dodaty(self, znachennya):
        if self.kilkist() < self.rozmir:
            self.stek.append(znachennya)
        else:
            print("Стек заповнено")
    
    def vydalyty(self):
        if not self.pusta():
            return self.stek.pop()
        else:
            print("Стек порожній")
            return None
    
    def podivytysya(self, indeks):
        if 0 <= indeks < self.kilkist():
            return self.stek[-1 - indeks]
        else:
            return None
    
    def povnyj(self):
        return self.kilkist() == self.rozmir
    
    def pusta(self):
        return len(self.stek) == 0

rozmir_steka = 13 * 5 + 50

stek = Stek(rozmir_steka)
for _ in range(rozmir_steka):
    zn = random.randint(1, 1000)
    stek.dodaty(zn)

parni_stek = Stek(rozmir_steka)
ne_stek = Stek(rozmir_steka)

while not stek.pusta():
    znach = stek.vydalyty()
    if znach % 2 == 0:
        parni_stek .dodaty(znach)
    else:
        ne_stek.dodaty(znach)

def printspysok(s):
    spysok = []
    while not s.pusta():
        spysok.append(s.vydalyty())
    print(spysok)

print("Парні")
printspysok(parni_stek)

print("Непарні:")
printspysok(ne_stek)
