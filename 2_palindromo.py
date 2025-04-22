def palindrome(word):
    inverted_word = ""
    for i in range(len(word)-1,-1,-1):
        inverted_word += word[i]
    
    if word == inverted_word:
        return "Es palindromo"
    else:
        return "No es palindromo"
    
if __name__ == "__main__":
    x = input("Ingrese la palabra: ")
    print(palindrome(x))

        