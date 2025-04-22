def max_sum_consecutive(nums):
    if len(nums) < 2:
        return "No hay suficientes elementos"
    
    max_sum = nums[0] + nums[1]
    
    for i in range(1, len(nums)-1):
        current_sum = nums[i] + nums[i+1]
        if current_sum > max_sum:
            max_sum = current_sum
        
    return max_sum

if __name__ == "__main__":
    x = input("Ingrese una lista de numeros separada por espacios: ")
    y = list(map(int,x.split()))
    result = max_sum_consecutive(y)
    print(result)
    