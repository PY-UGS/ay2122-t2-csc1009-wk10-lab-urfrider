# Question 2c from Laboratory Wk01
# loop from 102 to 66 in descending order
for i in range(102, 65, -1):
    # if the number modulo 2 is greater than 0 is an odd number
    if i % 2 > 0:
        # print the odd numbers
        print(i, end=" ")