def calculadistanciabandapercorre(numerorodadaensaios,numeroshows):
    bia=ana=cadu=edu=fabi=duda=0
    print(numerorodadaensaios)
    print(numeroshows)
    for rota in range(6*numerorodadaensaios):
       if rota%6==0:#casaBia
          bia+=0
          ana+=2
          cadu+=2
          edu+=2
          fabi+=3
          duda+=4
       elif rota%6==1:#casaAna
          bia+=2
          ana+=0
          cadu+=2
          edu+=2
          fabi+=1
          duda+=4
       elif rota%6==2:#casaCadu
          bia+=2
          ana+=2
          cadu+=0
          edu+=2
          fabi+=3
          duda+=2
       elif rota%6==3:#casaEdu
          bia+=2
          ana+=2
          cadu+=2
          edu+=0
          fabi+=1
          duda+=2
       elif rota%6==4:#casaFabi
          bia+=3
          ana+=1
          cadu+=3
          edu+=1
          fabi+=0
          duda+=3
       else:#casaDuda
          bia+=4
          ana+=4
          cadu+=2
          edu+=2
          fabi+=3
          duda+=0
      
    for rotap in range(numeroshows):#P
      bia+=5
      ana+=3
      cadu+=5
      edu+=3
      fabi+=2
      duda+=3
    print('Bia:')
    print(bia)
    print('Ana:')
    print(ana)
    print('Cadu:')
    print(cadu)
    print('Edu:')
    print(edu)
    print('Fabi:')
    print(fabi)
    print('Duda:')
    print(duda)
    totalquarteiroes=bia+ana+cadu+edu+fabi+duda
    final=totalquarteiroes*250*2#ida e volta quantidade de metros por quarteirao
    print('totalquarteiroes:')
    print(totalquarteiroes)
    print('final:')
    print(final)
    return final
pass

