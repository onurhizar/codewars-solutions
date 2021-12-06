def triangle(row):
    colors = {"R":0, "G":1, "B":2, 0:"R", 1:"G", 2:"B"}
    def merge(a, b): return colors[(-colors[a]-colors[b])%3] # returns the result color by using modulo
    if len(row)==1: return row
    section=[3**i+1 for i in range(10,-1, -1)] # 3**n+1 thanks to the video, descending order
    for length in section: # try each section from bigger to smaller
        while len(row)>=length: # if row is bigger than section, process
            if len(row)==length: return merge(row[0], row[-1])
            row = [merge(row[i], row[i+length-1]) for i in range(len(row)-length+1)]
    return row[0]
