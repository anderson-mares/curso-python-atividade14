# importando o módulo
from equacoes import *

# programa principal
if __name__ == "__main__":
    while True:
        print("0 - Sair do programa")
        print("1 - Calcular Equação do 1º grau")
        print("2 - Calcular Equação do 2º grau")

        opcao = int(input("Digite a opção desejada: "))

        match opcao:
            case 0:
                break
            case 1:
                try:
                    a = float(input("Informe o valor de a: ").replace(",", "."))
                    b = float(input("Informe o valor de b: ").replace(",", "."))
                    print(f"O valor de x é: {primeiro_grau(a, b)}.")
                except Exception as e:
                    print(f"Não foi possível calcular a equação do 1º grau. {e}")
                finally:
                    continue
            case 2:
                try:
                    a = float(input("Informe o valor de a: ").replace(",", "."))
                    b = float(input("Informe o valor de b: ").replace(",", "."))
                    c = float(input("Informe o valor de c: ").replace(",", "."))

                    # armazenar os valores da função em uma lista
                    resultados = segundo_grau(a, b, c)

                    # imprime os resultados na tela
                    for resultado in resultados:
                        print(resultado)
                except Exception as e:
                    print(f"Não foi possível calcular a equação do 2º grau. {e}") 
                finally:
                    continue
            case _:
                print("Opção inválida.")
                continue
