def digitver(cuit_sin_dv=str()):
    dverif=0
    for dcuit,dserie in zip( (cuit_sin_dv[0:2]+cuit_sin_dv[2::1].zfill(8)), [5,4,3,2,7,6,5,4,3,2]):
        dverif+=(int(dcuit)*int(dserie))
    dverif = 11 - dverif % 11
    if dverif == 11:
        return '0'
    if dverif == 10:
        return '9'
    return f'{dverif}'


def escuil(cuil=str()):
    if len(cuil)!=11 or f'{cuil[0:2]}' not in ['20','23','24','27'] or f'{cuil[-1]}' != digitver(str(cuit)[:-1]):
        return False
