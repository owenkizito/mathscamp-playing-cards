# Title

Kaprekar's Number

# Metadata

## Type

fun fact

# Main Version

## Statement

Choose a four digit number where the digits are not all the same.

Rearrange the digits to get the largest and smallest possible numbers these digits can make.

Subtract the smallest number from the largest to get a new number, and carry on repeating the operation for each new number. You will eventually end up at the same number.

## Hint

For example if you start with 4252, you should do the calculation 5422 - 2245 = 3177. Then do 7731 - 1377 and keep going.

## Explanation

You always end up with the number 6174. This is known as Kaprekar's number. For example 5432 – 2345 = 3087

8730 – 0378 = 8352

8532 – 2358 = 6174

7641 – 1467 = 6174

# Extension 1

## Statement

What happens when you do this process with 3 digit numbers (where not all the digits are the same)? Can you explain why you always end up at the same number? Note that if you find 99 as an answer at any stage, this would then give 099 as the smallest number and 990 as the biggest.

## Hint

For example, if you start with 792, the first calculation you have to do is 972 - 279 = 693. 

## Explanation

We can write a three digit number abc (imagine it is as big as possible) as 100×a + 10×b + c. If we rearrange the digits to make it as small as possible it would be cba which we can write as 100×c + 10×b + a. We then subtract to give 100×a + 10×b + c - (100×c + 10×b + a) = 99×a - 99×c = 99×(a - c). So after one step, the number will be a multiple of 99. The only 3 digit numbers that are multiples of 99 are 099, 198, 297, 396, 495, 594, 693, 792, 891, and 990. We only need to check the first five of these (as we will be rearranging the digits anyway) and we can verify that all of them end up giving the answer 495.

# Additional information

## About

D. R. Kaprekar (1905 - 1986) was an Indian school maths teacher who loved playing with numbers. He discovered a number of results in number theory and described various properties of numbers.

## References

* https://en.wikipedia.org/wiki/D._R._Kaprekar

* https://plus.maths.org/content/mysterious-number-6174
