# Title

Triangular Slices

# Metadata

## Type

Counting 

# Main Version

## Statement

Consider the cake below – a six-sided hexagon. Now split it into triangles by cutting along diagonals that don't cross each other, one example is given in red. This splitting into triangles is called a triangulation. In how many ways can you do this?

![](Triangular%20Slices_images/image_0.png)

## Correct Answer

14

## Hint

In how many ways could you do it if the cake were a square? What if it were a five-sided pentagon? Can you use the symmetries of your cake to count faster?

## Explanation

It is best to start with a simpler question and look for patterns. Start by looking at a square. There are two different ways we could slice the cake. 

![](Triangular%20Slices_images/image_1.png)

For a pentagon there are five ways:

![](Triangular%20Slices_images/image_2.png)

For a hexagon there are 14 ways as you can see below:

![](Triangular%20Slices_images/image_3.png)

In this diagram you can see the solution is found by thinking of 6 + 3 + 2 + 3 = 14, but you can arrive at the solution by doing 5 + 2 + 2 + 5 = 14 where 5 is the answer for a pentagon and 2 is the answer for a square. The equivalent combination for the pentagon is 2 + 1 + 2 = 5, where 1 is the result of the triangle (which has of course only one option) and 2 is the result for a square.

This is a more useful technique for moving on to thinking of polygons with more vertices.

# Extension 1

## Statement

Can you find the answer to the same question if the cake has the shape of a seven-sided heptagon? 

## Hint

Can you reuse previous results to compute this number? Counting explicitly might be too long. Can you come up with a way to reduce the problem in simpler cases you have already counted? Focus on when a fixed edge of the heptagon is present in a certain triangle. The heptagon is then split into two parts, the one at the left of the above triangle and the one at the right. Both parts are smaller...

## Correct Answer

42

## Explanation

Let us number the vertices of the heptagon from 1 to 7 counter-clockwise. Let us focus our attention on a fixed edge, say the one with vertices 1 and 2. When the edge is present in the triangle with the extra vertex 3, then the heptagon is split in that triangle and the hexagon at its left (with vertices 1, 3, 4, 5, 6, and 7). For the latter, the problem is the exact same you solved before, e.g. you get 14 ways of triangulating it. Then consider when the fixed edge forms a triangle with vertex 4. At the right of that triangle you have one triangle (with vertices 2, 3, and 4), whereas at the left you have a pentagon (with vertices 1, 4, 5, 6, and 7) for which we know you can do 5 triangulations. Therefore, this case provides you with 5×1 = 5 triangulations.
Let us consider the case when the fixed edge forms a triangle with a vertex 5. Both at the right of that triangle and at the left you have one square: one with vertices 2, 3, 4, and 5, and the other with vertices 1, 5, 6, and 7. Each square can be independently triangulated in 2 ways, therefore, this case provides you with 2×2 = 4 triangulations.
We continue with the fixed edge forming a triangle with vertices 6 and then 7.
We have exhausted all possible ways the fixed edge can appear in a triangulation. Moreover in every possible triangulation every edge has to be part of a triangle. Therefore above we have covered all possible cases, which are adding up: 14 + 1×5 + 2×2 + 5×1 + 14 = 42.

We can find a formula for the number Cₙ of triangulations of the (n + 2)-gon. Generalising what we did before we have that:
Cₙ = Cₙ₋₁ + C₁×Cₙ₋₂ + C₂×Cₙ₋₃ + … + Cₙ₋₂×C₁ + Cₙ₋₁
The iᵗʰ summand corresponds to the number of triangulations possible when the fixed edge forms a triangle with the vertex (i + 2), where i is a number from 1 to n. By what we saw: C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42, … .

# Extension 2

## Statement

Can you find the answer to the same question if the cake has the shape of a nine-sided nonagon? 

## Hint

Can you use the formula to find the answer for an eight sided shape so that you have all the values you need to find the answer for a nine sided shape? 

## Correct Answer

429

## Explanation

So far, the result for 3, 4, 5, 6, and 7 sides, the results of which are 1, 2, 5, 14, and 42 respectively). To find 8 sides we can do 42 + 1×14 + 2×5 + 5×2 + 14×1 + 42 = 132. Finally for 9 sides we have 132 + 1×42 + 2×14 + 5×5 + 14×2 + 42×1+132 = 429 

# Additional information

## About

These Cₙ are called *Catalan numbers* and they are crucial in the world of combinatorics. There is an explicit formula for them, but finding it goes much beyond our scopes: the above recursive definition is more than enough for now! Interestingly there are many different puzzles that lead to these numbers (more than 200!) … perhaps you have seen another puzzle with the same answers?

## References

* https://garethrees.org/2013/06/11/tabular/

