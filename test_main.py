import unittest
from main import caesar, alphabet

class TestCaesarCipher(unittest.TestCase):
	def test_encode_lowercase(self):
		# 'abc' shifted by 1 -> 'bcd'
		self.assertEqual(
			self._get_result('abc', 1, 'encode'),
			'bcd'
		)

	def test_decode_lowercase(self):
		# 'bcd' shifted by 1 decode -> 'abc'
		self.assertEqual(
			self._get_result('bcd', 1, 'decode'),
			'abc'
		)

	def test_encode_uppercase(self):
		# 'ABC' shifted by 2 -> 'CDE'
		self.assertEqual(
			self._get_result('ABC', 2, 'encode'),
			'CDE'
		)

	def test_decode_uppercase(self):
		# 'CDE' shifted by 2 decode -> 'ABC'
		self.assertEqual(
			self._get_result('CDE', 2, 'decode'),
			'ABC'
		)

	def test_encode_mixed_case(self):
		# 'AbC' shifted by 1 -> 'BcD'
		self.assertEqual(
			self._get_result('AbC', 1, 'encode'),
			'BcD'
		)

	def test_non_alpha_characters(self):
		# Numbers, punctuation, and spaces should remain unchanged
		self.assertEqual(
			self._get_result('Hello, World! 123', 5, 'encode'),
			'Mjqqt, Btwqi! 123'
		)

	def test_shift_wrap(self):
		# 'xyz' shifted by 3 -> 'abc'
		self.assertEqual(
			self._get_result('xyz', 3, 'encode'),
			'abc'
		)

	def test_negative_shift(self):
		# 'abc' shifted by -1 -> 'zab'
		self.assertEqual(
			self._get_result('abc', -1, 'encode'),
			'zab'
		)

	def test_large_shift(self):
		# 'abc' shifted by 27 -> 'bcd' (27 % 26 == 1)
		self.assertEqual(
			self._get_result('abc', 27, 'encode'),
			'bcd'
		)

	def _get_result(self, text, shift, direction):
		# Helper to capture printed output from caesar
		import io
		import sys
		captured = io.StringIO()
		sys.stdout = captured
		caesar(text, shift, direction)
		sys.stdout = sys.__stdout__
		# Extract the result line from printed output
		for line in captured.getvalue().splitlines():
			if direction == 'encode' and 'Encoded result:' in line:
				return line.split(':', 1)[1].strip()
			if direction == 'decode' and 'Decoded result:' in line:
				return line.split(':', 1)[1].strip()
		return None

if __name__ == '__main__':
	unittest.main()
