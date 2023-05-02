import graphviz


class Chaos:
    def __init__(self, mu, state):
        self.mu = mu
        self.state = state
        self.stabilize()
    
    def stabilize(self):
        for _ in range(1000):
            self.next()
    
    def next(self):
        pass

class LogisticMap(Chaos):
    def __init__(self, mu, state):
        super().__init__(mu, state)
    
    def next(self):
        x = self.state
        self.state = self.mu * x * (1 - x)
        return self.state

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
    dot.render('C:\\Users\\malin\\OneDrive\\Рабочий стол\\Python\\Python\\Practice\\Homework\\PR4\\3\\3_3\\graph', view=True)
    
def visualize(logistic_map):

    # Создаем список значений состояния в зависимости от времени
    state_values = []
    for _ in range(5):
        state_values.append(logistic_map.next())

    # Создаем список вершин графа
    vertices = [(0, str(state_values[0]))]
    vertex_index = {str(state_values[0]): 0}  # словарь для хранения названий вершин и их индексов
    for i in range(1, len(state_values)):
        vertex_name = str(state_values[i])
        if vertex_name not in vertex_index:  # проверяем, есть ли уже такая вершина в графе
            vertex_index[vertex_name] = len(vertices)  # добавляем новую вершину
            vertices.append((len(vertices), vertex_name))
        
    # Создаем список ребер графа
    edges = []
    for i in range(len(state_values)-1):
        from_vertex = vertex_index[str(state_values[i])]
        to_vertex = vertex_index[str(state_values[i+1])]
        edges.append((from_vertex, to_vertex))

    # Рисуем граф
    draw(vertices, edges)


visualize(LogisticMap(3.5, 0.1))