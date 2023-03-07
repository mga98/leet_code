def two_sum(nums: list, target: int) -> list:
    values = {}  # Armazena os valores

    for i, elem in enumerate(nums):
        # Cria uma variável comp (complementar) que faz a subtração
        # do target pelo atual elemento sendo iterado na lista de 
        # números.
        comp = target - elem

        if comp in values:
            # Se o resultado da subtração (comp) estiver no dicionário
            # values, então o resultado da faunção é o atual indice da
            # iteração "i" e o indice armazenado no dicinionário values.
            return [values[comp], i]

        # Caso o resultado da subtração (comp) não seja encontrado no
        # dicionário values, então o atual indice é adicionado ao dicionário
        # como o valor da chave do atual elemento.
        values[elem] = i

    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(result)
