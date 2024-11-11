seq = "aAbBcCdD"
result = list(map(lambda x: x.upper() if x.islower() else x.lower(), set(seq)))
print(result)
