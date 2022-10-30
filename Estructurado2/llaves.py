def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave} : {valor}')


listarTerminos(IDE='integraded developement enviromen',PK='Primary Key')
listarTerminos(DBS='Date Base')