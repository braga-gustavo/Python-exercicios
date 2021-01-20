
salario  = float(input("Informe seu salário: "))
despesas = float(input("Informe sua despesa mensal: "))
percentual_Comprometimento = ( despesas / salario)*100
print(" {0:.1f}% do salário é comprometido com despesas".format(percentual_Comprometimento))
