def tamanho_setor_busca(areamaior,areamenor):
    diferenca=areamaior-areamenor
    secao=diferenca/8
    intsecao=int(secao)
    if intsecao==secao:
      secao=intsecao
    secaofinal=str(secao)
    return secaofinal
pass

