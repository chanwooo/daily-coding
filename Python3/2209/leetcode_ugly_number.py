class Solution:
    def isUgly(self, x: int) -> bool:
        if x < 1:
            return False
        factors = []
        d = 2
        while d <= x:
            if x % d == 0:
                factors.append(d)
                x = x / d
            else:
                d = d + 1
            if d >= 7:
                return False
        return True

    def isUgly2(self, x):
        if x < 1:
            return False

        for i in [2, 3, 5]:
            while x % i == 0 < x:
                x /= i

        return x == 1


sol = Solution
print(sol.isUgly(sol, 14))
print(sol.isUgly(sol, 6))
print(sol.isUgly(sol, 1))
print(sol.isUgly(sol, -2147483648))

print(sol.isUgly2(sol, 120))
