def area(rec1, rec2, rec3):
    def rectangle_area(x1,y1,x2,y2):
        return abs(x2 - x1) * abs(y2-y1)

    def pair_overlap_area(recX, recY):
        (x1,y1,x2,y2) = recX
        (x3,y3,x4,y4) = recY
        overlap_width = max(0, min(x2, x4) - max(x1, x3))  # check if intersect
        overlap_height = max(0, min(y1, y3) - max(y2, y4))
        overlap_area = overlap_width * overlap_height
        return overlap_area
    
    def triple_overlap_area(recA, recB, recC):
        x1, y1, x2, y2 = recA
        x3, y3, x4, y4 = recB
        x5, y5, x6, y6 = recC
        overlap_width = max(0, min(x2, x4, x6) - max(x1, x3, x5))
        overlap_height = max(0, min(y1, y3, y5) - max(y2, y4, y6))
        return overlap_width * overlap_height
    
    rectangles = [rec1, rec2, rec3]
    total_area = 0
    total_pair_overlap = 0
    
    for i in range(len(rectangles)):
        area = rectangle_area(*rectangles[i])
        for j in range(len(rectangles)):
            if i < j:
                overlap_area = pair_overlap_area(rectangles[i], rectangles[j])
                total_pair_overlap += overlap_area
        total_area += area
        
    return total_area - total_pair_overlap + triple_overlap_area(rec1, rec2, rec3)   

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16