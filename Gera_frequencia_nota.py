def retorna_frequencia_nota(semitons):
    freq=440*pow(2,semitons/12)
    print(freq)
    frequencia= round(freq, 4)
    freq2=int(freq)
    print(frequencia)
    print(freq2)
    if freq2==frequencia:
      frequencia2=str(freq2)
    else:
      frequencia2=(f'{frequencia:.4f}')
    if semitons%12==0:#A
      nota='A'
    elif semitons%12==1:#A#
        if semitons<0:#bemol
          nota='Bb'
        else:#sustenido
          nota='A#'
    elif semitons%12==2:#B
      nota='B'
    elif semitons%12==3:#C
         nota='C'
    elif semitons%12==4:#C#
        if semitons<0:#bemol
           nota='Db'
        else:#sustenido
           nota='C#'
    elif semitons%12==5:#D
         nota='D'
    elif semitons%12==6:#D#
        if semitons<0:#bemol
           nota='Eb'
        else:#sustenido
           nota='D#'
    elif semitons%12==7:#E
         nota='E'
    elif semitons%12==8:#F
         nota='F'
    elif semitons%12==9:#F#
      if semitons<0:#bemol
         nota='Gb'
      else:#sustenido
         nota='F#'
    elif semitons%12==10:#G
         nota='G'
    else:#G#
      if semitons<0:#bemol
         nota='Ab'
      else:#sustenido
         nota='G#'
    return[frequencia2, nota]    
pass

