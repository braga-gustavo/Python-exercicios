"""
    saude = not not sorvete
    Confirmado os 2 = TV 50 + SORVETE
    Confirmando apenas 1 : TV 32 + SORVETE
    NENHUM CONFIMARDO: fica em casa
"""
trabalho_terca = False
trabalho_quinta = True

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca or trabalho_quinta
sorvete = trabalho_terca  or trabalho_quinta
mais_saudavel = not sorvete

print ("TV 50 = {}, TV 32 = {}, Sorvete = {}, Saudável = {}".format(tv_50, tv_32, sorvete, mais_saudavel) )

