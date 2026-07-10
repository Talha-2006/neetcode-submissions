class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s = []

        for i in range(len(position)):
            pos = position[i]
            s = speed[i]
            p_s.append((pos, s))

        p_s = sorted(p_s, reverse=True)

        fleets = 1

        prev = p_s[0]

        for i in range(1, len(p_s)):
            curr = p_s[i]

            prev_calc = (target - prev[0]) / prev[1]
            curr_calc = (target - curr[0]) / curr[1]

            if prev_calc < curr_calc:
                fleets += 1
                prev = curr
            

        return fleets



        #p_s = [(4, 1), (2, 3), (0, 2)]

        #calcs = [6, 2.6, 5]
        