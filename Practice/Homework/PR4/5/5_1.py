import inspect
import importlib

def generate_documentation(module_name):
    # Импортировать модуль
    module = importlib.import_module(module_name)

    # Получить описание модуля
    module_doc = inspect.getdoc(module)

    # Создать заголовок для модуля
    module_title = f'Markdown\n# Модуль {module_name}\n\n{module_doc}\n\n'

    # Создать список для хранения документации на классы
    class_docs = []

    # Получить информацию о классах в модуле
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # Получить описание класса
        class_doc = inspect.getdoc(obj)

        # Создать заголовок для класса
        class_title = f'## Класс {name}\n\n{class_doc}\n'

        # Создать список для хранения документации на методы класса
        method_docs = []

        # Получить информацию о методах класса
        for method_name, method_obj in inspect.getmembers(obj, inspect.isfunction):
            # Пропустить специальные методы, начинающиеся и заканчивающиеся на '__'
            if method_name.startswith('__') and method_name.endswith('__'):
                continue

            # Получить описание метода
            method_doc = inspect.getdoc(method_obj)

            # Получить сигнатуру метода
            signature = inspect.signature(method_obj)
            signature_str = str(signature)

            # Создать строку для документации на метод
            method_str = f'* **Метод** `{method_name}{signature_str}`\n{method_doc}\n'

            # Добавить строку в список методов
            method_docs.append(method_str)

        # Создать строку для документации на класс
        class_str = class_title + '\n'.join(method_docs) + '\n'

        # Добавить строку в список классов
        class_docs.append(class_str)

    # Создать список для хранения документации на функции
    function_docs = []

    # Получить информацию о функциях в модуле
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        # Получить описание функции
        function_doc = inspect.getdoc(obj)

        # Получить сигнатуру функции
        signature = inspect.signature(obj)
        signature_str = str(signature)

        # Создать строку для документации на функцию
        function_str = f'## Функция {name}\n\nСигнатура: `{name}{signature_str}`\n\n{function_doc}\n'

        # Добавить строку в список функций
        function_docs.append(function_str)

    # Создать строку для документации на модуль
    docs_str = module_title + '\n'.join(class_docs) + '\n'.join(function_docs)

    return docs_str

print(generate_documentation("mymodule"))