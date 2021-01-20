# Operadores : "and" e "or"
#print((7 != 3) and (2 > 3))

""" 
    
    #Tabela verdade XOR ("ou exclusivo"):
    True != True = False
    True != False = True
    False != True = True 
    False != False = False

    #Tabela verdade XOR ("ou exclusivo"):
    not true  = false ou not 1 = 0 
    not false = true ou not 0 = 1
    not -1 = 0 
    not not true = true

    CUIDADO!!
    OPERADORES BIT A BIT: 
    & = and
    | = or
    ^ = xor
"""
print(1 != 1)
print(1 != 0 )
print(0 != 1)
print(0 != 0,"\n")

print(not 1)
print(not 0)
print(not -1)
print(not not 0,"\n")

# exercício exemplo
saldo = 1000
salario = 4000
despesas = 3900

saldo_positivo = saldo > 0 
sobra_despesas = salario - despesas >= 0.2* salario
meta = saldo_positivo and sobra_despesas

print (meta)


