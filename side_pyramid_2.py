# for the pattern of type
#        *
#      * *
#    * * *
#  * * * *

i=int(input("Input Number of Lines in the Pattern"))
j=1
k=i
while j<=i:
    print((" "* (k-1)) + ("*" * j))
    j=j+1
    k=k-1