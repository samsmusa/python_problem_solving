# with open('name.txt','w') as file:
#     for i in range(20): 
#         file.write(str(i).rjust(5))
#         file.write("\n")
#         # print(len(str(i)))
        

# def format(listval,space):
#     return str(listval[0]).rjust(space)+str(listval[1]).rjust(space)+str(listval[2]).rjust(space)+str(listval[3]).rjust(space)

def print_formatted(number,space):
    # "": decimal
    # x: hexadecimal
    # o: octal
    # b: binary
    bases = ["", "o", "x", "b"]
    numbers_formatted = [format(number, x).upper() for x in bases]
    return str(numbers_formatted[0]).rjust(space-1)+str(numbers_formatted[1]).rjust(space)+str(numbers_formatted[2]).rjust(space)+str(numbers_formatted[3]).rjust(space)
with open('name.txt','w') as file:
    for i in range(1,18):
        file.write(print_formatted(i,len(format(18, 'b'))+1))
        file.write("\n")
    
    
"""  
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
   
"""