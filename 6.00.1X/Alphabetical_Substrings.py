""" prints the longest substring of s in which the letters occur in alphabetical order"""
def alphabetical_substrings(string):
    """ prints the longest substring of s in which the letters occur in alphabetical order"""
    max_substring = ''
    max_number = 1
    for i in range(len(string)):
        count = 1
        index = i
        substring = string[index]
        try:
            while string[index] <= string[index + 1]:
                count += 1
                substring = substring + string[index + 1]
                index += 1                
            if max_number < count: 
                max_number = count
                max_substring = substring
        except IndexError:
            count += 0
    print('Longest substring in alphabetical order is: ' + max_substring)
alphabetical_substrings('azcbobobegghakl')
