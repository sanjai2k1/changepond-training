maps = {0:"1",2:"2",1:"1"}
keys=list(maps.keys())
keys.sort()
maps={i:maps[i] for i in keys}
print(maps)
