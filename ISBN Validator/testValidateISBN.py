from ValidateISBN import ValidateISBN
import unittest


class TestValidateISBN(unittest.TestCase):
    def test_simple_test_to_make_sure_everything_works(self):
        expected = 54
        actual = ValidateISBN.answer()
        self.assertEqual(expected, actual)

    def test_simple_test_to_make_sure_everything_works2(self):
        expected = 54
        actual = ValidateISBN.answer()
        self.assertEqual(expected, actual)

    def test_real_ISBN_should_be_valid(self):
        validator = ValidateISBN()
        result = validator.is_ValidateISBN("0988753006")
        self.assertTrue(result)

    def test_ISBN_off_by_one_should_be_invalid(self):
        validator = ValidateISBN()
        result = validator.is_ValidateISBN("0988753005")
        self.assertFalse(result)

    def test_real_ISBN_should_be_valid2(self):
        validator = ValidateISBN()
        result = validator.is_ValidateISBN("1400069289")
        self.assertTrue(result)

    def test_nine_digit_ISBN_are_not_allowed(self):
        validator = ValidateISBN()
        try:
            validator.is_ValidateISBN("988753006")
        except ValueError as e:
            print(e)

    def test_non_numeric_ISBN_not_allowed(self):
        validator = ValidateISBN()
        try:
            validator.is_ValidateISBN("HelloWorld")
        except ValueError as e:
            print(e)

    def test_ISBN_can_end_with_an_x(self):
        validator = ValidateISBN()
        result = validator.is_ValidateISBN("172230054X")
        self.assertTrue(result)

    def test_real_ISBN_should_be_valid13(self):
        validator = ValidateISBN()
        result = validator.is_ValidateISBN("9781987631050")
        self.assertTrue(result)

    def test_13_digit_ISBN_should_not_have_x(self):
        validator = ValidateISBN()
        with self.assertRaises(ValueError):
            result = validator.is_ValidateISBN("978198763105X")

    def test_Invalid_13Digit_ISBNNumbers_should_be_thrown_out(self):
        validator = ValidateISBN()
        result = validator.is_ValidateISBN("9781987631051")
        self.assertFalse(result)