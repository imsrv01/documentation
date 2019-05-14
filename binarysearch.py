'''
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.

Assumption : No duplicates exists..
'''

class binarySearch:
    def __init__(self, searchList):
        self.searchList = searchList
        
    def search(self, target):
        list1 = self.searchList
        left=0
        right=len(list1)-1
        while left <= right:
            pivot = int((left + right)/2)
            print(list1[pivot])
            if list1[pivot] == target:
                return pivot
            else:
                if list1[pivot] < target:
                    left = pivot + 1
                else:
                    right = pivot - 1
        return -1                
            
list1 = [1, 2, 3,4,5]
target=6
bs = binarySearch(list1)
index = bs.search(target)
if str(index) == "-1":
    print("Target " + str(target) + " not found in given sorted array")
else: 
    print("Target " + str(target) + " found in given sorted array at position " + str(index))

        
