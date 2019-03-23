def decode(codes, encodes):
    codeMapping = {}
    for val, code in enumerate(codes):
        codeMapping[code] = val

    codeLeng = len(codes[0])
    res = ""
    for i in range(0, len(encodes, codeLeng)):
        res += codeMapping[encodes[i:i + codeLeng]]

    return res
