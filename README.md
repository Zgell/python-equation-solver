# python-equation-solver
A mathematical equation solver written in Python. It takes an algebraic equation as an input, then simplifies it and computes the answer.

To onlookers of this project, ignore this for now. This is a test to verify that Git is working for me.

However, I do intend to further develop this project over time.

**Sept. 24, 2020** - The project is semi-functional. Certain equations work, certain ones don't. I will investigate the issues a bit later, but this might also require a complete overhaul of the algorithm as its current implementation is getting a little bit too complicated to debug easily. It doesn't handle negative numbers very well, but I'm working on fixing that.

NOTE: One thing I would like to make clear to anyone reading the code is that I am *purposely* avoiding regex expressions. I'm doing this because I intend to rewrite the algorithms employed in this program in another language, and I'm trying to minimize the number of features exclusive to Python (ie. list comprehension) so that when I rewrite this in another language, I don't need to spend as much time recreating Python's functionality just to make it work. I guess it also serves as a sort of challenge to see if the algorithm can be made without doing it the easy way.
