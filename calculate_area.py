#funcion que calcula el area de un triangulo
def calculate_area(base,altura):
    area = base * altura / 2
    return area

# pido base y altura
altura_input = float(input("introduzca la altura: "))
base_input = float(input("introduzca la base: "))

#guardo el area calculada por la funcion en una variable
area_calculada = calculate_area(base_input,altura_input)  

#imprimo el area calculado
print("el area del triángulo es ", area_calculada)