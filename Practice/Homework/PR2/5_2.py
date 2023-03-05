import sys

def my_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    """Моя версия функции print"""
    # Преобразуем все аргументы в строки
    arg_strings = [str(arg) for arg in args]
    # Объединяем аргументы с помощью разделителя
    output = sep.join(arg_strings)
    # Добавляем символ окончания строки
    output += end
    # Записываем строку в файл вывода
    file.write(output)
    # Если нужно, сбрасываем буфер вывода
    if flush:
        file.flush()
        
my_print("Hello", "world", "!")
my_print("The answer is", 42, sep='')
my_print("This is a test", end="", flush=True)