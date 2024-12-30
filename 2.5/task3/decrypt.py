import sys

def decrypt(encrypted_message):
    """
    Расшифровывает сообщение согласно правилам:
    1. Если после символа стоит одна точка, символ остаётся неизменным, а точка удаляется.
    2. Если после символа стоят две точки, этот символ удаляется, как и обе точки.

    :param encrypted_message: зашифрованная строка
    :return: расшифрованная строка
    """
    stack = []
    i = 0

    while i < len(encrypted_message):
        if i + 1 < len(encrypted_message) and encrypted_message[i + 1] == ".":
            if i + 2 < len(encrypted_message) and encrypted_message[i + 2] == ".":
                if stack:
                    stack.pop()
                i += 3
            else:
                stack.append(encrypted_message[i])
                i += 2
        else:
            stack.append(encrypted_message[i])
            i += 1

    return "".join(stack)

if __name__ == "__main__":
    encrypted_message = sys.stdin.read().strip()
    decrypted_message = decrypt(encrypted_message)
    print(decrypted_message)
