'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        BaseGFSClient.__init__(self)

        self.chunkSize = chunkSize
        self.fileToChunks = {}


    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        if filename not in self.fileToChunks:
            return

        ret = ""
        for idx in range(self.fileToChunks[filename]):
            ret += self.readChunk(filename, idx)

        return ret

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        chunkIdx = 0
        for i in range(0, len(content), self.chunkSize):
            self.writeChunk(filename, chunkIdx, content[i:i + self.chunkSize])
            chunkIdx += 1

        self.fileToChunks[filename] = chunkIdx
