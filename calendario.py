from calendar import weekday

fecha = raw_input("Introduce tu fecha de nacimiento (DD-MM-YYYY): ")

lista_fecha = fecha.split("-")

semana = ["lunes", "martes","miercoles","jueves","viernes","sabado","domingo"]

diadelasemana = weekday(int(lista_fecha[2]), int(lista_fecha[1]), int(lista_fecha[0]))

print "Naciste en %s" % semana[diadelasemana]
