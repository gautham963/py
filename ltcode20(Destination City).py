#You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sec_set = set(path[1] for path in paths)
        fir_set = set(path[0] for path in paths)
        ans = sec_set - fir_set
        return ans.pop()
