'''counts up the number of vowels contained in the string'''
def counting_vowels(string):
    '''
    counts up the number of vowels contained in the string
    '''
    count = 0
    for i in string:
        if i in 'aeiou':
            count += 1
    print("Number of vowels: "+str(count))
counting_vowels('azcbobobegghakl')
