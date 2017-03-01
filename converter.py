from boostmappings import mappings

def join(arglist):
    joined=[]
    for arg in arglist:
        if arg not in mappings.values():
            arg = arg.replace('[','<').replace(']','>').replace("'",'')
        joined.append(arg)
    print(joined)
    return joined
