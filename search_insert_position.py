def search_input(nums:list, target:int) -> int:
    left = 0  # Primeiro indice da lista
    right = len(nums) - 1  # Ultimo indice da lista

    while left <= right:  # Enquanto o primeiro indice for menor ou igual ao ultimo
        mid = (left + right) // 2  # Calcula o indice do meio a cada loop

        # Se o indice do meio for igual ao target
        # a busca foi concluida
        if nums[mid] == target:
            return mid

        # Se o indice do meio for menor do que o target
        # o primeiro indice da lista passará a ser o indice do meio mais um
        elif nums[mid] < target:
            left = mid + 1

        # Se o indice do meio for maior do que o target
        # o ultimo indice da lista passará a ser o indice do meio menos um
        else:
            right = mid - 1

    # Se o indice não estiver na lista
    # vai ser retornado o indice em que ele deveria ser encontrado
    return left


if __name__ == '__main__':
    numeros = [1, 3, 5, 6]
    alvo = 4
    resultado = search_input(numeros, alvo)
    print(resultado)
