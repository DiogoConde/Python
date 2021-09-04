import math 
def retorna_tempo_minimo_em_minutos(p,s,n):
  print('p:')
  print(p)
  print('s:')
  print(s)
  print('n:')
  print(n)
  tempo1portao=p*s
  temporeal=tempo1portao/n
  temporeal=math.ceil(temporeal)
  print('temporeal')
  print(temporeal)
  inttemporeal=int(temporeal)
  print('inttemporeal:')
  print(inttemporeal)
  if inttemporeal<temporeal:
    temporeal=math.ceil(temporeal)
  tempomin=temporeal/60
  print('tempo1portao:')
  print(tempo1portao)
  print('temporeal')
  print(temporeal)
  print('tempomin:')
  print(tempomin)
  print('ceiltempomin:')
  print(math.ceil(tempomin))
  return math.ceil(tempomin)
pass