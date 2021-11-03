"""
Linear Feedback Shift Register based Random Number Generator
"""

import time
from typing import List, Optional


class LFSR:
    """
    Simple Linear Feedback Shift Register

    :param seed: An integer value to seed the shift register.
    :param tap: Which bit position should be used for calculating the
        next bit in sequence.
    """

    def __init__(self, seed: Optional[int] = None, tap: int = 8):
        self._seed = int(time.time()) if seed is None else seed
        self._tap = self._seed.bit_length() // 2 if tap is None else tap

        self._value = self._seed

    def __next__(self) -> int:
        """
        Generate the next bit in sequence.
        """

        # A seed value of 0 is a special case in an LFSR where the
        # generated bits will always be 0
        if self._seed == 0:
            return 0

        bit = self._value & 1
        tap_bit = self._value >> self._tap & 1
        leading_bit = bit ^ tap_bit
        leading_mask = leading_bit << self._seed.bit_length() - 1
        remainder = self._value >> 1
        self._value = leading_mask | remainder

        return bit

    def rand_int(self, bit_length: int = 32) -> int:
        """
        Generate a random integer value between 0 and 2^bit_length.

        :raises: ValueError if the bit_length is <= 0.
        """
        if bit_length <= 0:
            raise ValueError("Bit length must be a positive integer")

        total = 0
        for i in range(bit_length):
            bit = next(self)
            total = total | (bit << i)
        return total

    def shuffle(self, length: int, bit_length: int = 32) -> List[int]:
        """
        Return a shuffled list of unique integers.

        :param length: The number of elements to return
        :param bit_length: The maximum number of bits to return per element,
            e.g. a bit_length of 5 would mean values < 32.
        :raises ValueError: if the requested length would require more
            elements then would be possible with the given bit_length.

        :returns a shuffled list of integer values.
        """

        if length.bit_length() - 1 > bit_length:
            raise ValueError(
                f"Cannot generate more than {1 << bit_length} values"
            )

        values: List[int] = []
        while len(values) < length:
            value = self.rand_int(bit_length=bit_length)

            while value in values:
                value = (value + 1) % (1 << bit_length)

            values.append(value)

        return values
