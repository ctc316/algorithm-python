def closest(s, queries):
    pos_map = {}
    for i, v in enumerate(s):
        if v not in pos_map:
            pos_map[v] = []

        pos_map[v].append(i)

    res = []
    for q in queries:
        if q < 0 or q >= len(s):
            res.append(-1)
            continue

        ch = s[q]
        if ch not in pos_map:
            res.append(-1)
            continue

        indices = pos_map[ch]
        idx = -1
        closest = float("Inf")
        for i in indices:
            if i == q:
                continue

            if abs(i - q) < closest:
                closest = abs(i - q)
                idx = i 

        res.append(idx)

    return res
