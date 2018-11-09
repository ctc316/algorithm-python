class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_word = True


    def find(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return node.is_word


    def start_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False

            node = node.children[ch]

        return True

class Solution:

    def __init__(self):
        self.MOVES = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        n = len(board)
        if n == 0 or len(words) == 0:
            return []
        m = len(board[0])
        if m == 0:
            return []
        trie = Trie()
        for w in words:
            trie.add(w)

        results = set()
        for i in range(n):
            for j in range(m):
                results.update(self.dfs(board, n, m, i, j, trie))

        return list(results)


    def dfs(self, board, n, m, i, j, trie):
        stack = []
        visited = set()
        results = []

        stack.append((i, j, 0, board[i][j]))

        while len(stack) > 0:
            x, y, move_idx, curr_str = stack.pop()

            if trie.find(curr_str):
                results.append(curr_str)

            visited.add(x * m + y)

            is_next = False
            for idx in range(move_idx, len(self.MOVES)):
                x_ = x + self.MOVES[idx][0]
                y_ = y + self.MOVES[idx][1]

                if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:
                    continue

                next_str = curr_str + board[x_][y_]
                if x_ * m + y_ in visited:
                    continue

                if trie.start_with(next_str):
                    stack.append((x, y, idx + 1, curr_str))
                    stack.append((x_, y_, 0, next_str))
                    is_next = True
                    break

            if not is_next:
                visited.remove(x * m + y)

        return results




