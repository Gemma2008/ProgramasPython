def perimetro(radio):
    p = 2*3.14*radio
    return(p)
def area(radio):
    a = 3.14*radio*radio
    return(a)
radio = int(input("Dime el radio"))
print ("El perimetro es: ",perimetro(radio), "El area es: ", area(radio))
