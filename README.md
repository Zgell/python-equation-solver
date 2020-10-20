# Python Equation Solver (version 2 alpha)
A mathematical equation solver written in Python. It takes an algebraic equation as an input, then simplifies it and computes the answer.
With the project in its current state, I may potentially rewrite the algorithm from the ground up, as it is getting a little bit complicated to analyze with all of its recursive elements.

I do intend to develop this project further sometime in the future.

NOTE: One thing I would like to make clear to anyone reading the code is that I am *purposely* avoiding regex expressions. I'm doing this because I intend to rewrite the algorithms employed in this program in another language, and I'm trying to minimize the number of features exclusive to Python (ie. list comprehension) so that when I rewrite this in another language, I don't need to spend as much time recreating Python's functionality just to make it work. I guess it also serves as a sort of challenge to see if the algorithm can be made without doing it the easy way.

**Oct. 20, 2020** - I've decided to rebuild my implementation of the equation solving algorithm from the ground up. I had a look at my implementation and it had a lot of flaws that I don't think could be realistically overcome with my previous implementation. Depending on recursion was not a great idea because although it solves the issue of nested equations nicely, it makes debugging the algorithm a nightmare. One of the biggest limitations of the previous algorithm was the inability to handle multiple parentheses groups in parallel. See the example below.

```
y = a + (b * c) + (d * e)
```

The algorithm could only solve the first set of brackets, or the `(b * c)` term. What I'm looking for is an algorithm that could compute the following:

```
y = a * (b + (c * d) - e) + f + g * (h - i)
```

In other words, my motivation for rebuilding the algorithm was that I wanted an algorithm that could handle both nested equations and multiple parentheses groups in parallel at the same time.

My current approach for the algorithm is to utilize some object-oriented programming techniques (something I was NOT using in the last one) to manage the data organization in a much neater way, making it easier to debug. I've also come up with a way for a program to recognize the different levels of equations, and thus I have a fundamental idea that I can build this algorithm around. The current approach is to use something I'm calling a "level map", which is basically a character-by-character sequence of the raw input equation that gives the user the "level" of the equation at any point in the equation. The "level" is an integer value that indicates how many levels of equations deep a certain point goes.

An example of what a level map for a certain equation looks like:

```
Equation: 2+(3*8*(9-1-1)/4)-3^(1+1+0+1)
LevelMap: 00111112222221110000111111110
```

The level map can be used to easily identify the innermost set of parentheses easily by finding the maximum in the sequence. It also identifies all of the nested equations as opposed to just the first one. This approach is already significantly better than the first version of this algorithm.

**Sept. 24, 2020** - The project is semi-functional. Certain equations work, certain ones don't. I will investigate the issues a bit later, but this might also require a complete overhaul of the algorithm as its current implementation is getting a little bit too complicated to debug easily. It doesn't handle negative numbers very well, but I'm working on fixing that.
