import unittest
from projects.Quiz_Game.src.gamesystem import QuizGameSystem

class QuizGameTest(unittest.TestCase):
    def setUp(self):
        self.system = QuizGameSystem()


    #def test_start_game_no(self):
    def test_get_questions_items(self):
        questions = self.system.get_questions()
        self.assertEqual(questions[0]['question'], "Question 1: What is your Favourite programming language?")
        self.assertEqual(questions[0]['answer'], "python")

    def test_start_game_yes(self):
        result = self.system.start_game(start="yes")
        self.assertTrue(result)

    def test_start_game_no(self):
        result = self.system.start_game(start="no")
        self.assertFalse(result)

    def test_show_result_all_correct(self):
        mark = self.system.show_result(3,3)
        self.assertEqual(mark, 100)

    def test_show_result_correct_one(self):
        mark = self.system.show_result(1,3)
        self.assertEqual(mark, 33)

if __name__ == "__main__":
    unittest.main()