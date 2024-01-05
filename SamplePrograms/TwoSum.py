"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
>>> twoSum([2,7,11,15],13)
(0, 2)
>>> twoSum([3,2,4],6)
(1, 2)
"""


def twoSum( nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return(num_dict[complement],i)
            
            num_dict[num] = i
        return []

if __name__ == '__main__':
     import doctest
     doctest.testmod()