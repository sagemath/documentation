Search.setIndex({"docnames": ["index", "sage/cpython/atexit", "sage/cpython/cython_metaclass", "sage/cpython/debug", "sage/cpython/dict_del_by_value", "sage/cpython/getattr", "sage/cpython/string", "sage/cpython/wrapperdescr"], "filenames": ["index.rst", "sage/cpython/atexit.rst", "sage/cpython/cython_metaclass.rst", "sage/cpython/debug.rst", "sage/cpython/dict_del_by_value.rst", "sage/cpython/getattr.rst", "sage/cpython/string.rst", "sage/cpython/wrapperdescr.rst"], "titles": ["Python technicalities", "Utilities for interfacing with the standard library\u2019s atexit module.", "Metaclasses for Cython extension types", "Various functions to debug Python internals", "Delete item from PyDict by exact value and hash", "Variants of getattr()", "String &lt;-&gt; bytes encoding/decoding", "Slot wrappers"], "terms": {"sagemath": [0, 1], "ha": [0, 2, 3, 5], "variou": 0, "modul": [0, 2], "provid": [0, 5], "access": [0, 5, 7], "low": 0, "level": 0, "intern": 0, "util": 0, "interfac": [0, 3], "standard": [0, 5], "librari": 0, "": [0, 4, 5, 6], "atexit": 0, "string": [0, 3, 5], "byte": 0, "encod": 0, "decod": 0, "function": [0, 1, 2, 4, 5, 7], "debug": 0, "variant": [0, 7], "getattr": [0, 3], "metaclass": 0, "cython": [0, 3, 5], "extens": [0, 5, 7], "type": [0, 3, 5, 7], "slot": [0, 3], "wrapper": [0, 3], "delet": 0, "item": 0, "from": [0, 1, 2, 3, 5, 6, 7], "pydict": 0, "exact": 0, "valu": [0, 3], "hash": 0, "index": 0, "search": 0, "page": 0, "class": [1, 2, 3, 5, 7], "sage": [1, 2, 3, 4, 5, 6, 7], "cpython": [1, 2, 3, 4, 5, 6, 7], "restore_atexit": 1, "base": [1, 2, 3, 5], "object": [1, 2, 3, 4, 5, 7], "context": 1, "manag": 1, "restor": 1, "state": 1, "its": 1, "previou": 1, "when": [1, 2, 5, 7], "exit": 1, "input": [1, 3, 4, 5, 6, 7], "run": 1, "bool": 1, "default": [1, 3], "fals": [1, 2, 5, 7], "true": [1, 5, 6], "befor": 1, "old": 1, "all": [1, 2, 3, 6], "which": [1, 2, 4, 5], "were": 1, "ad": [1, 3], "insid": 1, "clear": 1, "equal": 1, "alreadi": 1, "regist": 1, "handler": 1, "upon": 1, "enter": 1, "The": [1, 2, 3, 4, 5, 7], "combin": 1, "caus": 1, "twice": 1, "onc": 1, "again": 1, "python": [1, 2, 4, 5, 6, 7], "exampl": [1, 2, 3, 5, 6, 7], "For": [1, 5, 7], "thi": [1, 2, 3, 4, 5, 6, 7], "we": [1, 3, 5], "wrap": 1, "entir": 1, "so": [1, 2, 3, 5], "start": 1, "fresh": 1, "sake": 1, "note": [1, 2, 3, 7], "_run_exitfunc": 1, "list": [1, 3, 6], "can": [1, 2, 5, 7], "us": [1, 3, 4, 5, 6, 7], "test": [1, 3, 4, 5], "manipul": 1, "import": [1, 2, 3, 5, 6, 7], "def": [1, 2, 5, 7], "arg": [1, 2, 7], "kwarg": 1, "sy": 1, "see": [1, 5], "http": 1, "github": [1, 5], "com": 1, "issu": [1, 5], "25270": 1, "comment": 1, "56": 1, "stdout": 1, "write": 1, "str": [1, 3, 6], "n": [1, 5], "1": [1, 3, 5], "2": [1, 3, 5], "c": [1, 5, 7], "3": [1, 3, 5, 6], "0x": [1, 3], "4": [1, 3, 5], "5": [1, 3, 7], "d": [1, 4, 5], "6": [1, 5, 7], "should": [1, 2, 5, 7], "none": [1, 2, 3, 6], "just": 1, "option": 1, "i": [1, 2, 3, 4, 5, 6, 7], "_": [1, 2, 3], "7": [1, 7], "8": 1, "e": [1, 5], "9": [1, 7], "origin": 1, "ar": [1, 2, 4, 5, 7], "pass": [1, 2, 5, 7], "still": 1, "place": 1, "doe": [2, 3, 4, 5], "support": [2, 5], "mani": 2, "caveat": [2, 5], "you": [2, 7], "easili": [2, 5, 7], "get": [2, 5], "segfault": 2, "make": [2, 4], "mistak": 2, "It": [2, 6], "reli": [2, 4], "undocu": 2, "behaviour": 2, "thing": 2, "might": 2, "break": 2, "futur": 2, "version": 2, "To": 2, "enabl": 2, "mechan": 2, "need": [2, 3, 5, 7], "put": 2, "cimport": 2, "cython_metaclass": 2, "your": 2, "pxd": 2, "file": 2, "one": [2, 5], "In": [2, 5], "k": 2, "cdef": [2, 3, 4, 5], "want": [2, 5], "defin": [2, 5], "method": [2, 3, 5, 7], "__getmetaclass__": 2, "singl": 2, "unus": 2, "argument": [2, 7], "turn": 2, "off": 2, "direct": 2, "always_allow_keyword": 2, "return": [2, 3, 4, 5, 7], "mycustomtyp": 2, "foo": [2, 3], "mymetaclass": 2, "must": 2, "an": [2, 4, 5, 7], "ordinari": [2, 3], "take": 2, "cl": [2, 3, 5], "being": [2, 5], "construct": 2, "meta": 2, "__init__": [2, 3, 7], "call": [2, 3, 5, 6, 7], "would": 2, "name": [2, 3, 5], "dict": [2, 3, 4, 5, 7], "while": 2, "creat": [2, 5], "dure": 2, "therefor": 2, "refer": 2, "ani": [2, 5, 7], "global": 2, "includ": 2, "other": [2, 3, 5, 7], "unless": 2, "veri": 2, "care": 2, "non": 2, "those": 2, "safe": 2, "same": [2, 5], "warn": 2, "appli": [2, 5], "__new__": [2, 3], "__cinit__": 2, "never": 2, "re": [2, 3], "particular": 2, "cannot": [2, 4], "have": [2, 3, 5, 7], "attribut": [2, 3, 5], "virtual": 2, "misc": [2, 5], "print": [2, 3, 5], "format": 2, "myderivedtyp": 2, "__class__": [2, 3, 5], "mypythontyp": 2, "pytypereadi": 2, "t": [2, 5, 7], "sage_pytype_readi": 2, "first": [2, 7], "pytype_readi": 2, "handl": [2, 5], "stuff": 2, "getattr_debug": 3, "obj": [3, 5], "_no_default": 3, "A": [3, 5, 7], "implement": [3, 4, 5, 7], "lot": 3, "info": 3, "correctli": 3, "__getattr__": [3, 5], "On": 3, "hand": 3, "assum": 3, "gener": [3, 5], "overridden": 3, "__getattribute__": [3, 5], "detect": 3, "case": 3, "whose": [3, 4, 5], "request": 3, "wa": [3, 5], "found": [3, 4, 6], "revers": 3, "broken": 3, "12": 3, "__dict__": [3, 5], "did": 3, "find": [3, 4], "mro": [3, 5], "method_descriptor": 3, "got": 3, "descriptor": [3, 5], "__get__": [3, 5], "built": 3, "builtin_function_or_method": 3, "__doc__": 3, "gp": 3, "log": 3, "lib": [3, 5], "pari": 3, "gpelement": 3, "expect": [3, 6], "functionel": 3, "ipywidget": 3, "intslid": 3, "0": [3, 7], "widget": 3, "widget_int": 3, "_int": 3, "traitlet": 3, "cint": 3, "data": 3, "__set__": 3, "ignor": [3, 5], "becaus": [3, 5], "int": [3, 5, 7], "traceback": [3, 5, 6], "most": [3, 5, 6], "recent": [3, 5, 6], "last": [3, 5, 6], "attributeerror": [3, 5], "ring": [3, 5], "integ": [3, 5, 7], "xyz": 3, "shortrepr": 3, "max": 3, "50": 3, "repr": [3, 5], "bound": [3, 5, 7], "charact": 3, "If": [3, 4, 5], "too": 3, "long": 3, "truncat": 3, "end": 3, "hello": [3, 5], "world": [3, 5], "worl": 3, "type_debug": 3, "random": 3, "0x7fc57da7f040": 3, "ob_refcnt": 3, "9739": 3, "ob_typ": 3, "tp_name": 3, "tp_basics": 3, "16": 3, "tp_items": 3, "tp_dictoffset": 3, "tp_weaklistoffset": 3, "tp_base": 3, "__base__": 3, "null": 3, "__bases__": 3, "tupl": 3, "tp_mro": 3, "__mro__": 3, "tp_dict": 3, "__setattr__": 3, "__reduce_ex__": 3, "__reduce__": 3, "__str__": 3, "__format__": 3, "__delattr__": 3, "__subclasshook__": 3, "__repr__": 3, "__hash__": 3, "__sizeof__": 3, "tp_alloc": 3, "pytype_genericalloc": 3, "tp_new": 3, "0x7fc57d7594f0": 3, "tp_init": 3, "0x7fc57d758ee0": 3, "tp_dealloc": 3, "__dealloc__": 3, "0x7fc57d757010": 3, "tp_free": 3, "pyobject_del": 3, "tp_repr": 3, "0x7fc57d75b990": 3, "tp_print": 3, "tp_hash": 3, "_py_hashpoint": 3, "tp_call": 3, "__call__": [3, 5, 7], "tp_str": 3, "0x7fc57d757020": 3, "tp_compar": 3, "__cmp__": 3, "tp_richcompar": 3, "__richcmp__": 3, "tp_getattr": 3, "tp_setattr": 3, "__setattribute__": 3, "tp_getattro": 3, "pyobject_genericgetattr": 3, "tp_setattro": 3, "pyobject_genericsetattr": 3, "tp_iter": 3, "__iter__": 3, "tp_iternext": 3, "__next__": 3, "tp_descr_get": 3, "tp_descr_set": 3, "tp_cach": 3, "tp_weaklist": 3, "tp_travers": 3, "tp_clear": 3, "tp_is_gc": 3, "tp_as_numb": 3, "tp_as_sequ": 3, "tp_as_map": 3, "tp_as_buff": 3, "tp_flag": 3, "have_getcharbuff": 3, "have_sequence_in": 3, "have_inplaceop": 3, "have_richcompar": 3, "have_weakref": 3, "have_it": 3, "have_class": 3, "basetyp": 3, "readi": 3, "have_index": 3, "have_version_tag": 3, "valid_version_tag": 3, "tp_version_tag": 3, "typeerror": [3, 5, 6], "bewar": 4, "routin": 4, "here": 4, "detail": 4, "go": 4, "beyond": 4, "publish": 4, "api": 4, "author": [4, 5], "nil": 4, "bruin": 4, "2017": 4, "05": [4, 5], "dict_del_by_valu": 4, "test_del_dictitem_by_exact_valu": 4, "h": 4, "help": 4, "some": [4, 5], "dictionari": 4, "kei": 4, "under": [4, 5], "underli": 4, "bucket": 4, "determin": 4, "ident": 4, "Of": 4, "cours": 4, "onli": [4, 5], "sens": 4, "pair": 4, "correspond": 4, "wise": 4, "distinct": 4, "match": 4, "noth": 4, "silent": 4, "attributeerrormessag": 5, "tri": 5, "emul": 5, "messag": 5, "typic": 5, "fate": 5, "error": [5, 6], "caught": 5, "henc": 5, "normal": [5, 7], "circumst": 5, "nobodi": 5, "ever": 5, "idea": 5, "fast": 5, "represent": 5, "That": 5, "someon": 5, "bla": 5, "indirect": 5, "doctest": 5, "x": [5, 7], "polygen": 5, "zz": 5, "qq": 5, "gen": 5, "flint": 5, "polynomi": 5, "polynomial_rational_flint": 5, "simon": 5, "king": 5, "2011": 5, "21": 5, "dir_with_other_class": 5, "self": [5, 7], "dir": 5, "also": 5, "instanc": 5, "right": 5, "after": 5, "caller_class": 5, "resolut": 5, "order": 5, "b": [5, 6, 7], "f": 5, "check": [5, 7], "without": [5, 7], "well": 5, "public": 5, "hasattr": 5, "getattr_from_other_class": 5, "new": 5, "style": 5, "rais": 5, "avoid": 5, "doubl": 5, "lookup": 5, "intend": 5, "inc": 5, "staticmethod": 5, "greet": 5, "lazy_attribut": 5, "static": 5, "work": 5, "lazi": 5, "thei": 5, "allow": 5, "assign": 5, "_cached_method": 5, "condit": 5, "satisfi": 5, "g": 5, "deriv": 5, "parent": 5, "polynomialr": 5, "spars": 5, "17": 5, "yet": 5, "often": 5, "do": 5, "accept": 5, "cheat": 5, "__weakref__": 5, "doesn": 5, "occur": 5, "8296": 5, "coupl": 5, "more": 5, "ip": 5, "get_ipython": 5, "interact": 5, "shell": 5, "magic_psearch": 5, "yield": 5, "workaround": 5, "guarante": 5, "robust": 5, "raw_getattr": 5, "like": [5, 7], "invok": 5, "bind": 5, "behavior": 5, "unbound": [5, 7], "hook": 5, "actual": 5, "mean": 5, "properti": 5, "prop": 5, "42": 5, "magic": 5, "attr": 5, "ye": 5, "ok": 5, "inherit": 5, "y": 5, "bytes_to_str": 6, "convert": 6, "given": 6, "unicod": 6, "specifi": 6, "op": 6, "xcf": 6, "x80": 6, "u": 6, "\u03c0": 6, "str_to_byt": 6, "instal": 7, "special": 7, "__lt__": 7, "alwai": 7, "__add__": 7, "pure": 7, "notimpl": 7, "wrapperdescr": 7, "wrapperdescr_cal": 7, "slotwrapp": 7, "kwd": 7, "main": 7, "reason": 7, "arithmet": 7, "__mul__": 7, "worri": 7, "about": 7, "whether": 7, "__rmul__": 7, "posit": 7, "correct": 7, "howev": 7, "skip": 7, "arbitrari": 7, "further": 7, "sinc": 7, "crash": 7, "incorrectli": 7, "54": 7, "63": 7, "structur": 7, "element": 7, "numer": 7, "mip": 7, "mixedintegerlinearprogram": 7, "maxim": 7, "mix": 7, "program": 7, "variabl": 7, "constraint": 7}, "objects": {"sage.cpython": [[1, 0, 0, "-", "atexit"], [2, 0, 0, "-", "cython_metaclass"], [3, 0, 0, "-", "debug"], [4, 0, 0, "-", "dict_del_by_value"], [5, 0, 0, "-", "getattr"], [6, 0, 0, "-", "string"], [7, 0, 0, "-", "wrapperdescr"]], "sage.cpython.atexit": [[1, 1, 1, "", "restore_atexit"]], "sage.cpython.debug": [[3, 2, 1, "", "getattr_debug"], [3, 2, 1, "", "shortrepr"], [3, 2, 1, "", "type_debug"]], "sage.cpython.dict_del_by_value": [[4, 2, 1, "", "test_del_dictitem_by_exact_value"]], "sage.cpython.getattr": [[5, 1, 1, "", "AttributeErrorMessage"], [5, 2, 1, "", "dir_with_other_class"], [5, 2, 1, "", "getattr_from_other_class"], [5, 2, 1, "", "raw_getattr"]], "sage.cpython.getattr.AttributeErrorMessage": [[5, 3, 1, "", "cls"], [5, 3, 1, "", "name"]], "sage.cpython.string": [[6, 2, 1, "", "bytes_to_str"], [6, 2, 1, "", "str_to_bytes"]], "sage.cpython.wrapperdescr": [[7, 2, 1, "", "wrapperdescr_call"]]}, "objtypes": {"0": "py:module", "1": "py:class", "2": "py:function", "3": "py:attribute"}, "objnames": {"0": ["py", "module", "Python module"], "1": ["py", "class", "Python class"], "2": ["py", "function", "Python function"], "3": ["py", "attribute", "Python attribute"]}, "titleterms": {"python": [0, 3], "technic": 0, "indic": 0, "tabl": 0, "util": 1, "interfac": 1, "standard": 1, "librari": 1, "": 1, "atexit": 1, "modul": 1, "metaclass": 2, "cython": 2, "extens": 2, "type": 2, "how": 2, "us": 2, "implement": 2, "variou": 3, "function": 3, "debug": 3, "intern": 3, "delet": 4, "item": 4, "from": 4, "pydict": 4, "exact": 4, "valu": 4, "hash": 4, "variant": 5, "getattr": 5, "string": 6, "byte": 6, "encod": 6, "decod": 6, "slot": 7, "wrapper": 7}, "envversion": {"sphinx.domains.c": 3, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 9, "sphinx.domains.index": 1, "sphinx.domains.javascript": 3, "sphinx.domains.math": 2, "sphinx.domains.python": 4, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx.ext.todo": 2, "sphinx": 60}, "alltitles": {"Python technicalities": [[0, "python-technicalities"]], "Indices and Tables": [[0, "indices-and-tables"]], "Utilities for interfacing with the standard library\u2019s atexit module.": [[1, "utilities-for-interfacing-with-the-standard-library-s-atexit-module"]], "Metaclasses for Cython extension types": [[2, "metaclasses-for-cython-extension-types"]], "How to use": [[2, "how-to-use"]], "Implementation": [[2, "implementation"]], "Various functions to debug Python internals": [[3, "various-functions-to-debug-python-internals"]], "Delete item from PyDict by exact value and hash": [[4, "delete-item-from-pydict-by-exact-value-and-hash"]], "Variants of getattr()": [[5, "variants-of-getattr"]], "String <-> bytes encoding/decoding": [[6, "string-bytes-encoding-decoding"]], "Slot wrappers": [[7, "slot-wrappers"]]}, "indexentries": {"module": [[1, "module-sage.cpython.atexit"], [2, "module-sage.cpython.cython_metaclass"], [3, "module-sage.cpython.debug"], [4, "module-sage.cpython.dict_del_by_value"], [5, "module-sage.cpython.getattr"], [6, "module-sage.cpython.string"], [7, "module-sage.cpython.wrapperdescr"]], "restore_atexit (class in sage.cpython.atexit)": [[1, "sage.cpython.atexit.restore_atexit"]], "sage.cpython.atexit": [[1, "module-sage.cpython.atexit"]], "sage.cpython.cython_metaclass": [[2, "module-sage.cpython.cython_metaclass"]], "getattr_debug() (in module sage.cpython.debug)": [[3, "sage.cpython.debug.getattr_debug"]], "sage.cpython.debug": [[3, "module-sage.cpython.debug"]], "shortrepr() (in module sage.cpython.debug)": [[3, "sage.cpython.debug.shortrepr"]], "type_debug() (in module sage.cpython.debug)": [[3, "sage.cpython.debug.type_debug"]], "sage.cpython.dict_del_by_value": [[4, "module-sage.cpython.dict_del_by_value"]], "test_del_dictitem_by_exact_value() (in module sage.cpython.dict_del_by_value)": [[4, "sage.cpython.dict_del_by_value.test_del_dictitem_by_exact_value"]], "attributeerrormessage (class in sage.cpython.getattr)": [[5, "sage.cpython.getattr.AttributeErrorMessage"]], "cls (sage.cpython.getattr.attributeerrormessage attribute)": [[5, "sage.cpython.getattr.AttributeErrorMessage.cls"]], "dir_with_other_class() (in module sage.cpython.getattr)": [[5, "sage.cpython.getattr.dir_with_other_class"]], "getattr_from_other_class() (in module sage.cpython.getattr)": [[5, "sage.cpython.getattr.getattr_from_other_class"]], "name (sage.cpython.getattr.attributeerrormessage attribute)": [[5, "sage.cpython.getattr.AttributeErrorMessage.name"]], "raw_getattr() (in module sage.cpython.getattr)": [[5, "sage.cpython.getattr.raw_getattr"]], "sage.cpython.getattr": [[5, "module-sage.cpython.getattr"]], "bytes_to_str() (in module sage.cpython.string)": [[6, "sage.cpython.string.bytes_to_str"]], "sage.cpython.string": [[6, "module-sage.cpython.string"]], "str_to_bytes() (in module sage.cpython.string)": [[6, "sage.cpython.string.str_to_bytes"]], "sage.cpython.wrapperdescr": [[7, "module-sage.cpython.wrapperdescr"]], "wrapperdescr_call() (in module sage.cpython.wrapperdescr)": [[7, "sage.cpython.wrapperdescr.wrapperdescr_call"]]}})