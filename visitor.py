# Visitor -COMPOSITION - Language
# Visitor -GENERALIZATION - Student
from language import Language


class Visitor:
    name :str
    language: Language

    def __init__(self, name :str, language: Language):
        self.name = name
        self.language = language

    def __str__(self):
        return self.name + self.language.__str__()
