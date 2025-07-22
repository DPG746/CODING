def isPalindrome(s:str)->bool:
        s=''.join(c.lower() for c in s if c.isalnum())
        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    
user_input=input("Enter a string")
result=isPalindrome(user_input)
if result:
        print("Its Plaindrome")
else:
        print("Not Palindrome")
