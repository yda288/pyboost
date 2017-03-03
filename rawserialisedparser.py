
from rawserialised import *
from boostmappings import mappings

class Parser:
    def __init__(self, funcs):
        self.funcs = funcs
        self.parsed = []

    def parse(self):
        for func in self.funcs:
            self.parsed.append(Parser._parse(func))

    ##static methods below as they do not require instance state
    @staticmethod
    def _parse(serialised):
        nested_args = []
        nested_ret = []

        ##parse arg types
        try:
            for arg in serialised['type']['arg_types']:
                chain = Parser._chain_nested(arg)
                nested_args.append(chain)
        except:
            nested_args.append('None')

        ##parse return types
        try:
            nested_ret.append(Parser._chain_nested(serialised['type']['ret_type']))
        except:
            nested_ret.append('None')
        return (nested_ret, nested_args)

    @staticmethod
    def _chain_nested(arg):
        try:
            if 'args' in arg:
                return '%s%s' % (Parser._mapped(arg['type_ref']),[Parser._chain_nested(a) for a in arg['args']])
            elif 'items' in arg:
                return '%s%s' % (Parser._mapped(arg['fallback']['type_ref']), [Parser._chain_nested(i) for i in arg['items']])
            elif 'item' in arg:
                return Parser._chain_nested(arg['item'])
            else:
                return Parser._mapped(arg['type_ref'])
        except:
            return 'None'

    @staticmethod
    def _mapped(builtin):
        return mappings.get(builtin, builtin)


if __name__ == '__main__':
    parser = Parser([inproduct])
    parser.parse()
    print(parser.parsed)