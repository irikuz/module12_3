import module_12_1
import module_12_2
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        walker = module_12_1.Runner("walker")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = module_12_1.Runner("runner")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_1 = module_12_1.Runner("Begun_1")
        runner_2 = module_12_1.Runner("Begun_2")

        for i in range(10):
            runner_1.run()
            runner_2.walk()

        self.assertNotEqual(runner_1.distance, runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.usain = module_12_2.Runner("Усэйн", 10)
        self.andrey = module_12_2.Runner("Андрей", 9)
        self.nick = module_12_2.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_1(self):
        tour_1 = module_12_2.Tournament(90, self.usain, self.nick)
        all_results = tour_1.start()
        self.assertTrue(all_results[2], self.nick)
        print(all_results)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_2(self):
        tour_2 = module_12_2.Tournament(90, self.andrey, self.nick)
        all_results = tour_2.start()
        self.assertTrue(all_results[2], self.nick)
        print(all_results)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_3(self):
        tour_3 = module_12_2.Tournament(90, self.usain, self.andrey, self.nick)
        all_results = tour_3.start()
        self.assertTrue(all_results[3], self.nick)
        print(all_results)


if __name__ == "__main__":
    unittest.main()
