import graphviz

def draw(vertices, edges):
    dot = graphviz.Digraph()
    
    # Добавляем вершины
    for vertex in vertices:
        dot.node(str(vertex[0]), vertex[1])
        
    # Добавляем рёбра
    for edge in edges:
        dot.edge(str(edge[0]), str(edge[1]))
    
    # Рисуем граф и сохраняем его в файл
    dot.format = 'png'
    dot.render('C:\\Users\\malin\\OneDrive\\Рабочий стол\\Python\\Python\\Practice\\Homework\\PR4\\3\\3_1\\graph', view=True)

draw([(1, 'v1'), (2, 'v2')], [(1, 2), (2, 3), (2, 2)])