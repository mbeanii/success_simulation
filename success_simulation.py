import random


class Person:
    def __init__(self, treasure: int, credentials: list, knowledge: int, title: str):
        self.treasure = treasure
        self.credentials = credentials
        self.knowledge = knowledge
        self.title = title

    def learn(self):
        pass

    def apply_knowledge(self):
        self.treasure += self.knowledge

    work = apply_knowledge

    def enjoy_success(self):
        pass


class SelfMade(Person):
    """If you want to have what they have, don't do what they do, learn what they know and apply it."""

    def __init__(self, treasure: int, credentials: list, knowledge: int, title: str):
        super().__init__(treasure, credentials, knowledge, title)
        self.habits = [
            self.learn,
            self.apply_knowledge,
            self.enjoy_success,
        ]

    def learn(self):
        """Everyone in your life is your mentor whether either of you realizes it."""
        mentor = SelfMade(treasure=1000, credentials=["MBA"], knowledge=50, title="CEO")
        return mentor.knowledge

    def enjoy_success(self):
        self.treasure -= 30


class Normie(Person):
    """What do you want - to look successful or to be successful?"""

    master_dict = {"coding": 5, "public speaking": 3, "leadership": 4, "etc": 0}

    def __init__(self, time_left, want):
        self.knowledge = 0
        self.habits = []
        self.treasure = random.randint(1, 1000)
        self.time_left = time_left
        self.want = want
        self.books_read = 0
        self.work_experience = 0
        self.tutorials_completed = 0
        self.skills_obtained = []

        if self.want == "style":
            credentials = ["Engineering Degree", "PMP certification"]
            title = "Director"
            covetee = SelfMade(self.treasure, credentials, {}, title)
            self.habits = [covetee.enjoy_success]

        elif self.want == "substance":
            mentor = SelfMade(self.treasure, [], 0, "")
            self.habits = [
                getattr(self, method.__name__)
                for method in mentor.habits
                if hasattr(self, method.__name__)
            ]

    def learn(self):
        self.books_read += 1
        self.work_experience += 1
        self.tutorials_completed += 1
        self.knowledge += (
            self.books_read + self.work_experience + self.tutorials_completed
        )
        for skill in self.skills_obtained:
            self.knowledge += Normie.master_dict[skill]

        if self.treasure > 100:
            self.__class__ = SelfMade
        return

    def add_skill(self, skill):
        self.skills_obtained.append(skill)
        self.knowledge += Normie.master_dict[skill]

    def __str__(self):
        return f"{self.__class__}"


def calculate_percent_success_rate(want):
    num_self_made = 0
    iterations = 10000
    for _ in range(iterations):
        normie = Normie(random.randint(1, 70), want=want)
        for _ in range(normie.time_left):
            for habit in normie.habits:
                habit()
        if isinstance(normie, SelfMade):
            num_self_made += 1
    return (num_self_made / iterations) * 100


if __name__ == "__main__":
    success_rate_style = calculate_percent_success_rate("style")
    print(f"Success rate for style: {success_rate_style}%")

    success_rate_substance = calculate_percent_success_rate("substance")
    print(f"Success rate for substance: {success_rate_substance}%")
