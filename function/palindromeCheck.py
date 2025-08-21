def checkPalindrome(str):
    rev =""
    for i in range(len(str)-1,-1,-1):
        rev = rev + str[i]

    if rev == str:
        print("its a palindrome string")
    else:
        print("its not a palindrome")

checkPalindrome("arko")
checkPalindrome("madam")