class Solution:
    
    MOVE = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        source = self.matrixToString(init_state)
        target = self.matrixToString(final_state)
        
        from queue import Queue
        q = Queue()
        hash = set()
        
        q.put(source)
        hash.add(source)
        
        steps = 0
        while not q.empty():
            for i in range(q.qsize()):
                state = q.get()
                if state == target:
                    return steps
                
                for next in self.exploreNext(state):
                    if next in hash:
                        continue
                    
                    q.put(next)
                    hash.add(next)
                
            steps += 1
            
        return -1

    

    def matrixToString(self, state):
        s = ""
        for i in range(3):
            for j in range(3):
                s += str(state[i][j])
        
        return s


    def exploreNext(self, state):
        # find 0
        zeroIdx = state.find("0")
        row = int(zeroIdx / 3)
        col = zeroIdx % 3
        
        results = []
        for m in self.MOVE:
            row_ = row + m[0]
            col_ = col + m[1]
            
            if row_ < 0 or row_ > 2 or col_ < 0 or col_ > 2:
                continue
            
            nextIdx = row_ * 3 + col_
            nextState = state[:zeroIdx] + state[nextIdx] + state[zeroIdx + 1:]
            nextState = nextState[:nextIdx] + '0' + nextState[nextIdx + 1:]
            results.append(nextState)
        
        return results