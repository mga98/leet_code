def is_palindrome(x: int) -> bool:
    # Cria uma lista para armazenar o número em forma de string.
    num_list = []

    for i in str(x):
        # Transforma cada unidade do número em str e itera sobre o mesmo
        # adicionando-o a lista num_list.
        num_list.append(i)

    # Compara o número invertido da lista ao número normal e returna
    # True ou False caso seja ou não um palindromo.
    return num_list[::-1] == num_list
