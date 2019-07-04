class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplifyPath(self, path):
        cmds = path.strip().split("/")
        dirs = []
        for c in cmds:
            if c == '' or c == '.':
                continue
            elif c == '..':
                if len(dirs) > 0:
                    dirs.pop()
            else:
                dirs.append(c)

        return "/" + "/".join(dirs)