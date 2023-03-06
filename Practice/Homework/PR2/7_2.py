import graphviz


class Room:
    def __init__(self, name, list):
        self.name = name  # Имя комнаты
        self.description = 'Вы находитесь в комнате №' + str(name)  # Описание комнаты
        self.list = list  # Список с направлениями к соседним комнатам
    
    def print_info(self):
        print(f'Комната №{self.name}', end='\n\n')  # Выводит номер комнаты на экран
        print(self.description, sep='', end='\n\n')  # Выводит описание комнаты на экран
        
class Game:
    def __init__(self):
        self.room_list = self.create_game()  # Создание списка комнат
            
    # Переход в комнату
    def run(self, id):
        if id == 0:
            print('Вы выбрались!!!')
            return Room('0', [])  # Возвращаем объект класса Room для выхода из игры
        return self.room_list[id - 1]  # Возвращаем объект класса Room для следующей комнаты
    
    # Создание комнат
    def create_game(self):
        return [
            Room('1', {2:'запад', 3:'юг', 4:'восток'}),
            Room('2', {5:'юг', 1:'восток'}),
            Room('3', {1:'север', 6:'восток'}),
            Room('4', {1:'запад', 6:'юг'}),
            Room('5', {2:'север', 7:'юг'}),
            Room('6', {4:'север', 3:'запад', 9:'юг'}),
            Room('7', {5:'север', 8:'восток'}),
            Room('8', {7:'запад', 0:'юг. Вы выбрались!'}),
            Room('9', {6:'север', 10:'юг'}),
            Room('10', {9:'север'})
        ]
        
    # Создание диаграммы комнат за счёт строки в формате Graphviz
    def create_string_diagram(self):
        answer = "digraph G {"
        for i in self.room_list:
            id = i.name
            keys = list(i.list.keys())
            for j in keys:
                if id == '1':
                    answer += f"\n\tstart -> {str(j)}"
                elif j == 0:
                    answer += f"\n\t{id} -> end"
                elif j == 1:
                    answer += f"\n\t{id} -> start"
                else:
                    answer += f"\n\t{id} -> {str(j)}"
        answer += "\n\tstart [shape=Mdiamond];\n\tend [shape=Msquare];\n}"
        return answer
    
    # Отрисовка диаграммы комнат в формате Graphviz
    def render_graph(self):
        # Создаем новый граф
        dot = graphviz.Digraph(comment='Graph')
        # Добавляем начальную вершину
        dot.node('1', label='start', shape='Mdiamond', style='filled', fillcolor='grey')
        # Добавляем конечную вершину
        dot.node('0', label='end', shape='Msquare', style='filled', fillcolor='green')
        # Добавляем рёбра между вершинами
        for i in self.room_list:
            id = i.name
            keys = list(i.list.keys())
            for j in keys:
                dot.edge(id, str(j))
        # Рендерим граф в файл с расширением .gv
        dot.render('Practice/Homework/PR2/doctest-output/round-table.gv').replace('\\', '/')
        # Выводим граф на экран
        print(dot)
            

run = 1 # Начальная комната
game = Game() # Создание объекта класса Game
game.render_graph() # Вызов метода отрисовки диаграммы комнат в формате Graphviz
print(game.create_string_diagram()) # Вызов метода создание диаграммы комнат за счёт строки в формате Graphviz