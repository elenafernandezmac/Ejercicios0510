"""
este programa calcula el tiempo que tarda un objeto en caída libre desde una altura dada, con una velocidad inicial dada
"""
# recibo la altura
altura = float(input("inserta la altura del objeto en m: "))
# recibo velocidad_inicial
velocidad_inicial = float(input("inserta la velocidad inicial en m/s: "))
"""
calculo el tiempo segun la formula de la caida libre h=v0t-(1/2)gt^2
altura = -(1/2) * 9.8 * tiempo ** 2
 (- velocidad inicial + √(velocidad inicial² - 4 * (gravedad/2)* (-altura) ) )/ 2 * (gravedad / 2)
"""
tiempo = (-velocidad_inicial + (velocidad_inicial ** 2 -4 * (9.8 / 2) * -(altura))) / 2 * (9.8 / 2)
# damos el resultado al usuario
print("el objeto tocará el suelo en el segundo ", tiempo , " = minuto ", tiempo / 60)