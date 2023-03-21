def is_valid(s: str) -> bool:
    # Um dicionário com os brackets e seus respectivos fechamentos
    # como valores
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    stack = []

    for char in s:
        if char in brackets:
            # Se o caractere da iteração atual for encontrado nas
            # chaves do dicionário de brackets ele é adicionado a
            # lista stack.
            stack.append(char)

        # Checa se há stack ou se o último elemento adicionado
        # a stack é diferente do caractere atual, se sim, é
        # retornado False.
        elif not stack or brackets[stack.pop()] != char:
            return False

    # Ao final, se o comprimento de stack for igual a 0, então
    # podemos dizer que todos os brackets são fechados de forma
    # correta, ou seja, a função retornará True.
    return len(stack) == 0


if __name__ == '__main__':
    string = '[()]'
    parenteses = is_valid(string)   
    result = print(parenteses)
