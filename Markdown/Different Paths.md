# Title

Different Paths

# Metadata

## Type

Counting 

# Main Version

## Statement

There are 5 different paths you could take to get from home to school. In a week (from Monday to Friday) you would like to try a different path every day. In how many different ways can you organise your walk to school for the week? 

## Correct Answer

120

## Hint

Think about how many options you have to select the first path, then how many you have for the second and so on. Be careful that you can not choose the same path twice in a week.

## Explanation

You have 5 possible days of the week and you would like to have one different path per day. ON the first day you have a choice of 5 paths. On the second day, you only have 4 paths left to choose from because you can't take the one you took on Monday. On the third day you have 3 to choose from and so on. The solution is therefore 5×4×3×2×1 =120. This is counting how many ways you can order 5 objects (paths) in 5 positions (days of the week). This is a problem on *permutations* (without repetition). 

The mathematical symbol ! is called *factorial* and represents multiplying by decreasing integers until you reach 1. So 5×4×3×2×1 can be written as 5!  

# Extension 1

## Statement

What if you had to go to school on Saturdays as well and you also found a new path? In how many ways can you arrange your week such that every day you go to school walking on different paths? 

## Hint

Is there a way to use the result of the previous problem? Think about how many ways you can now walk to school on Monday.

## Correct Answer

720

## Explanation

You have now 6 possible days of the week and 6 different paths. You would like to have one different path per day. The solution is obtained by counting how many ways you can order 6 objects (paths) in 6 positions (days of the week). The solution is obtained as 6×5×4×3×2×1 = 120  Notice this is 6×120 (6 times the previous solution). You have just discovered a recursive property of factorials: n! = n×(n - 1)!.

# Extension 2

## Statement

What if you had to go to school on Sundays as well and you also found four new paths so there are now 10 paths to choose from? In how many ways can you arrange your week such that every day you go to school walking on different paths? 

## Hint

Is this exactly the same style of problem as before? Think about how many ways you can now walk to school on Monday etc but when you get to Sunday there will still be more than one to choose from. 

## Correct Answer

604800

## Explanation

You have now 7 possible days of the week and 10 different paths. You would like to have one different path per day. The solution is obtained by counting how many ways you can order 10 objects (paths) in 7 positions (days of the week). The solution is obtained by 10×9×8×7×6×5×4 =  604800. If you wanted to calculate this using factorials, 10! is close to the answer, but we don't want 3×2×1 at the end. 3×2×1 is 3! so we can do 10! ∕ 3! =604800.  

# Additional information

## About

Factorials were used to count permutations at least as early as the 12th century, by Indian scholars. The notation n! was introduced by the French mathematician Christian Kramp in 1808.

Factorials get big very quickly. 5! = 120, but 20! = 2432902008176640000.

## References

* https://en.wikipedia.org/wiki/Factorial

* https://www.mathsisfun.com/numbers/factorial.html

