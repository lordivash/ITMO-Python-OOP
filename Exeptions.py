class HealthError(ValueError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Здоровье бойца не может быть {}'.format(self.value)
