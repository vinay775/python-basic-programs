def remove_vowels(a):
    ans = ''
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in a:
        if i in vowels:
            continue
        ans += i
    return ans
word = input("Enter the word:")
print(remove_vowels(word))
