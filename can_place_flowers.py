

class Solution:

    def canPlaceFlowers(self, flowerbed, n: int) -> bool:

        if len(flowerbed) == 1:
            if n > 1:
                return False
            if n == 1 and flowerbed[0] == 0:
                return True
            if n == 1 and flowerbed[0] != 0:
                return False

        if n == 0:
            return True

        for i in range(0, len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                return self.canPlaceFlowers(flowerbed, n-1)

            if i == len(flowerbed) - 1 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                return self.canPlaceFlowers(flowerbed[i], n-1)

            if i > 1 and i < len(flowerbed) - 1 and flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                return self.canPlaceFlowers(flowerbed, n-1)

        return False

Sol = Solution()
