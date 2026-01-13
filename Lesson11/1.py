# Создать класс газировка,если клбуничный вкус и если обычный

class Soda:
    def __init__(self, taste=None):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f"У вас газировка с {self.taste} вкусом"
        else:
            return "У вас обычная газировка"

# Примеры использования
soda1 = Soda("клубничным")
soda2 = Soda()
soda3 = Soda("вишневым")

print(soda1)
print(soda2)
print(soda3)