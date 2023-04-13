import os
import graphviz

def visualize_module_hierarchy(project_path):
    # Получаем список всех файлов и директорий в проекте
    all_files = os.listdir(project_path)

    # Отбираем только файлы с расширением .py
    py_files = [f for f in all_files if f.endswith('.py')]

    # Создаём граф
    dot = graphviz.Digraph(comment='Module Hierarchy')

    # Добавляем все модули в граф
    for py_file in py_files:
        module_name = py_file[:-3]  # убираем расширение .py
        dot.node(module_name, module_name)

    # Добавляем связи между модулями
    for py_file in py_files:
        module_name = py_file[:-3]  # убираем расширение .py
        with open(os.path.join(project_path, py_file), 'r', encoding="utf-8") as f:
            contents = f.read()
            # Ищем импорты в модуле и добавляем связи в граф
            for line in contents.splitlines():
                line = line.strip()
                if line.startswith('import'):
                    imported_module = line.split()[1]
                    dot.edge(imported_module, module_name)
                else:   # Извлекаем import, только если он написан в начале
                    break

    # Рисуем граф и сохраняем его в файл
    dot.format = 'png'
    dot.render('C:\\Users\\Light Flight PC\\OneDrive\\Рабочий стол\\Python\\Python\\Practice\\Homework\\PR4\\5\\module_hierarchy', view=True)

print(visualize_module_hierarchy("C:\\Users\\Light Flight PC\\OneDrive\\Рабочий стол\\Python\\Python\\Practice\\Homework\\PR4\\5"))