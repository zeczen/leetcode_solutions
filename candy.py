# https://leetcode.com/problems/candy
class Solution:
    def candy(self, ratings):
        def fix(i):
            if candies[i - 1] < 1:
                candies[i - 1] = 1
                for j in range(i - 1, 0, -1):
                    if ratings[j - 1] <= ratings[j]:
                        break
                    if candies[j - 1] <= candies[j]:
                        candies[j - 1] = candies[j] + 1

        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                fix(i)
                candies[i] = candies[i - 1] + 1
            elif ratings[i - 1] > ratings[i]:
                candies[i] = min(candies[i - 1] - 1, 1)
            elif ratings[i - 1] == ratings[i]:
                fix(i)
                candies[i] = 1
        fix(len(ratings))
        return sum(candies)
