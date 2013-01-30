direccion = raw_input("Dame una direccion ipv4: ")

direccion_lista = direccion.split(".")

print "La parte de red 6to4 correspondiente es: ",
print "2002:%x%x:%x%x" % (int(direccion_lista[0]), int(direccion_lista[1]), int(direccion_lista[2]),int(direccion_lista[3]))
