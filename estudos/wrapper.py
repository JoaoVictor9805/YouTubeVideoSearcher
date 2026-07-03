def decorator(funcao): #Decorator
    
    def iniciarWrapper(): #Wrapper
        print("iniciando função...")
        funcao()

    return iniciarWrapper

@decorator
def cumprimentar():
    print("olá")

# =======================================================

if __name__ == "__main__":
    cumprimentar()