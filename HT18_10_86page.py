from lib2to3.pgen2.token import MINUS


num = int(input("Сколько температур вы хотите ввести? : "))

just = 0
minus_temp = 0 
while num != just:
    just += 1 
    n = int(input("Введите температуру: ")) 

    if n < 0:
        minus_temp += 1 

print (minus_temp)