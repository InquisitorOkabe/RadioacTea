class Action:
    def __init__(self):
        self.name = 'Действие'
        self.desu = 'Описание.'
        self.type = None # True / False - Активное / Пассивное.
        self.tags = {}

    def start(self):
        pass

    def powerStart(self):
        pass

class Ukus(Action):
    def __init__(self):
        super().__init__()
        self.name = 'Укус'
        self.desu = 'Урон: 10\nСилы: 25\nЧмоня кусает противника, делая ему больно.\n(С) Вешает статус Прокус при атаке.'
        self.type = True

        self.damage = 10
        self.stamine = 25

    def start(self, me, tar):
        self.stamine[0] -= self.stamine
        tar.hp[0] -= self.damage
