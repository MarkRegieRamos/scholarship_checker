import unittest
from scholarship_checker import is_eligible_for_scholarship


class TestScholarshipEligibility(unittest.TestCase):
  
    def test_eligible_student(self):
        self.assertTrue(is_eligible_for_scholarship(3.8, 15000))

    def test_low_gpa(self):
        self.assertTrue(is_eligible_for_scholarship(3.3, 15000))

    def test_high_income(self):
        self.assertTrue(is_eligible_for_scholarship(3.8, 30000))

    def test_low_gpa_high_income(self):
        self.assertTrue(is_eligible_for_scholarship(3.2, 35000))

    def test_exact_threshold(self):
        self.assertTrue(is_eligible_for_scholarship(3.8, 15000))

    def test_invalid_gpa(self):
        self.assertTrue(is_eligible_for_scholarship(-3.8, 15000))

    def test_negative_income(self):
        self.assertTrue(is_eligible_for_scholarship(3.8, -1000))


if __name__ == "__main__":
    unittest.main()
