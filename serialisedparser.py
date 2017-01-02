# -*- coding: utf-8 -*-
from serialised import *

def parse(serialised):
    nested_args = []
    nested_ret = []
    try:
        for arg in serialised['type']['arg_types']:
            if 'args' in arg:
                chain = chain_nested(arg['args'][0])
                nested_args.append(chain)
            else:
                #print(arg)
                chain = chain_nested(arg)
                nested_args.append(chain)
    except:
        nested_args.append('None')
    try:
        nested_ret.append(chain_nested(serialised['type']['ret_type']))
    except:
        nested_ret.append('None')
    return (nested_ret, nested_args)

def chain_nested(arg):
    #print(arg)
    try:
        if 'args' in arg:
            return arg['boost_map'] + str([chain_nested(a) for a in arg['args']])
        elif 'items' in arg:
            return arg['boost_map'] + str([chain_nested(i) for i in arg['items']])
        elif 'item' in arg:
            return chain_nested(arg['item'])
        else:
            return arg['boost_map']
    except:
        return 'None'


if __name__ == '__main__':
    p = parse(mapped_max_np_array)
    print(str(p))