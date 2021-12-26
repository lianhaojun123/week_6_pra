class ProgrammingLanguage:
    def __init__(self, field="", typing="", reflection="", year=""):
        self.year = year
        self.reflection = reflection
        self.typing = typing
        self.field = field

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return "{},{} Typing,Reflection={},First appeared in {}".format(self.field, self.typing, self.reflection, self.year)
