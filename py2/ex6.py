# EX6
# Crie uma função que recebe um valor
# e imprime "É número!" se for int, float ou complex.
def verificar_numero(valor):
    if isinstance(valor, (int, float, complex)):
        print ("É número")
    else:
       print("Não é número")
verificar_numero(5)
verificar_numero("texto")
