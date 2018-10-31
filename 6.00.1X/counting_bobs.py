"""prints the number of times the string 'bob' occurs in string"""

def counting_bobs(string):
    """
    prints the number of times the string 'bob' occurs in string
    """
    count = 0
    for i in range(len(string) - 2):
        if string[i] == 'b' and string[i + 1] == 'o' and string[i + 2] == 'b':
            count += 1
    print("Number of times bob occurs is: " + str(count))
counting_bobs('bjbobbbqrboobbobfoboboioboobbobbbobbob')
