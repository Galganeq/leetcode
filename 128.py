def longestConsecutive(nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        liczby = []
        previous = 0
        for i in nums:
                if (((i - 1) == previous) or (i == previous)):
                        liczby.append(i)
                else:
                     
                     break
                previous = i
        print(len(liczby))
            
nums = [100,4,200,1,3,2]
longestConsecutive(nums)