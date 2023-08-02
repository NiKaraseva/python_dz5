# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def get_tuple_file(path_file: str) -> tuple:
    *path, extension = path_file.split('\\')
    return ('\\'.join(path),
            extension.split('.')[0],
            extension.split('.')[1])

link = 'C:\desktop\docs\Letter.txt'
print(get_tuple_file(link))
