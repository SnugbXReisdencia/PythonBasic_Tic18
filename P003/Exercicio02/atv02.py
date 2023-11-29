

lista_empregados = []
with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(",")
        empregado = {
            "nome": dados[0],
            "sobrenome": dados[1],
            "ano_nascimento": int(dados[2]),
            "RG": dados[3],
            "ano_admissao": int(dados[4]),
            "salario": float(dados[5])
        }
        lista_empregados.append(empregado)
    
def Reajusta_dez_porcento(empregados):
    for empregado in empregados:
        empregado["salario"] *= 1.1




for empregado in lista_empregados:
    print(empregado)

if __name__ == "__main__":
    lista_empregados = []
    with open("arquivo.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            empregado = {"nome": dados[0], "sobrenome": dados[1], "ano_nascimento": dados[2], "RG": dados[3], "ano_admissao": dados[4], "salario": float(dados[5])}
            lista_empregados.append(empregado)
    
    Reajusta_dez_porcento(lista_empregados)

    print("\n Lista de Empregados Atualizada Após Reajuste:\n") 
    for empregado in lista_empregados:
        print(empregado)



# lista_empregados = [
#     {
#         'nome': 'João',
#         'sobrenome': 'Silva',
#         'ano_nascimento': 1990,
#         'RG': '123456',
#         'ano_admissao': 2010,
#         'salario': 5000
#     },
#     {
#         'nome': 'Maria',
#         'sobrenome': 'Souza',
#         'ano_nascimento': 1985,
#         'RG': '654321',
#         'ano_admissao': 2008,
#         'salario': 6000
#     }
# ]

# # Salvar a lista em um arquivo
# with open("arquivo.txt", "w") as arquivo:
#     for empregado in lista_empregados:
#         linha = f"{empregado['nome']},{empregado['sobrenome']},{empregado['ano_nascimento']},{empregado['RG']},{empregado['ano_admissao']},{empregado['salario']}\n"
#         arquivo.write(linha)        