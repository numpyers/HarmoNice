"""
Input:
if(1<=x<3, 3,
2<=x<4, 1,
5<=x<6, 2)

Output:
[(1,3,3),(2,4,1),(5,6,2)]
"""
s = '''if(0 <= x < 1, 261.63,
1 <= x < 2, 261.63,
2 <= x < 3, 392,
3 <= x < 4, 392,
4 <= x < 5, 440,
5 <= x < 6, 440,
6 <= x < 8, 392,
8 <= x < 9, 349.23,
9 <= x < 10, 349.23,
10 <= x < 11, 329.63,
11 <= x < 12, 329.63,
12 <= x < 13, 293.66,
13 <= x < 14, 293.66,
14 <= x < 16, 261.63)'''


def ranges_to_tuples(s: str):
    s = s[3:]
    lines = s.split("\n")
    for line in lines:
        line = line[:-1]
        div = line.split(',')
        temp = div[0].split('<')
        elements = tuple(map(float, (temp[0], temp[-1], div[-1])))
        print(elements)


ranges_to_tuples(s)
