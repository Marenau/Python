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

run = 1  # Начальная комната
game = Game()  # Создание объекта класса Game
while True:
    curren_room = game.run(run)  # Получение объекта класса Room для текущей комнаты
    if curren_room.name == '0':  # Если это конец игры, то выходим из цикла
        break;
    curren_room.print_info()  # Вывод информации о текущей комнате на экран
    
    actions = list(curren_room.list.values())  # Список допустимых действий
    for k, action in enumerate(actions):
        print(f"{k + 1}. Проход на {action}")  # Вывод допустимых действий на экран
        
    choice = int(input())  # Получение действия от пользователя
    run = list(curren_room.list.keys())[choice - 1] # В какую комнату переместится пользователь после выполнения действия