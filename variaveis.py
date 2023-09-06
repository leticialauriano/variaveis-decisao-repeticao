nome=input("Digite um funcionário: ")
empresa=input("Digite a instituição: ")
qtde_funcionarios=int(input("Digite a qtde de funcionários: "))
mediaMensalidade=float(input("Digite a média da mensalidade: "))
print(nome+ " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.") # Concatenação string com string
print("A média da mensalidade é de: " + str(mediaMensalidade)) # Concatenação string com número. str = converter para string

print("==============Verifique os tipos de dados abaixo:==============") # Como verificar os tipos de variáveis
print("O tipo de dado da variavel [nome] é: ",type(nome))
print("O tipo de dado da variavel [empresa] é: ",type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ",type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ",type(mediaMensalidade))

# Variáveis são espaços em memória, que vão guardar os dados fornecidos pelo usuário.
# Cada variável é identificada por um identificador próprio, que precisa iniciar com letra sempre minúsculo, não pode iniciar com número. 
# Cuidado com caracteres especiais. Único que pode é o _.
# 3 tipos de dados que iremos usar são: strings, int, float.