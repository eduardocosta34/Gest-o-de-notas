print("-----Sistema de Gestão de Notas-----")

nome = input('Nome do aluno: ')

def adicionar_notas():
    notas = []
    for i in range(4):
        while True:
            nota = input(f"Digite a nota {i + 1} do aluno (0 a 10): ")
            try:
                nota = float(nota)
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break  # sai do loop se a nota é válida
                else:
                    print("Por favor, insira uma nota válida entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
    
    return notas

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def determinar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def relatorio_final(notas, media, situacao):
    print("\nRelatório Final:")
    print("Notas inseridas:", notas)
    print("Média das notas:", media)
    print(f"Situação do aluno {nome}: {situacao}")

def main():
    notas = adicionar_notas()
    media = calcular_media(notas)
    situacao = determinar_situacao(media)
    relatorio_final(notas, media, situacao)

