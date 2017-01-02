from enum import Enum

ARG_KINDS = Enum( 'ARG_KINDS', 'ARG_POS ARG_OPT ARG_STAR ARG_NAMED ARG_STAR2')
# ARG_POS: positional
# ARG_OPT: optional argument (functions only, not calls)
# ARG_STAR: *arg argument
# ARG_NAMED: keyword argument x=y in call, or keyword-only function arg
# ARG_STAR2 **arg argument


mapped_inproduct = {'.class': 'FuncDef',
 'arg_kinds': [0, 0],
 'arg_names': ['v', 'arg2'],
 'flags': [],
 'fullname': 'test_def.inproduct',
 'name': 'inproduct',
 'type': {'.class': 'CallableType',
          'arg_kinds': [0, 0],
          'arg_names': ['v', 'arg2'],
          'arg_types': [{'.class': 'Instance',
                         'args': [{'.class': 'TupleType',
                                   'boost_map': 'tuple',
                                   'fallback': {'.class': 'Instance',
                                                'args': [{'.class': 'AnyType'}],
                                                'boost_map': 'tuple',
                                                'type_ref': 'builtins.tuple'},
                                   'implicit': False,
                                   'items': [{'.class': 'Instance',
                                              'boost_map': 'double',
                                              'type_ref': 'builtins.float'},
                                             {'.class': 'Instance',
                                              'boost_map': 'double',
                                              'type_ref': 'builtins.float'}]}],
                         'boost_map': 'vector',
                         'type_ref': 'builtins.list'},
                        {'.class': 'Instance',
                         'boost_map': 'string',
                         'type_ref': 'builtins.str'}],
          'fallback': {'.class': 'Instance',
                       'boost_map': None,
                       'type_ref': 'builtins.function'},
          'implicit': False,
          'is_classmethod_class': False,
          'is_ellipsis_args': False,
          'name': '"inproduct"',
          'ret_type': {'.class': 'Instance',
                       'args': [{'.class': 'TypeType',
                                 'item': {'.class': 'Instance',
                                          'boost_map': 'Foo',
                                          'type_ref': 'foo.Foo'}}],
                       'boost_map': 'vector',
                       'type_ref': 'builtins.list'},
          'variables': []}}





mapped_builtins_only = {'.class': 'FuncDef',
 'arg_kinds': [0, 0],
 'arg_names': ['arg2', 'arg3'],
 'flags': [],
 'fullname': 'test_def.builtins_only',
 'name': 'builtins_only',
 'type': {'.class': 'CallableType',
          'arg_kinds': [0, 0],
          'arg_names': ['arg2', 'arg3'],
          'arg_types': [{'.class': 'Instance',
                         'boost_map': 'double',
                         'type_ref': 'builtins.float'},
                        {'.class': 'Instance',
                         'boost_map': 'int',
                         'type_ref': 'builtins.int'}],
          'fallback': {'.class': 'Instance',
                       'boost_map': None,
                       'type_ref': 'builtins.function'},
          'implicit': False,
          'is_classmethod_class': False,
          'is_ellipsis_args': False,
          'name': '"builtins_only"',
          'ret_type': {'.class': 'Instance',
                       'boost_map': 'complex',
                       'type_ref': 'builtins.complex'},
          'variables': []}}


mapped_void_method = {'.class': 'FuncDef',
 'arg_kinds': [0],
 'arg_names': ['arg'],
 'flags': [],
 'fullname': 'test_def.void_method',
 'name': 'void_method',
 'type': {'.class': 'CallableType',
          'arg_kinds': [0],
          'arg_names': ['arg'],
          'arg_types': [{'.class': 'Instance',
                         'boost_map': 'string',
                         'type_ref': 'builtins.str'}],
          'fallback': {'.class': 'Instance',
                       'boost_map': None,
                       'type_ref': 'builtins.function'},
          'implicit': False,
          'is_classmethod_class': False,
          'is_ellipsis_args': False,
          'name': '"void_method"',
          'ret_type': {'.class': 'AnyType'},
          'variables': []}}


mapped_void_no_args = {'.class': 'FuncDef',
 'arg_kinds': [],
 'arg_names': [],
 'flags': [],
 'fullname': 'test_def.void_no_args',
 'name': 'void_no_args',
 'type': None}

mapped_void_starargs = {'.class': 'FuncDef',
 'arg_kinds': [2],
 'arg_names': ['args'],
 'flags': [],
 'fullname': 'test_def.starargs',
 'name': 'starargs',
 'type': None}


mapped_void_starkwargs = {'.class': 'FuncDef',
 'arg_kinds': [4],
 'arg_names': ['kwargs'],
 'flags': [],
 'fullname': 'test_def.starkwargs',
 'name': 'starkwargs',
 'type': None}


mapped_max_np_array = {'.class': 'FuncDef',
 'arg_kinds': [0],
 'arg_names': ['arg1'],
 'flags': [],
 'fullname': 'test_def.max_np_array',
 'name': 'max_np_array',
 'type': {'.class': 'CallableType',
          'arg_kinds': [0],
          'arg_names': ['arg1'],
          'arg_types': [{'.class': 'TypeType',
                         'item': {'.class': 'Instance',
                                  'args': [{'.class': 'Instance',
                                            'boost_map': 'double',
                                            'type_ref': 'builtins.float'}],
                                  'boost_map': 'ndarray',
                                  'type_ref': 'numpy.ndarray'}}],
          'fallback': {'.class': 'Instance',
                       'boost_map': None,
                       'type_ref': 'builtins.function'},
          'implicit': False,
          'is_classmethod_class': False,
          'is_ellipsis_args': False,
          'name': '"max_np_array"',
          'ret_type': {'.class': 'Instance',
                       'boost_map': 'double',
                       'type_ref': 'builtins.float'},
          'variables': []}}



     