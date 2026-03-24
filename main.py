from person import Person
from region import Region
from CPF import CPF
import time
name = input("What is your full name? ")
age = int(input("How old are you? "))
you = Person(name, age)
reg = Region()
print(f"Full name: {you.get_name()}\nAge old: {you.get_age()}")
state_flag = 0
state = ""
while state_flag == 0:
    state = input("Which state of Brazil from Emissor? For Example São Paulo >> SP:\n")
    result = reg.validation(state)
    state_flag = result
    if result == 0:
        print("Try again")

identification = CPF()
calc_cpf = identification.linking_reg(state)
update1 = identification.emission_reg(calc_cpf)
identification.update_cpf(update1)
print("Validation", end="")
for x in range(5):
    print('.', end="")
    time.sleep(1)
print(f"\nYour CPF: {identification.get_cpf()}")