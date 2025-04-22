def calculate(num1: int,num2: int,operation: str):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! No se puede dividir entre 0"
    else:
        return "Operador no valido"

if __name__ == "__main__":
    x = float(input("ingrese el primer numero: "))
    y = float(input("ingrese el segundo numero: "))
    z = input("ingrese la operacion que desea realizar(solo el simbolo +, -, *, /): ")
    result = calculate(x, y, z)
    print(result)
    