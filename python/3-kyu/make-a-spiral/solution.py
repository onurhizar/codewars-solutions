def spiralize(size):
    eC,fC = 0,1                                                 # characters of emptyCell and filledCell
    spiral = [[eC for j in range(size)] for i in range(size)]   # step 1: create an empty nxn array with dots
    spiral[0] = [fC for i in range(size)]                       # step 2: fill three edges (top, bottom, right)
    spiral[size-1] = [fC for i in range(size)]
    for i in range(size): spiral[i][size-1] = fC

    horizontalMovement = False  # True: up/down   False: right/left
    r,c = size-1, 0             # row, column for the position
    v,h = 1,1                   # vertical 1:right -1:left,   horizontal 1:up -1:down

    while True:
        if not horizontalMovement: # vertical movement
            for i in range(1,size):
                if spiral[r-(i+1)*v][c] != fC: spiral[r-i*v][c] = fC # if next cell is not empty, fill this
                else: 
                    r = r-(i-1)*v   # update the row with last successful position (y axis)
                    horizontalMovement = not horizontalMovement
                    v*=-1
                    break
        elif horizontalMovement:    # horizontal movement
            for i in range(1,size):
                if spiral[r][c+(i+1)*h] != fC: spiral[r][c+i*h] = fC # if next cell is not empty, fill this
                else: 
                    c = c+(i-1)*h   # update the col with last successful position (x axis)
                    h*=-1
                    horizontalMovement = not horizontalMovement
                    break
        if size%2==1: # if size is an odd number, check four sides of the last position
            if spiral[r][c+2] == spiral[r][c-2] == spiral[r+2][c] == spiral[r-2][c] == fC: return spiral
        elif spiral[r-v][c+2*h]==fC: return spiral # if size is an even number, check the neighbor of the next cell

def printSpiral(spiral):
    for row in spiral:
        [print(j, end=' ') for j in row]
        print()

#printSpiral(spiralize(11)) # for testing
