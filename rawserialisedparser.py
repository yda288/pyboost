
from rawserialised import *
from boostmappings import mappings
# def walk_args(func):
#     #filter(lambda f: isinstance(f, FuncDef), funcs)
#     for arg in func.arguments:
#         if arg.variable:
#
#         func.arguments[1].variable.type.type.fullname()
#         func.arguments[0].variable.type.args[0].items[0].type.fullname()
#
#         arg.variable

# if 'args' in arg:
#     chain = mapped(arg['type_ref']) + str([chain_nested(a) for a in arg['args']])
#     nested_args.append(chain)
# else:
#     chain = chain_nested(arg)
#     nested_args.append(chain)

def parse(serialised):
    nested_args = []
    nested_ret = []

    ##parse arg types
    try:
        for arg in serialised['type']['arg_types']:
            chain = chain_nested(arg)
            nested_args.append(chain)
    except:
        nested_args.append('None')

    ##parse return types
    try:
        nested_ret.append(chain_nested(serialised['type']['ret_type']))
    except:
        nested_ret.append('None')
    return (nested_ret, nested_args)

def chain_nested(arg):
    try:
        if 'args' in arg:
            return '%s%s' % (mapped(arg['type_ref']),[chain_nested(a) for a in arg['args']])
        elif 'items' in arg:
            return '%s%s' % (mapped(arg['fallback']['type_ref']), [chain_nested(i) for i in arg['items']])
        elif 'item' in arg:
            return chain_nested(arg['item'])
        else:
            return mapped(arg['type_ref'])
    except:
        return 'None'

def mapped(builtin):
    return mappings.get(builtin, builtin)

if __name__ == '__main__':
    p = parse(inproduct)
    print(p)