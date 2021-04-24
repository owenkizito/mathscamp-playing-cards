# Title

Monkey business

# Metadata

## Type

puzzle

# Main Version

## Statement

A large room has 1000 light bulbs in it, all are switched off. 1000 monkeys enter the room and decide to press the light switches in a very particular way.

The 1<sup>st</sup> monkey presses every multiple of 1.

The 2<sup>nd</sup> monkey presses every multiple of 2.

The 3<sup>rd</sup> monkey presses every multiple of 3.

Etc., until the 1000<sup>th</sup> monkey. After all the monkeys have finished pressing switches, how many lights in total will be on?

## Correct Answer

31

## Hint

Can you work out whether number 8 will be on or off? How about number 9? What is it about the factors of these two numbers that means one of them is on and one of them is off?

## Explanation

Most numbers will be pressed by an even number of monkeys, e.g. 24 has factors (1×24, 2×12, 3×8, 4×6), so monkeys 1, 2, 3, 4, 6, 8, 12, 24 will press the switch, and as this is an even number the light will be off.

Square numbers are the only ones which do not have an even number of factors, e.g. 16 has factors (1×16, 2×8, 4×4). Monkeys 1, 2, 4, 8, 16 will press the switch, and as this is an odd number that the switch has been pressed, the light will stay on (monkey 4 won't press it twice!).

So we just need to work out how many square numbers there are between 1 and 1000. 

We find the largest square number less than 1000: 31×31 = 961, 32×32 = 1024

So there will be 31 switches left on! (switch numbers 1, 4, 9, 16, 25, 36, … , 900, 961)

# Extension 1

## Statement

How many lights switches will be touched by exactly three monkeys?

## Hint

Light switch number 9 will be touched by three monkeys:1, 3, and 9. Can you find other numbers that will?

## Correct Answer

11

## Explanation

The switches which are touched by only three monkeys are the squares of prime numbers (because these are the only numbers which have exactly three factors.) The numbers are 4,9, 25, 49, 121, 169, 289, 361, 529, 841 and 961 which is 11 in total.

# Extension 2 

## Statement

Which light bulb will be touched by the most monkeys?

## Hint

Which number under 1000 has most factors? Try and build up a number using small prime numbers.

## Correct Answer

840

## Explanation

A number will have the most number of factors if its prime factor decomposition has the most numbers in it. For example 24 = 2³×3 has 8 factors (1, 2, 3, 4, 6, 8, 12, 24) compared to 25 = 5² which only has 3 (1, 5, 25). 

To find the number less than 1000 that has the most factors, we start with as many of the smallest primes as we can, then multiply to less than 1000 (2×3×5×7) and then we can multiply by 2 until the number is as close to 1000 as possible.

Therefore, the answer is 2³×3×5×7 = 840.

The number of factors of 840 is 32, so light switch 840 has been touched by 32 monkeys.

# Additional information

## About

This is a very famous puzzle that can be found in different contexts - opening and closing lockers is another common one. It is designed to make you think about the properties of different numbers. 

## References

* https://mathsclub.samicharity.co.uk/en/monkey-business

* https://tasks.illustrativemathematics.org/content-standards/tasks/938

* https://nrich.maths.org/countingfactors

* https://en.wikipedia.org/wiki/Highly_composite_number

