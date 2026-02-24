class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def vote(self):
        self.votes += 1

class Election:
    def __init__(self):
        self.candidates = {}

    def add_candidate(self, name):
        self.candidates[name] = Candidate(name)

    def vote(self, name):
        if name in self.candidates:
            self.candidates[name].vote()

    def result(self):
        for c in self.candidates.values():
            print(c.name, c.votes)

def run():
    e = Election()
    e.add_candidate("Ali")
    e.add_candidate("Vali")

    e.vote("Ali")
    e.vote("Ali")
    e.vote("Vali")

    e.result()

run()
