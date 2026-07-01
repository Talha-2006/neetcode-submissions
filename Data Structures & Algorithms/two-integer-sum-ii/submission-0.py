class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #[1,2,3,4]

        left_pointer = 0
        right_pointer = len(numbers) - 1 

        while left_pointer < right_pointer:
            curr_sum = numbers[left_pointer] + numbers[right_pointer]

            if curr_sum == target and left_pointer != right_pointer:
                return [left_pointer + 1, right_pointer + 1]
            
            elif curr_sum < target:
                left_pointer += 1
            else:
                right_pointer -= 1
        