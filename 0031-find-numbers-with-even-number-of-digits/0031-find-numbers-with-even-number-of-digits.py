import numpy as np
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count=sum((1 for i in nums if len(str(i))%2==0))
        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna