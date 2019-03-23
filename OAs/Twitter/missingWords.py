def missingWords(s, t):
    s = s.split(" ")
    t = t.split(" ")
    n = len(s)
    m = len(t)
    p_s = 0
    p_t = 0
    res = []
    while p_t < m:
        while t[p_t] != s[p_s]:
            res.append(s[p_s])
            p_s += 1

        p_t += 1

    while p_s < n:
        res.append(s[p_s])
        p_s += 1

    return res 
