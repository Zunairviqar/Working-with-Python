import unittest
from bits import BitList


class TestBitList(unittest.TestCase):

    def test_constructor_value_error_prefix(self):
        with self.assertRaises(ValueError):
            b = BitList('11110000')

    def test_constructor_value_error_bits(self):
        with self.assertRaises(ValueError):
            b = BitList('0bFE110000')

    def test_from_ints(self):
        self.assertEqual(BitList.from_ints(1, 1, 0, 0), BitList('0b1100'))

    def test_from_ints_error(self):
        with self.assertRaises(ValueError):
            BitList.from_ints(1, 2, 3, 4)

    def test_arithmetic_shift_left(self):
        b = BitList('0b01000001')
        b.arithmetic_shift_left()
        self.assertEqual(b, BitList('0b10000010'))

        b = BitList('0b01000000')
        b.arithmetic_shift_left()
        self.assertEqual(b, BitList('0b10000000'))

    def test_arithmetic_shift_right_1(self):
        b = BitList('0b10000000')
        b.arithmetic_shift_right()
        self.assertEqual(b, BitList('0b11000000'))

        b = BitList('0b10000001')
        b.arithmetic_shift_right()
        self.assertEqual(b, BitList('0b11000000'))

    def test_arithmetic_shift_right_0(self):
        b = BitList('0b01111111')
        b.arithmetic_shift_right()
        self.assertEqual(b, BitList('0b00111111'))

        b = BitList('0b01111110')
        b.arithmetic_shift_right()
        self.assertEqual(b, BitList('0b00111111'))

    def test_and(self):
        b1 = BitList('0b10000011')
        b2 = BitList('0b11000001')
        self.assertEqual(b1.bitwise_and(b2), BitList('0b10000001'))

    def test_str(self):
        self.assertEqual(str(BitList('0b1010')), '1010')

    def test_equals(self):
        self.assertEqual(BitList('0b1010'), BitList('0b1010'))

    def test_decode_ascii_A(self):
        b = BitList('0b1000001')
        self.assertEqual(b.decode('us-ascii'), 'A')

    def test_decode_ascii_bracket(self):
        b = BitList('0b1011011')
        self.assertEqual(b.decode('us-ascii'), '[')

    def test_decode_ascii_multiple_chars(self):
        b = BitList('0b10000011011011')
        self.assertEqual(b.decode('us-ascii'), 'A[')

    # OPTIONAL - add these tests if you are implementing decode with utf-8

    def test_decode_utf8_4_bytes_multiple_chars(self):
        b = BitList('0b11110000100111111001100010000010111000101000001010101100')
        self.assertEqual(b.decode('utf-8'), '😂€')

    # def test_decode_utf8_4_bytes(self):
    #     b = BitList('0b11110000100111111001100010000010')
    #     self.assertEqual(b.decode('utf-8'), '😂')
    #
    # def test_decode_utf8_3_bytes(self):
    #     b = BitList('0b111000101000001010101100')
    #     self.assertEqual(b.decode('utf-8'), '€')

    # def test_decode_utf8_1_byte(self):
    #     b = BitList('0b01000001')
    #     self.assertEqual(b.decode('utf-8'), 'A')



if __name__ == '__main__':
    unittest.main()
