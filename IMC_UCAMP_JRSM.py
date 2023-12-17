#Ingreso de datos

nombre = input("Ingrese su nombre: ")
while nombre == "":
    nombre = input("Nombre invalido. Ingrese su nombre: ")

apellido_p = input("Ingrese su apellido paterno: ")    
while apellido_p == "":
   apellido_p = input("Apellido inválido. Ingrese su apellido paterno: ")
   
apellido_m = input("Ingrese su apellido materno: ")
while apellido_m == "":
   apellido_m = input("Apellido inválido. Ingrese su apellido materno: ")
   
edad = 0   
while edad == 0:
   try:
      edad = int(input("Ingrese su edad (solo números): ")) 
   except:
      print("Debe ingresar un número válido")

peso = 0
while peso == 0:
   try:
      peso = float(input("Ingrese su peso (kg) (solo números): "))
   except:
      print("Debe ingresar un número válido") 

estatura = 0   
while estatura == 0:
   try:
      estatura = float(input("Ingrese su estatura (m) (solo números): "))
   except:
      print("Debe ingresar un número válido")
#aquí calculamos el Indice de Masa Corporal      
imc = peso / estatura**2
#Aquí imprimimos los datos ingresados
#Comparamos con datos reconocidos de Categoría de Peso

print(f"\nNombre: {nombre} {apellido_p} {apellido_m}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")  
#La Variable feedback define la categoría de peso
if imc < 18.5:
   feedback = "usted esta en BAJO PESO"
elif 18.5 <= imc < 25: 
   feedback = "usted tiene PESO NORMAL"
elif 25 <= imc < 30:
   feedback = "usted tiene SOBREPESO"
else:
   feedback = "usted tiene OBESIDAD"
#Se imprime la categoría de peso que corresponde   
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}") 
print(feedback)
print ("Has finalizado la ejecución")
input ()
