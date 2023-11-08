file = open('song_codec.txt', 'r') #abrimos el archivo con la cancion normal, en modo lectura
fileCiphered = open('songCiphered.txt', 'w') #abrimos un archivo donde guardaremos la letra cifrada, en modo escritura
fileCodec = open('codecSong.txt', 'w') #en este archivo se guarda la cancion decodificada
character = file.read(1) #empezamos a leer el archivo original caracter por caracter


List = [] #declaramos una lista vacia que contendra los caracteres sin cifrar
ListCiphered = [] #una segunda lista donde guardaremos los caracteres cifrados
contador = 0 #inicializamos una variable contador iniciando desde 0

while character != "": #ciclo while que recorre el archivo original hasta que se llegue a su fin
    List.append(character) #almacenamos el caracter en la lista
    character = file.read(1)
    asciichar = ord(List[contador]) #convertimos el caracter en su forma ascii
    if(asciichar >= 97 and asciichar <= 122): #evaluamos si es una letra minuscula
        if(asciichar == 122): #evaluamos si es z
            asciichar = 97
            letra = chr(asciichar) #reconvertimos el ascii a caracter
            ListCiphered.append(letra) #almacenamos en la lista cifrada
        else:
            asciichar = asciichar+1 #sumamos 1 al ascii para cambiar a la letra que le sigue
            letra = chr(asciichar)
            ListCiphered.append(letra)
    else:
        letra = chr(asciichar)# si es mayuscula o simbnolo, no se hace nada
        ListCiphered.append(letra)#append a la lista cifrada
    contador = contador + 1 #incrementamos el contador para pasar al siguiente caracter

fileCiphered.write("".join(ListCiphered))#almacenamos el contenido de la lista en el archivo cifrado
print(List)

print(ListCiphered)
fileCiphered.close()#cerramos el archivo cifrado

fileCipheredRead = open('songCiphered.txt', 'r') #abrimos el archivo cifrado en modo lectura
characterCiphered = fileCipheredRead.read(1)
List = [] #re inicializamos las variables y listas desde 0
ListCodec = []
contador = 0

while characterCiphered != "": #repetimos el proceso, pero esta vez restamos al ascii en vez de sumar 1
    List.append(characterCiphered)
    characterCiphered = fileCipheredRead.read(1)
    asciichar = ord(List[contador])
    if(asciichar >= 97 and asciichar <= 122): #evaluamos si es a, si es a, se vuelve z
        if(asciichar == 97):
            asciichar = 122
            letra = chr(asciichar)
            ListCodec.append(letra)
        else:
            asciichar = asciichar-1
            letra = chr(asciichar)
            ListCodec.append(letra)
    else:
        letra = chr(asciichar)
        ListCodec.append(letra)
    contador = contador + 1
fileCodec.write("".join(ListCodec))#Guardamos la lista con los caracteres decodificados en el archivo final

fileCipheredRead.close()#cerramos los archivos restantes
fileCodec.close()
file.close()
