class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # if rec1 left < rec2 right and rec1 right > rec2 left
        # rec 1 top > rec 2 bot and rec 2 top > rec 1 bot
        return rec1[0] < rec2[2] and rec1[2] > rec2[0] and rec1[3] > rec2[1] and rec1[1] < rec2[3]
