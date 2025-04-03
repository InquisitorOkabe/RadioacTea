import actions

class MainPop:
    def __init__(self):
        self.poptype = BasePop(self)
        self.name = 'Чмоня'
        self.hp = [self.poptype.stats[0], self.poptype.stats[0]]
        self.mind = [self.poptype.stats[1], self.poptype.stats[1]]
        self.love = [self.poptype.stats[2], self.poptype.stats[2]]
        self.food = [self.poptype.stats[3], self.poptype.stats[3]]
        self.water = [self.poptype.stats[4], self.poptype.stats[4]]

        # Создаём словарь действий
        self.actions = {}
        # Обновляем его из словаря действий Чмони Обыкновенной.
        self.actions.update(self.poptype.actions)
        self.traits = {}
        self.status = []
        # Модификаторы на статы. Прописываем в них базовые статы от типа.
        self.mods = {
                     'hp':{'poptype':self.poptype.stats[0]},
                     'mind':{'poptype':self.poptype.stats[1]},
                     'love':{'poptype':self.poptype.stats[2]},
                     'food':{'poptype':self.poptype.stats[3]},
                     'water':{'poptype':self.poptype.stats[4]},
                     }
        # Перерассчитываем статы с учётом модов.
        self.calcMods()

        # Функция перерассчёта статов.
    def calcMods(self):
        for i in self.mods['hp'].values():
            self.hp[1] += i
        for i in self.mods['mind'].values():
            self.mind[1] += i
        for i in self.mods['love'].values():
            self.love[1] += i
        for i in self.mods['food'].values():
            self.food[1] += i
        for i in self.mods['water'].values():
            self.water[1] += i

class BasePop:
    def __init__(self, mainPop):
        self.typename = 'Чмоня Обыкновенная' # Название типажа.
        self.size = 1 # Размер
        self.stats = [ # Статы
                      10, # Здоровье
                      10, # Рассудок
                      10, # Ласка
                      10, # Голод
                      10, # Жажда
                      ]
        self.traits = { # Четры Характера
                       'trait':''
                       }
        self.actions = { # Действия
                        # --- Базовые ---
                        'Укусить':actions.Ukus(),
                        'Пищать':None,
                        'Лизать':None,
                        'Убежать':None,
                        'Спрататься':None,
                        # --- Тренированные 0-6 ---
                        }
