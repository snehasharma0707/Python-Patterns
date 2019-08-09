# for the pattern of type
#      *
#     * *
#    * * *
#   * * * *

i=int(input("Number of lines in pattern?"))
j=1
while i>=1:
    print((' ' * (i-1)) + ('* ' * j ) )
    j=j+1
    i=i-1
