# lfsr

Simple implementation of a Linear Feedback Shift Register

An LFRS can be used to generate psuedo-random numbers based on a given seed value.  In it's most basic form, an LFSR will XOR the values at given bit positions in a nubmer, and feed that back to generate a new most-signifcant bit for that nubmer.  The stored value will then be shifted to the right, and the least-significant bit will be returned.

## A simple example

Given the seed value 1101 and using the bit in positions 0 and 2 as the taps, the following sequence is generated.

1101 -> 0110 -> 1011 -> 1101

At each iteration, the least significant bit will be returned, yielding 1, 0, 1, 1 as the resulting bits. The resulting output will continue to cycle through that pattern 1,0,1,1,1,0,1,1,1,0,1,1...

Taking groupings of N bits it is possible to generate pseudo random numbers assuming that the seed is sufficiently randomized.
