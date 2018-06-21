class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.row = 0
        self.col = 0
        if len(vec2d) == 0 or len(vec2d[0]) == 0:
            self.row = -1

    # @return {int} a next element
    def next(self):
        val = self.vec2d[self.row][self.col]
        self.col += 1
        if self.col >= len(self.vec2d[self.row]):
            self.col = 0
            self.row += 1
            if self.row >= len(self.vec2d):
                self.row = -1
                
        return val

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        return self.row > -1
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())