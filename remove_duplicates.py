def remove_duplicates(nums: list) -> int:
    j = 0

    # Cria um FOR que utiliza dois indices, um começando por 0
    # e outro começando com 1.
    for i in range(1, len(nums)):
        # Se o elemento de indice anterior for diferente do elemento
        # de indice posterior:
        if nums[i] != nums[j]:
            # Adiciona 1 a váriavel de indice j.
            j += 1
            # E iguala o elemento do indice anterior (j) ao elemento
            # de indice posterior (i), 'jogando' os elementos duplicados
            # para o fim da lista.
            nums[j] = nums[i]

    # Ao final retorna j + 1 que é o comprimento da lista sem os números
    # duplicados.
    return j + 1


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 4]
    remove = remove_duplicates(nums)
    print(remove)
