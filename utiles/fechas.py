def bisiesto(aaaa=int()):
    if (aaaa%4 == 0 and aaaa % 100 != 0) or aaaa % 400 == 0:
        return True
    return False


def es_dia(aaaammdd=str()):
    aaaa = int(aaaammdd[0:4])
    mes  = int(aaaammdd[4:6])
    dia  = int(aaaammdd[6:8])
    print(f'{dia}/{mes}/{aaaa}')
    if ( ((mes%2==0 and mes>7) or (mes%2!=0 and mes<8)) and dia>31 ) or ( ((mes%2!=0 and mes>7) or (mes%2==0 and mes<7 and mes!=2)) and dia>30 ) :
        return False
    if mes == 2:
        if bisiesto(aaaa):
            if dia>29:
                return False
        if dia > 28:
            return False
    return True




def valida(fecha=str()):
    if len(fecha)!=8 or int(fecha[4:6])>12 or int(fecha[4:6])<1 or not es_dia(fecha):
        return False
    return True
