def q1(limite, numero):  # Limite para quantos números terá na lista, número é para verificar se ele aparece na sequência
    sequencia = [0, 1]
    for i in range(2, limite):
        prox = sequencia[i - 1] + sequencia[i - 2]
        sequencia.append(prox)

    for j in sequencia:
        if j == numero:
            return print(f"{sequencia}\n{numero} está na sequência")

    return print(f"{sequencia}\n{numero} não está na sequência")

def q2(s):
    if isinstance(s, str) and s.isalpha(): #Verificar se é caracter válido

        contador = {
            "a": 0, "A": 0
        }

        for char in s:
            if char in contador:
                contador[char] += 1

        total = contador["a"] + contador["A"]


        if total > 0:
            return print(f"'{s}' contém o total de : {total} letras A ou a")


    else:
        return print(f"'{s}' Porfavor insira penas letras em STRING nos parâmetros")



q1(11, 7)
q2("ABaCAXI")



