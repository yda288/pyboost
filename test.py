from serialised import *
from rawserialised import *
import serialisedparser
import rawserialisedparser

class TestParser:
    def test_mapped_inproduct(self):
        assert(serialisedparser.parse(mapped_inproduct) == (["vector['Foo']"], ["tuple['double', 'double']", 'string']))

    def test_mapped_builtins_only(self):
        assert(serialisedparser.parse(mapped_builtins_only) == (['complex'], ['double', 'int']))

    def test_mapped_max_np_array(self):
        assert(serialisedparser.parse(mapped_max_np_array) == (['double'], ["ndarray['double']"]))

    ##voids
    def test_mapped_void_method(self):
        assert(serialisedparser.parse(mapped_void_method) == (['None'], ['string']))

    def test_mapped_void_no_args(self):
        assert(serialisedparser.parse(mapped_void_no_args) == (['None'], ['None']))

    def test_mapped_void_starargs(self):
        assert(serialisedparser.parse(mapped_void_starargs) == (['None'], ['None']))

    def test_mapped_void_starkwargs(self):
        assert(serialisedparser.parse(mapped_void_starkwargs) == (['None'], ['None']))

class TestRawParser:
    def test_inproduct(self):
        assert(rawserialisedparser.parse(inproduct) == (["vector['foo.Foo']"], ["vector['tuple['double', 'double']", 'string']))

    def test_builtins_only(self):
        assert(rawserialisedparser.parse(builtins_only) == (['complex'], ['double', 'int']))

    def test_max_np_array(self):
        assert(rawserialisedparser.parse(max_np_array) == (['double'], ["numpy.ndarray['double']"]))

    ##voids
    def test_void_method(self):
        assert(rawserialisedparser.parse(void_method) == (['None'], ['string']))

    def test_void_no_args(self):
        assert(rawserialisedparser.parse(void_no_args) == (['None'], ['None']))

    def test_void_starargs(self):
        assert(rawserialisedparser.parse(void_starargs) == (['None'], ['None']))

    def test_void_starkwargs(self):
        assert(rawserialisedparser.parse(void_starkwargs) == (['None'], ['None']))
