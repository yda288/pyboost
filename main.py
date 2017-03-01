from mypy.main import *
from mypy.nodes import FuncDef
import argparse



def process_cmd(args):
    parser = argparse.ArgumentParser(description='pyboost')
    parser.add_argument('-file', action="store", dest="filename")
    parser.add_argument('-module', action="store", dest="module")
    parser.add_argument('-func', action="store", dest="func", type=str)
    opts = parser.parse_args()
    return opts

def parse(opts):
    print(opts)
    sources, options = process_options([opts.filename])
    res = type_check_only(sources, None, options)

    funcs = filter(lambda f:
                   isinstance(f, FuncDef) and f.fullname() == '%s.%s' % (opts.module, opts.func),
                   res.manager.modules[opts.module].defs
                   )
    return funcs

def main(args):
    opts = process_cmd(args)
    print(opts)
    funcs = parse(opts)
    return list(funcs)
    #print(res)

if __name__ == "__main__":
    funcs = main(sys.argv[1:])