import unittest
import helper

class TestExercise1(unittest.TestCase):
    def setUp(self):
        self.data = {
          "DC_PEC": '',
          "DC_SCT": "test_or(lambda: test_function('print'), lambda: test_object('test'))",
          "DC_SOLUTION": "print('test')\ntest = 3"
        }

    def test_Pass1(self):
        self.data["DC_CODE"] = 'test = 3'
        sct_payload = helper.run(self.data)
        self.assertEqual(sct_payload['correct'], True)

    def test_Pass2(self):
        self.data["DC_CODE"] = "print('test')"
        sct_payload = helper.run(self.data)
        self.assertEqual(sct_payload['correct'], True)

    def test_Pass3(self):
        self.data["DC_CODE"] = "test = 3\nprint('test')"
        sct_payload = helper.run(self.data)
        self.assertEqual(sct_payload['correct'], True)

    def test_Pass4(self):
        self.data["DC_CODE"] = "test = 4\nprint('test')"
        sct_payload = helper.run(self.data)
        self.assertEqual(sct_payload['correct'], True)

    def test_Pass4(self):
        self.data["DC_CODE"] = "test = 3\nprint('not test')"
        sct_payload = helper.run(self.data)
        self.assertEqual(sct_payload['correct'], True)

    def test_Fail1(self):
        self.data["DC_CODE"] = "test = 4\nprint('not test')"
        sct_payload = helper.run(self.data)
        self.assertEqual(sct_payload['correct'], False)
        self.assertEqual(sct_payload['message'], "Did you call <code>print()</code> with the correct arguments? Call on line 2 has wrong arguments. The first argument seems to be incorrect. Expected <code>'test'</code>, but got <code>'not test'</code>.")

if __name__ == "__main__":
    unittest.main()