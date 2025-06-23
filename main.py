from consulta import request_get
from crear_card import crear_card
from vista_usuario import vista_usuario
from crear_archivo import crear_archivo

url = 'https://aves.ninjas.cl/api/birds'

datos_pajaros = request_get(url)

cards = crear_card(datos_pajaros)

plantilla = vista_usuario(cards)

crear_archivo(plantilla)