import math
def maxArea(height):
    maxA = 0
    i = 0
    j = len(height) - 1
    while i < j:
        h = min(height[i], height[j]);
        maxA = max(maxA, h * (j - i));
        if height[i] < height[j]:
            i = i + 1
        else:
            j = j - 1
    print(int(maxA))
    return int(maxA)














if __name__ == '__main__':
    maxArea([1,8,6,2,5,4,8,3,7])
