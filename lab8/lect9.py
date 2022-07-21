class Base:
    def __init__(self, x):
        self.x = x

    def show(self):
        print('Base', self.x)

class Deriviate(Base):  # Base - базовый класс, Deriviate - производный класс
    def __init__(self):
#        Base.__init__(self, 20)
        super().__init__(20)  # явный вызов конструктора
        self.name = ''

a = Base(10)
b = Deriviate()
a.show()
b.show()