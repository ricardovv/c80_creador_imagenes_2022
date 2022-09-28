### - - - - - - - - - - - - - - - - - - 
### DATOS EXTERNOS 
### - - - - - - - - - - - - - - - - - - 


### - - - - - - - - - - - - - - - - - - 
### importamos el archivo
archivo = "datos_iconos_01.csv"
with open( archivo, encoding='utf-8' ) as f:
    datosBruto = f.readlines()
#print(datosBruto)


### - - - - - - - - - - - - - - - - - - 
### Creamos istas para guardar los datos
lista_titulo = []
lista_texto  = []
lista_imagen = []


### - - - - - - - - - - - - - - - - - - 
### Seleccionar filas columnas, guardarlas en sus listas 
for linea in datosBruto[1:]:	
	s = linea[0:len(linea)]
	datos = s.split(",")
	#selecciona que ele,ento de cada fila
	titulo = datos[0]
	texto  = datos[1]
	imagen = datos[2]
	
	## los agrega en cada lista
	lista_titulo.append(titulo)
	lista_texto.append(texto)
	lista_imagen.append(imagen)

    
### - - - - - - - - - - - - - - - - - - 
### ciclo para mostrar que se leen los elementos   
for i in range( len(lista_titulo) ):
    pass
#    print(	lista_titulo[i], lista_texto[i], lista_imagen[i] )
    print(	lista_imagen[i]  )


### - - - - - - - - - - - - - - - - - - 
### DIBUJA
### - - - - - - - - - - - - - - - - - - 
## ciclo for del msmo largo que total de filas
for i in range( len(lista_titulo) ):
    newPage(400, 400) # crea ua nueva pagina
    # caja color
    fill(0,.3,.9)
    rect(10, 10, 380, 380)

    # imagen
    ## ojo en rutaimg.strip() se usa strip para rmover el salto de linea 
    rutaimg = lista_imagen[i]
    image( rutaimg.strip(), (20, 80) ) 

    # titulo1
    fill( .0, .8, .0)
    fontSize(30)
    text( lista_titulo[i], (50, 250) )

    # texto
    fill( .8, .8, .0)
    fontSize(20)
    textBox(lista_texto[i], (50, 30, 220, 50) )
    
    
### - - - - - - - - - - - - - - - - - - 
### GUARDAR
### - - - - - - - - - - - - - - - - - - 
## Guarda un archivo con todas la simagenes, luego se pueden separar
saveImage('salvar/imagenes.pdf') 

