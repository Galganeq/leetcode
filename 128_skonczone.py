def longestConsecutive(nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        nums_set = set(nums)
        current_longest = 0.
        for num in nums_set:
                if (num - 1) not in nums_set:

                        current_longest = 1
                        while (num + current_longest) in nums_set:
                                current_longest = current_longest + 1   
                 
                        longest = max(longest, current_longest)
        return longest
            
nums = [100,4,200,1,3,2]
print(nums)
print(longestConsecutive(nums))






















        # nums.sort()
        # print(nums)
        # liczby = []
        # previous = 0
        # for i in nums:
        #         if (((i - 1) == previous) or (i == previous)):
        #                 liczby.append(i)
        #         else:
                     
        #              break
        #         previous = i
        # print(len(liczby))