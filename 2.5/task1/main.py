import os

def sum_rss(file_path):
    """
    подсчитывает суммарный объем памяти RSS

    :param file_path: путь к файлу
    :return: строка с суммарным объемом памяти
    """
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()[1:]

    total_rss = 0
    for line in lines:
        colums = line.split()
        total_rss += int(colums[5])

    total_rss /= 1024
    return f"{total_rss:.2f}"

if __name__ == "__main__":
    os.system('ps aux > output_file.txt')
    path_to_file = "output_file.txt"
    res = sum_rss(path_to_file)
    print(f"Cуммарное потребление памяти: {res} мб")