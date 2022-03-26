# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = int(input())
bc = int(input())
degree_sign = u'\N{DEGREE SIGN}'
print(str(round(math.degrees(math.atan(ab/bc))))+degree_sign)
