# for the pattern of type
#  * * * *
#   * * *
#    * *
#     *

i=1
j=int(input("Number of lines in pattern?"))
while j>=1:
    print((' ' * (i-1)) + ('* ' * j ) )
    j=j-1
    i=i+1
