import sys

def get_mean_size(data):
    """
    Рассчитывает средний размер файлов из данных, переданных через результат команды ls -l.

    :param data: строки вывода команды ls -l
    :return: средний размер файла или сообщение, если файлов нет
    """
    lines = data.splitlines()[1:]

    total_size = 0
    file_count = 0

    for line in lines:
        columns = line.split()
        file_size = int(columns[4])
        total_size += file_size
        file_count += 1

    if file_count == 0:
        return "В каталоге нет файлов."

    mean_size = total_size / file_count
    return f"Средний размер файлов: {mean_size:.2f} байт"

if __name__ == "__main__":
    data = sys.stdin.read()
    result = get_mean_size(data)
    print(result)
