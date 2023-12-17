def field(items, *spec, key=0): 
    assert len(spec) > 0, "Параметры обязательно указывать"
    if len(spec) == 1:
        ans = []
        for i in range(len(items)-1):
            if items[i].get(spec[0]) != None : ans.append(items[i].get(spec[0]))
        if items[i+1].get(spec[0]) != None : ans.append(items[i+1].get(spec[0]))
        return ans
    else:
        for it in items:
            tdict = {}
            for sp in spec:
                if it.get(sp) != None : tdict[sp] = it.get(sp)
            if len(tdict.keys()) != 0 : return(tdict)
            
if __name__ == "__main__":
    cars = [
        {'name' : 'bmw', 'price' : 10000, 'max_speed' : 300, 'hpower' : 650},
        {'name' : 'audi', 'price' : 9000, 'max_speed' : 250, 'hpower' : 400, 'color' : 'red'},
        {'name' : 'mercedes', 'price' : 15000, 'max_speed' : 270, 'hpower' : 4000, 'color' : 'green'}
    ]

    print(field(cars, 'name', 'price'))