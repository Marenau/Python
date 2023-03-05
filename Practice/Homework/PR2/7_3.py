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
            
    # Проверка на наличие тупиков в игре
    def check_for_dead_ends(self):
        dead_ends = [] # Список тупиков
        for room in self.room_list:
            if len(room.list) == 1: # Если в комнате есть только один выход (тупик)
                dead_ends.append(room) # Добавляем комнату в список тупиков
        if len(dead_ends) > 0: # Если в игре есть тупики
            print("Найдены тупики в комнатах:")
            for room in dead_ends: # Выводим список тупиков
                print(f"Комната {room.name}")
        else: # Если в игре нет тупиков
            print("Тупиков не найдено")

run = 1 # Начальная комната
game = Game() # Создание объекта класса Game
game.check_for_dead_ends() # Вызов метода для поиска тупиков в игре