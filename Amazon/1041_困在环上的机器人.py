

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        point = [0,0] 
        left = 0 
        right = 0
        up = 1
        down = 0
        instructions = instructions*4
        for ins in instructions:
            if ins == 'G':
                if up == 1:
                    point[1] += 1 
                if down == 1:
                    point[1] -= 1
                if right == 1:
                    point[0] += 1 
                if left == 1:
                    point[0] -= 1 
            elif ins == 'L':
                if up == 1:
                    left = 1 
                    up = 0
                elif down == 1:
                    right = 1
                    down = 0
                elif left == 1:
                    down = 1
                    left = 0
                elif right == 1:
                    up = 1
                    right = 0
            elif ins == 'R':
                if up == 1:
                    right = 1
                    up = 0
                elif down == 1:
                    left = 1
                    down = 0
                elif left == 1:
                    up = 1
                    left = 0
                elif right == 1:
                    down = 1
                    right = 0 
        if point[0]== 0 and point[1] == 0:
            return True
        else:
            return False