# Visitor -COMPOSITION - Language
# Visitor -GENERALIZATION - Student
class Visitor:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __str__(self):
        return self.name