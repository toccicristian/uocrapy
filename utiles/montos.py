def validar (monto):
    try:
        float(monto)
        return True

    except ValueError:
        return False
