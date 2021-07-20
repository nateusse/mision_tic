# programa capacidad de endeudamiento
#

puntaje = int(input("Por favor digite el puntaje del usuario:"))



def capacidad_endeudamiento(puntaje):
    h = (puntaje*2)-4
    if puntaje >= 0 and puntaje <= 20:
        print (puntaje, h)



capacidad_endeudamiento(30)
