import pytest

from lfsr import LFSR


def test_bit_generation_simple():

    lfsr = LFSR(seed=0b1101, tap=2)

    # Initial Cycle
    assert (lfsr._value, next(lfsr)) == (0b1101, 1)
    assert (lfsr._value, next(lfsr)) == (0b0110, 0)
    assert (lfsr._value, next(lfsr)) == (0b1011, 1)
    assert (lfsr._value, next(lfsr)) == (0b1101, 1)

    # Cycle Repeats
    assert (lfsr._value, next(lfsr)) == (0b0110, 0)
    assert (lfsr._value, next(lfsr)) == (0b1011, 1)
    assert (lfsr._value, next(lfsr)) == (0b1101, 1)


def test_bit_generation_complex():
    lfsr = LFSR(seed=0b10110010, tap=6)

    assert (lfsr._value, next(lfsr)) == (0b10110010, 0)
    assert (lfsr._value, next(lfsr)) == (0b01011001, 1)
    assert (lfsr._value, next(lfsr)) == (0b00101100, 0)
    assert (lfsr._value, next(lfsr)) == (0b00010110, 0)
    assert (lfsr._value, next(lfsr)) == (0b00001011, 1)
    assert (lfsr._value, next(lfsr)) == (0b10000101, 1)
    assert (lfsr._value, next(lfsr)) == (0b11000010, 0)
    assert (lfsr._value, next(lfsr)) == (0b11100001, 1)
    assert (lfsr._value, next(lfsr)) == (0b01110000, 0)
    assert (lfsr._value, next(lfsr)) == (0b10111000, 0)
    assert (lfsr._value, next(lfsr)) == (0b01011100, 0)
    assert (lfsr._value, next(lfsr)) == (0b10101110, 0)
    assert (lfsr._value, next(lfsr)) == (0b01010111, 1)
    assert (lfsr._value, next(lfsr)) == (0b00101011, 1)


def test_rand_int():
    lfsr = LFSR(seed=0b1101, tap=2)

    assert lfsr.rand_int(bit_length=4) == 13
    assert lfsr.rand_int(bit_length=4) == 6
    assert lfsr.rand_int(bit_length=4) == 11

    # Cycle Repeats
    assert lfsr.rand_int(bit_length=4) == 13
    assert lfsr.rand_int(bit_length=4) == 6
    assert lfsr.rand_int(bit_length=4) == 11

    # Cycle Repeats
    assert lfsr.rand_int(bit_length=4) == 13
    assert lfsr.rand_int(bit_length=4) == 6
    assert lfsr.rand_int(bit_length=4) == 11


def test_shuffle():

    lfsr = LFSR(seed=0b1101, tap=2)

    assert lfsr.shuffle(length=16, bit_length=4) == [
        13,
        6,
        11,
        14,
        7,
        12,
        15,
        8,
        0,
        1,
        9,
        2,
        3,
        10,
        4,
        5,
    ]


def test_shuffle_zero_seed_value():
    lfsr = LFSR(seed=0, tap=2)
    assert lfsr.shuffle(length=16, bit_length=4) == [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
    ]
