# Competitive Programming Exercises/Problems Solving

![Image of many people in a programming competition, the image was found on google on mycplus website](../Assets/programming-competition.png)

## Base code

```cpp
// Include all libs is not a good practice,
// but it save writing time during the programming competition
#include<bits/stdc++.h>

using namespace std;

int main()
{
    /*
     ===    Fast-io
            when a exercise have many I/O, the
            TLE could happen in the start of problem

     - These command will works against these TLE problems caused by a bunch of I/O.
     - Using scanf/printf instead CIN and COUT could work also.
     */
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}
```

## Input Common Cases:

Read until finish:

```cpp
    int a, b, c;

    while(cin >> a >> b)
    {
        c = a + b;
        cout << c << endl;
    }
```

Number of predetermined test cases:

```cpp
    int t, a, b, c;
    cin >> t;
    while(t--)
    {
        cin >> a >> b;
        c = a + b;
        cout << c << endl;
    }
```

## Possible erros:

- **[TLE]** Time Limit Exceed: It happen when you algorithm exceed the time of execution. The main problem with this error is that it will not allow you to know that your solution would reach to correct solution or not;

- **[PE] or [WA]** Presentation Error: Some judges do not have Presentation Error well implemented, e.g. if you print more `\n` or more space than necessary, it could return Wrong Answer instead Presentaton Error;

- **[WA]** Wrong Answer: It happen when the answer for the tests is wrong, or a possible (PA).

## Exercises List

| Type         | Description            | Problem Question Link                                                       | Solving                     |
| ------------ | ---------------------- | --------------------------------------------------------------------------- | --------------------------- |
| Stack        | Stack                  | [uri1068](https://www.beecrowd.com.br/judge/en/problems/view/1068)          | [C++](./uri1068/1068.cpp)   |
| Queue        | The Stock Span Problem | [letcode406](https://leetcode.com/problems/queue-reconstruction-by-height/) | [C++](./letcode406/406.cpp) |
| Logical      | Used cpp max()         | [uva11799](./uva11799/)                                                     | [C++](./uva11799/11799.cpp) |
| Stack/Object | Stack, Class & Object  | [uva12015](./uva12015/)                                                     | [C++](./uva12015/12015.cpp) |
