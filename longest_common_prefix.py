def longest_common_prefix(strs: list) -> str:
    prefix = ''

    # Usa o zip() para adicionar em uma tupla as primeiras letras de cada palavra.
    for letter in zip(*strs):

        # Usa o set() para cada tupla, afim de remover os elementos duplicados, e
        # então verifica se o tamanho da tupla é igual a 1.
        if len(set(letter)) == 1:
            # Se for igual a 1, quer dizer que todas as letras daquela tupla são
            # iguais, assim é adicionada a letra a string prefix.
            prefix += letter[0]

        else:
            # Caso o tamanho seja diferente de 1, é retornado a string como está
            # até o momento da atual iteração.
            return prefix

    # Se nenhuma letra for adicionada a string prefix, então ela é retornada vazia.
    return prefix


if __name__ == '__main__':
    words = ['flower', 'flow', 'flight']
    result = longest_common_prefix(words)
    print(result)
