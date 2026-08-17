print("Digite um número: ")
i = int(input())

if i:
    print("TABUADA DO " + str(i) + ":")
    print(i, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10)
else:
    raise ValueError("Erro: número informado é nulo.")
    