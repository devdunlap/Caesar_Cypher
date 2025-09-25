
"""
Unit tests for the Caesar Cipher program.
"""

import unittest
import io
import sys
from main import caesar

class TestCaesarCipher(unittest.TestCase):
	def test_symbols_and_numbers(self):
		"""
		Test that a string with only symbols and numbers is unchanged.
		"""
		input_str = '1234!@#$%^&*()_+-=,./<>?'
		self.assertEqual(self._get_result(input_str, 10, 'encode'), input_str)
		self.assertEqual(self._get_result(input_str, 10, 'decode'), input_str)
	def test_empty_string(self):
		"""
		Test encoding and decoding of an empty string.
		"""
		self.assertEqual(self._get_result('', 5, 'encode'), '')
		self.assertEqual(self._get_result('', 5, 'decode'), '')
	"""
	Unit tests for the caesar function.
	"""

	def test_encode_lowercase(self):
		"""
		Test encoding lowercase letters.
		"""
		self.assertEqual(
			self._get_result('abc', 1, 'encode'),
			'bcd'
		)

	def test_decode_lowercase(self):
		"""
		Test decoding lowercase letters.
		"""
		self.assertEqual(
			self._get_result('bcd', 1, 'decode'),
			'abc'
		)

	def test_encode_uppercase(self):
		"""
		Test encoding uppercase letters.
		"""
		self.assertEqual(
			self._get_result('ABC', 2, 'encode'),
			'CDE'
		)

	def test_decode_uppercase(self):
		"""
		Test decoding uppercase letters.
		"""
		self.assertEqual(
			self._get_result('CDE', 2, 'decode'),
			'ABC'
		)

	def test_encode_mixed_case(self):
		"""
		Test encoding mixed case letters.
		"""
		self.assertEqual(
			self._get_result('AbC', 1, 'encode'),
			'BcD'
		)

	def test_non_alpha_characters(self):
		"""
		Test that non-alphabetic characters remain unchanged.
		"""
		self.assertEqual(
			self._get_result('Hello, World! 123', 5, 'encode'),
			'Mjqqt, Btwqi! 123'
		)

	def test_shift_wrap(self):
		"""
		Test wrap-around at end of alphabet.
		"""
		self.assertEqual(
			self._get_result('xyz', 3, 'encode'),
			'abc'
		)

	def test_negative_shift(self):
		"""
		Test negative shift values.
		"""
		self.assertEqual(
			self._get_result('abc', -1, 'encode'),
			'zab'
		)

	def test_large_shift(self):
		"""
		Test large shift values (>26).
		"""
		self.assertEqual(
			self._get_result('abc', 27, 'encode'),
			'bcd'
		)

	def _get_result(self, text, shift, direction):
		"""
		Helper to capture printed output from caesar and extract result.
		"""
		captured = io.StringIO()
		sys.stdout = captured
		caesar(text, shift, direction)
		sys.stdout = sys.__stdout__
		for line in captured.getvalue().splitlines():
			if direction == 'encode' and 'Encoded result:' in line:
				return line.split(':', 1)[1].strip()
			if direction == 'decode' and 'Decoded result:' in line:
				return line.split(':', 1)[1].strip()
		return None

if __name__ == '__main__':
	unittest.main()
