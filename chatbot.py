"""
este programa es un chatbot simple que preguntará preguntas determinadas y
podrá dar algunas respuestas
"""
# recibimos un nombre
nombre = input(f"¿cómo te llamas? ")
# recibimos una edad
edad = int(input(f"hola, {nombre} ¿cuantos años tienes? "))
if edad < 40:
    print(f"encantado de conocerte!")
else:
     print(f"...")
# recibimos intereses
hobby = input(f"¿qué te gusta hacer en tu tiempo libre? ")
# recibimos tiempo dedicado a ello
tiempo_hobby = int(input(f"¡qué interesante!¿cuántas horas le dedicas a  {hobby} al día? "))
if tiempo_hobby < 2 :
    print(f"muy bien")
else:
     print("eso son muchas horas...")
print("me alegro de conocerte, byee!")