class Candidate:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes


class Elections:
    def __init__(self):
        self.candidates = []

    def winner(self):
        return max(self.candidates, key=lambda c: c.votes)


elections = Elections()

for i in range(5):
    name = input("Прізвище кандидата " + str(i + 1) + ": ")
    votes = int(input("Кількість голосів: "))
    elections.candidates.append(Candidate(name, votes))

total = sum(c.votes for c in elections.candidates)






print()
for c in elections.candidates:
    print(c.name, c.votes, str(round(c.votes / total * 100, 2)) + "%")

print()
print("Переможець:", elections.winner().name)