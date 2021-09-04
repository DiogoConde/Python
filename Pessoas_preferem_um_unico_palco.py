

import math
def retorna_pessoas_preferem_um_unico_palco(quantidade_pessoas_evento):
    AeBeC=3
    AeB=17
    AeC=15
    BeC=7
    soA=45-(AeB+AeC+AeBeC)
    soB=33-(AeB+BeC+AeBeC)
    soC=34-(BeC+AeC+AeBeC)
    multiplicador=(soA+soB+soC)/100
    final=quantidade_pessoas_evento*multiplicador
    print('soA:')
    print(soA)
    print('soB:')
    print(soB)
    print('soC:')
    print(soC)
    print('multiplicador:')
    print(multiplicador)
    return math.floor(final)
pass

