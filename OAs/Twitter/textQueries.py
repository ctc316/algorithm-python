def textQueries(sentences, queries):
    sentences = [set(s.split(" ") for s in sentences)]
    queries = [q.split(" ") for q in queries]
    res = []
    for q in queries:
        matches = []
        for i in range(len(sentences)):
            isMatch = True
            for w in q:
                if w not in sentences[i]:
                    isMatch = False
                    break

            if isMatch:
                matches.append(i)

        res.append(matches)

    return res