'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        inverted = {}
        for doc in docs:
            duplicate = set()
            for word in doc.content.split(" "):
                if not word or word in duplicate:
                    continue

                duplicate.add(word)

                if word not in inverted:
                    inverted[word] = [doc.id]
                else:
                    inverted[word].append(doc.id)

        return inverted