# Title

Shaking Hands

# Metadata

## Type

Counting 

# Main Version

## Statement

At your friend's birthday there are 8 children at the party. Each child shakes hands with all the other children in the party. How many handshakes happened in total? 

## Correct Answer

28

## Hint

Start with a small number of children, e.g. 3, 4, or 5. What is the number of handshakes you have to add if another child joins the party? 

## Explanation

By counting from small examples, you may realise that each time you add a person at the birthday party with n children, the number of handshakes increases by n.

If we have 2 children (say A and B) we just have 1 handshake AB. 

When we have 3 children (say A, B, and C) we have 3 handshakes: AB, AC, and BC. There is the original one and 2 extra ones now that C has joined. 1 + 2 = 3.  

If we add another child (say D) they must shake hands with A, B, and C and all the other handshakes still take place. So there will be 1 + 2 + 3 = 6 handshakes

If we add another child to this group of 4, then there will be another 4 handshakes.So 1 + 2 + 3 + 4 = 10 handshakes.

If we follow this pattern we can find the answer for 8 children is 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

Another way to think about it is if you are one of the 8 children, you need to shake hands with the 7 other people. So does every other child at the party. Since there are 8 of you, and you each shake hands with 7 other people, there should be 8×7 handshakes. However, as it takes 2 people to shake hands we have counted each handshake twice. So we divide by two and the answer is 8×7 ∕ 2 = 28 

# Extension 1

## Statement

The whole school came to the birthday party: there are now 100 children! How many handshakes happen?

## Hint

Can you find a formula for the number of handshakes when there are n children at the birthday party? Think about the strategy you used to answer the previous question and try to generalise it for any number of children.

## Correct Answer

4950

## Explanation

Generalising what you found earlier, you can come up with the rule that for a birthday party with n children you have 1 + 2 + … + (n - 1) handshakes. You may realise that you can then use a formula (n×(n - 1) ∕ 2) to calculate the number of handshakes. For 100 children there are 100×99 ∕ 2 = 4950 handshakes. This is the same as adding up the numbers 1 + 2 + 3 + …+ 99.

# Extension 2

## Statement

A bigger school had a party. There were 28680 handshakes! How many children were there?

## Hint

Try using the formula we have derived for the total number of handshakes for n children.

## Correct Answer

240

## Explanation

The formula for the number of handshakes for n children is n×(n - 1) ∕ 2. We need to find the value of n such that n×(n - 1) ∕ 2=28680. Multiplying by two gives us n×(n - 1) = 57360. Notice that we roughly want n×n = 57360 so try taking the square root of 57360. This gives 239.49947… So let us try 240, which indeed gives 240×239/2 = 28680.

# Additional information

## About

This is a classic puzzle that has been around for many years. There are many problem-solving strategies that can be used to find the solution - act it out, draw a diagram, look for a pattern, solve a simpler problem, make an organized list, make a table, use logical reasoning, . . . . The solution has deep mathematical properties and is a key result in the field of combinatorics. The number of handshakes is always a **triangular number**. The first ten triangular numbers are 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …

## References

* https://nrich.maths.org/6708

* https://www.nctm.org/Publications/Teaching-Children-Mathematics/Blog/Reflecting-on-the-Handshake-Problem/

* https://www.mathsisfun.com/algebra/triangular-numbers.html

* https://en.wikipedia.org/wiki/Triangular_number

