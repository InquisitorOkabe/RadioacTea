class Status:
    def __init__(self):
        self.name = 'Статус'
        self.desu = 'Описание'

    def cast(self, tar):
        # Функция, вызываемая при присвоении статуса.
        pass

    def tick(self, tar):
        # Функция, вызываемая при тике статуса.
        pass

    def decast(self, tar):
        # Функция, вызываемая при снятии статуса.
        pass
