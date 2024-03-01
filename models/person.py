class Person:
    def __init__(self, name, profession = 'None', age = 0):
        self._name = name
        self._profession = profession
        self._age = age

    def __str__(self):
        return f'{self._name}, {self._profession}, {self._age} years old.'

    @property
    def salutation(self):
        if self._profession != 'None':
            return f"Hi, I'm {self._name}, I work as {self._profession}!"
        else:
            return f"Hi, I'm {self._name}"

    def birthday(self):
        self._age += 1
