from Scripts import car

dados = [
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 20
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Familia",
        "idade": 68
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 73
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 20
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 52
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Empresa",
        "idade": 41
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 58
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 8
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Familia",
        "idade": 23
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 12
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 45
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Empresa",
        "idade": 85
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 69
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 36
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Empresa",
        "idade": 25
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 14
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 47
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Familia",
        "idade": 20
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Amigos",
        "idade": 52
    },
    {
        "nome": "ademir",
        "email": "agrj@gmail.com",
        "numero": "85 999 666 333",
        "tag": "Empresa",
        "idade": 85
    }
]



carros = []

def addCarros():
    carro1 = car.Carro('Fiat uno', 'fiat', 'uno', 'red')
    carro2 = car.Carro('Golf', 'wolksvagem', 'golf', 'yellow')
    carro3 = car.Carro('Marea', 'chevrolet', 'marea', 'black')

    carros.append(carro1)
    carros.append(carro2)
    carros.append(carro3)

    return carros

def media(filtro):
    totalIdade = 0
    for dado in dados:
        totalIdade += dado[filtro]
    mediaIdade = int(totalIdade / len(dados))
    return mediaIdade

