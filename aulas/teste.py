carros={
    "Carro1":{
        "Fabricante": "Volkswagem",
        "Modelo": "Gol" 
    },
    "Carro2":{
        "Fabricante": "Ford",
        "Modelo": "Focus"
    },
    "Carro3":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    }
}
#para acessar e como se force uma matriz
print(carros)
print(carros["Carro1"])
print(carros["Carro2"]["Fabricante"])
print(carros["Carro3"]["Modelo"])