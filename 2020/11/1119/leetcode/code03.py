# Valid Square
# 4변 길이체크(with set) - 2개 개 같은 길이, 1개 길이 0, 1개 대각선
# 대각선 길이 및 그 중간점 확인
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p_set = set()
        for i in p1,p2,p3,p4:
            p_set.add((i[0],i[1]))
            
        if len(p_set) < 4:
            return False

        # check
        
        max_arr = []
        for i in p_set:
            x,y = i
            max_dist = 0
            mid_point = [0,0]
            dist_set = set()
            for j in p_set:
                dist = (i[0]-j[0])**2 + (i[1]-j[1])**2
                dist_set.add(dist)
                if max_dist < dist:
                    max_dist = max(dist,max_dist)
                    mid_point = [(i[0]+j[0])/2, (i[1]+j[1])/2]
            if len(dist_set) != 3:
                return False
            max_arr.append((max_dist,mid_point))
        
        for i in max_arr[1:]:
            dist, mid = i
            if dist != max_arr[0][0] or mid != max_arr[0][1]:
                return False
        return True

# dist set 이 2 개만 나옴 !
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1,p2,p3,p4]
        distances = set()
        for i in range(4):
            for j in range(i+1, 4):
                distances.add(self.distance(points[i], points[j]))
        print(distances)
        return len(distances) == 2 and 0 not in distances
    
    def distance(self, p1, p2):
        return sum((p1[i]-p2[i])**2 for i in range(len(p1)))

# 각 꼭지점과의 길이 array
# 변4개 길이 체크
# 대각선 길이 체크
# 대각선 - 변과 거리체크
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        distances = []
        points = [p1, p2, p3, p4]
        for i in range(4):
            for j in range(i + 1, 4):
                p, q = points[i], points[j]
                distances.append((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
        
        if distances[0] == 0:
            return False
        
        distances.sort()
        for i in range(3):
            if distances[i] != distances[i + 1]:
                return False
        
        if distances[-1] != distances[-2]:
            return False
        
        if distances[-1] != 2 * distances[0]:
            return False
        
        return True

# sort 후 p1 p4 는 대각선!? 맞음!!
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
     
        coordinates = [p1,p2,p3,p4]
        distinct_points = set([(i[0],i[1]) for i in coordinates])
        if len(distinct_points)<4: 
            return False 
        coordinates.sort()
        p1,p2,p3,p4 = coordinates[0],coordinates[1],coordinates[2],coordinates[3]
        diagonal_length_1 = (p1[0]-p4[0])**2 + (p1[1]-p4[1])**2
        diagonal_length_2 = (p2[0]-p3[0])**2 + (p2[1]-p3[1])**2
        s1 = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 
        s2 = (p1[0]-p3[0])**2 + (p1[1]-p3[1])**2 
        s3 = (p4[0]-p2[0])**2 + (p4[1]-p2[1])**2 
        s4 = (p4[0]-p3[0])**2 + (p4[1]-p3[1])**2 
        if s1==s2 and s2==s3 and s3==s4 and diagonal_length_1==diagonal_length_2 and s1 + s2==diagonal_length_1: 
            return True 
        else: 
            return False


# 한 꼭지점과 다른꼭지점 길이 sorted array 생성
#  -> 2개 같고, 1개 대각선
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = set()
        for p in [p1,p2,p3,p4]:
            t = tuple(p)
            if t in points:
                return False
            points.add(t)
        
        def dist(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
        
        distances = sorted([(dist(p1, p), p) for p in [p2, p3, p4]])
        
        a,b = distances[0], distances[1]
        if a[0] != b[0]:
            return False
        
        s = distances[-1][1]
        if dist(s,a[1]) != a[0] or dist(s, b[1]) != b[0]:
            return False
        
        if dist(a[1],b[1]) != distances[-1][0]:
            return False
        
        return True

# (root 하지 않음)
# 변길이 4개 동일
# 대각선 2개 길이 동일
# 변길이 *2 == 대각선 이여야함 
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Idea: In any square there will be 4 lines of same length and 2 lines of same length
        p = [p1, p2, p3, p4]
        sides = []
        for i in range(4):
            for j in range(i+1, 4):
                if p[i] == p[j]:
                    print(p[i], p[j])
                    return False
                sides.append((p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2)
        sides.sort()
        return (sides[0] == sides[1] == sides[2] == sides[3]) and (sides[4] == sides[5]) and (sides[0] * 2 == sides[-1])