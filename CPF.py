import random
from region import Region
class CPF:
    def __init__(self):
        self.cpf = "XXX.XXX.XXX-XX"
        i = 0
        intermediate = []
        for x in self.cpf[:10]:
            if x == "X":
                intermediate.append(x.replace("X",str(random.randint(0,9))))
            else:
                intermediate.append(x)

        self.cpf = "".join(intermediate)
    def linking_reg(self, accurate):
        reg = Region()
        accurate = reg.get_states_in().get(accurate.upper())
        return accurate
    def emission_reg(self, calc_reg):
        self.cpf += calc_reg
        return self.cpf
    def update_cpf(self, updated):
        self.cpf = updated
        decrement1 = 10
        decrement2 = 11
        acumulate1 = 0
        acumulate2 = 0
        for i, x in enumerate(self.cpf):
            if self.cpf[i].isdigit():
                acumulate1 += int(x) * decrement1
                decrement1 -= 1
        if acumulate1 % 11 == 0 or acumulate1 == 1:
            verificator1 = "0"
        else:
            verificator1 = str( 11 - (acumulate1 % 11))
            if int(verificator1) >= 10:
                verificator1 = "0"
        self.cpf += "-" + verificator1

        for i, x in enumerate(self.cpf):
            if x.isdigit():
                    acumulate2 += int(x) * decrement2
                    decrement2 -= 1
        if acumulate2 % 11 == 0 or acumulate2 == 1:
            verificator2 = "0"
        else:
            verificator2 = str( 11 - (acumulate2 % 11))
            if int(verificator2) >= 10:
                    verificator2 = "0"


        self.cpf += verificator2
    def get_cpf(self):
        return self.cpf
