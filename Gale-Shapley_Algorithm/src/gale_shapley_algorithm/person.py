class Person:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.match = None
        self.index = 0

    def is_free(self):
        return self.match is None

    def propose(self):
        if self.index < len(self.preferences):
            return self.preferences[self.index]
        return None

    def accept_proposal(self, suitor):
        if self.match is None or self.preferences.index(suitor) < self.preferences.index(self.match):
            self.match = suitor
            return True
        return False
