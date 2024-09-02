def is_fibonacci(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return f"{num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"{num} não pertence à sequência de Fibonacci."


numero = 21  
print(is_fibonacci(numero))


def count_a_in_string(s):
    count = s.lower().count('a')
    return f"A letra 'a' ocorre {count} vezes na string."


string = "Abracadabra"
print(count_a_in_string(string))


INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)  


# a) 1, 3, 5, 7, ___
seq_a = [1, 3, 5, 7]
next_a = seq_a[-1] + 2
print(f"Próximo elemento da sequência a): {next_a}")

# b) 2, 4, 8, 16, 32, 64, ____
seq_b = [2, 4, 8, 16, 32, 64]
next_b = seq_b[-1] * 2
print(f"Próximo elemento da sequência b): {next_b}")

# c) 0, 1, 4, 9, 16, 25, 36, ____
seq_c = [0, 1, 4, 9, 16, 25, 36]
next_c = (len(seq_c)) ** 2
print(f"Próximo elemento da sequência c): {next_c}")

# d) 4, 16, 36, 64, ____
seq_d = [4, 16, 36, 64]
next_d = (len(seq_d) + 2) ** 2
print(f"Próximo elemento da sequência d): {next_d}")

# e) 1, 1, 2, 3, 5, 8, ____
seq_e = [1, 1, 2, 3, 5, 8]
next_e = seq_e[-1] + seq_e[-2]
print(f"Próximo elemento da sequência e): {next_e}")

# f) 2, 10, 12, 16, 17, 18, 19, ____
seq_f = [2, 10, 12, 16, 17, 18, 19]
next_f = seq_f[-1] + 1
print(f"Próximo elemento da sequência f): {next_f}")


lampada1 = {"estado": "apagada", "temperatura": "fria"}
lampada2 = {"estado": "apagada", "temperatura": "fria"}
lampada3 = {"estado": "apagada", "temperatura": "fria"}


def identificar_lampadas():
    lampada1["estado"] = "acesa"

    lampada1["temperatura"] = "quente"

    lampada1["estado"] = "apagada"
    lampada2["estado"] = "acesa"


    if lampada1["estado"] == "apagada" and lampada1["temperatura"] == "quente":
        lampada_correspondente_ao_primeiro_interruptor = "lampada1"
    if lampada2["estado"] == "acesa":
        lampada_correspondente_ao_segundo_interruptor = "lampada2"
    if lampada3["estado"] == "apagada" and lampada3["temperatura"] == "fria":
        lampada_correspondente_ao_terceiro_interruptor = "lampada3"

    return (lampada_correspondente_ao_primeiro_interruptor, 
            lampada_correspondente_ao_segundo_interruptor, 
            lampada_correspondente_ao_terceiro_interruptor)

resultado = identificar_lampadas()

print(f"O primeiro interruptor controla a {resultado[0]}")
print(f"O segundo interruptor controla a {resultado[1]}")
print(f"O terceiro interruptor controla a {resultado[2]}")
