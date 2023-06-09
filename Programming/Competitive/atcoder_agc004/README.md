# C - AND Grid { [AtCoder AGC004](https://atcoder.jp/contests/agc004/tasks/agc004_c?lang=en) }

- _**Time Limit:**_ 2 sec
- _**Memory Limit:**_ 256 MB

## Problem Statement

Snuke and Ciel went to a strange stationery store. Each of them got a transparent graph paper with $H$ rows and $W$ columns.

Snuke painted some of the cells red in his paper. Here, the cells painted red were 4-connected, that is, it was possible to traverse from any red cell to any other red cell, by moving to vertically or horizontally adjacent red cells only.

Ciel painted some of the cells blue in her paper. Here, the cells painted blue were 4-connected.

Afterwards, they precisely overlaid the two sheets in the same direction. Then, the intersection of the red cells and the blue cells appeared purple.

You are given a matrix of letters $a_{ij} ​(1 ≤ i ≤ H , 1 ≤ j ≤ W)$ that describes the positions of the purple cells. If the cell at the $i$-th row and $j$-th column is purple, then $a_{ij}$ is `#`, otherwise $a_{ij}$ is `.`. Here, it is guaranteed that **no outermost cell is purple.** That is, if $i=1, H$ or $j=1, W,$ then $a_{ij}$ is `.`.

Find a pair of the set of the positions of the red cells and the blue cells that is consistent with the situation described. It can be shown that a solution always exists.

## Constraints

- $3≤H,W≤500$
- $a_{ij}$ is `#` or `.`
- If $i=1, H$ or $j = 1, W$, then $a_{ij}$ is `.`
- At least one of $a_{ij}$ is `#`

## Input

The input is given from Standard Input in the following format:

$H \hspace{1em} W\newline
a_{11}...a_{1W}\newline
:\newline
a_{H1}...a_{HW}\newline
$

## Output

Print a pair of the set of the positions of the red cells and the blue cells that is consistent with the situation, as follows:

- The first $H$ lines should describe the positions of the red cells.
- The following $1$ line should be empty.
- The following $H$ lines should describe the positions of the blue cells.

The description of the positions of the red or blue cells should follow the format of the description of the positions of the purple cells.

## Sample Input 1

```
5 5
.....
.#.#.
.....
.#.#.
.....
```

## Sample Output 1

```
.....
#####
#....
#####
.....

.###.
.#.#.
.#.#.
.#.#.
.....
```

One possible pair of the set of the positions of the red cells and the blue cells is as follows:

![image from https://atcoder.jp/contests/agc004/tasks/agc004_c?lang=en](./images/C_1.png)

## Sample Input 2

```
7 13
.............
.###.###.###.
.#.#.#...#...
.###.#...#...
.#.#.#.#.#...
.#.#.###.###.
.............
```

## Sample Output 2

```
.............
.###########.
.###.###.###.
.###.###.###.
.###.###.###.
.###.###.###.
.............

.............
.###.###.###.
.#.#.#...#...
.###.#...#...
.#.#.#.#.#...
.#.#########.
.............
```

One possible pair of the set of the positions of the red cells and the blue cells is as follows:

![https://atcoder.jp/contests/agc004/tasks/agc004_c?lang=en](./images/C_2.png)
