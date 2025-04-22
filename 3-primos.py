def isPrime(n):
    m = int(n**0.5)
    if n < 2:
        return False
    for i in range(2,m+1):
        if n % i == 0:
            return False
    return True
        
def list_prime(list):
    primes_in_list = []
    for num in list:
        if isPrime(num):
            primes_in_list.append(num)
    return primes_in_list
        
if __name__ == "__main__":
    x = input("Ingrese una lista de numeros separada por espacios: ")
    y = list(map(int,x.split()))
    result = list_prime(y)
    print(result)