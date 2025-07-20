def check_for_target(nums,target):
    left=0
    right=len(nums)-1

    while left<right:
        curr=nums[left]+nums[right]
        if curr==target:
            return [left,right]
        if curr>target:
            right-=1
        else:
            left+=1

    return None



# Take input from the user
user_input = input("Enter a array")
nums=list(map(int,user_input.strip().split()))
target=int(input("Enter the target sum:"))
result=check_for_target(nums,target)
# Call the function and print the result
if result:
    print(result)
else:
    print("None")
