import math
def retorna_tempo_arena_em_milisegundos(distancia,velocidade):
    dist=float(distancia)
    tempo=1000*(dist*1000/velocidade)
    time=int(tempo)
    if tempo-time>0.5:
      time=time+1
    print ('time:')
    print (time)
    print ('tempo:')
    print (tempo)
    print(math.ceil(tempo))
    return time
pass

