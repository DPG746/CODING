def check_for_target(nums,target):
    left=0
    right=len(nums)-1

    while left<right:
        curr=nums[left]+nums[right]
        if curr==target:
            return True
        if curr>target:
            right-=1
        else:
            left+=1

    return false



# Take input from the user
user_input = input("Enter a array")
nums=list(map(int,user_input.strip().split()))
target=int(input("Enter the target sum:"))

# Call the function and print the result
if check_for_target(nums,target):
    print("True")
else:
    print("False")
