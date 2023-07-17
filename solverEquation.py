
def checkIncognito(valor):
    try:
        float(valor)
        return False
    except:
        return True
