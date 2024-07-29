import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.Run1 = Runner('Усэйн', 10)
        self.Run2 = Runner('Андрей', 9)
        self.Run3 = Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')
    def test_race1(self):
        race = Tournament(90, self.Run1, self.Run3)
        result = race.start()
        self.all_results['забег №1'] = result
    def test_race2(self):
        race = Tournament(90, self.Run2, self.Run3)
        result = race.start()
        self.all_results['забег №2'] = result
    def test_race3(self):
        race = Tournament(90, self.Run1, self.Run2, self.Run3)
        result = race.start()
        self.all_results['забег №3'] = result

    if __name__ == '__main__':
        unittest.main()