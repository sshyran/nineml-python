import unittest
from nineml.values import (ArrayValue, RandomValue)
from nineml.utils.testing.comprehensive import instances_of_all_types
from nineml.exceptions import (NineMLValueError, NineMLRuntimeError)


class TestArrayValueExceptions(unittest.TestCase):

    def test___init___ninemlvalueerror(self):
        """
        line #: 216
        message: Values provided to ArrayValue ({}) could not be converted to a list of floats

        context:
        --------
    def __init__(self, values, datafile=None):
        super(ArrayValue, self).__init__()
        try:
            self._values = values.astype(float)  # If NumPy array
        except AttributeError:
            try:
                self._values = [float(v) for v in values]
            except (TypeError, ValueError):
        """

        arrayvalue = next(instances_of_all_types['ArrayValue'].itervalues())
        self.assertRaises(
            NineMLValueError,
            arrayvalue.__init__,
            values=None,
            datafile=None)

    def test_inverse_arrayvalue(self):
        """
        line #: 263
        message: GeneratorExp(elt=BinOp(left=Num(n=1.0), op=Div(), right=Name(id='v', ctx=Load())), generators=[comprehension(target=Name(id='v', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='_values', ctx=Load()), ifs=[])])

        context:
        --------
    def inverse(self):
        try:
            return ArrayValue(1.0 / self._values)
        except AttributeError:
        """

        arrayvalue = next(instances_of_all_types['ArrayValue'].itervalues())
        self.assertRaises(
            ArrayValue,
            arrayvalue.inverse)

    def test_to_xml_notimplementederror(self):
        """
        line #: 272
        message: TODO: Need to implement code to save data to external file

        context:
        --------
    def to_xml(self, document, E=E, **kwargs):  # @UnusedVariable
        if self._datafile is None:
            return E.ArrayValue(
                *[E.ArrayValueRow(index=str(i), value=repr(v))
                  for i, v in enumerate(self._values)])
        else:
        """

        arrayvalue = next(instances_of_all_types['ArrayValue'].itervalues())
        self.assertRaises(
            NotImplementedError,
            arrayvalue.to_xml,
            document=None,
            E=E)

    def test_from_xml_ninemlruntimeerror(self):
        """
        line #: 300
        message: Negative indices found in array rows

        context:
        --------
    def from_xml(cls, element, document, **kwargs):  # @UnusedVariable
        if element.tag == 'ExternalArrayValue':
            url = get_xml_attr(element, 'url', document, **kwargs)
            with contextlib.closing(urlopen(url)) as f:
                # FIXME: Should use a non-numpy version of this load function
                values = numpy.loadtxt(f)
            return cls(values, (get_xml_attr(element, 'url', document,
                                             **kwargs),
                                get_xml_attr(element, 'mimetype', document,
                                             **kwargs),
                                get_xml_attr(element, 'columnName', document,
                                             **kwargs)))
        else:
            rows = [(get_xml_attr(e, 'index', document, dtype=int, **kwargs),
                     get_xml_attr(e, 'value', document, dtype=float, **kwargs))
                    for e in get_subblocks(element, 'ArrayValueRow', **kwargs)]
            sorted_rows = sorted(rows, key=itemgetter(0))
            indices, values = zip(*sorted_rows)
            if indices[0] < 0:
        """

        self.assertRaises(
            NineMLRuntimeError,
            ArrayValue.from_xml,
            element=None,
            document=None)

    def test_from_xml_ninemlruntimeerror2(self):
        """
        line #: 304
        message: Duplicate indices ({}) found in array rows

        context:
        --------
    def from_xml(cls, element, document, **kwargs):  # @UnusedVariable
        if element.tag == 'ExternalArrayValue':
            url = get_xml_attr(element, 'url', document, **kwargs)
            with contextlib.closing(urlopen(url)) as f:
                # FIXME: Should use a non-numpy version of this load function
                values = numpy.loadtxt(f)
            return cls(values, (get_xml_attr(element, 'url', document,
                                             **kwargs),
                                get_xml_attr(element, 'mimetype', document,
                                             **kwargs),
                                get_xml_attr(element, 'columnName', document,
                                             **kwargs)))
        else:
            rows = [(get_xml_attr(e, 'index', document, dtype=int, **kwargs),
                     get_xml_attr(e, 'value', document, dtype=float, **kwargs))
                    for e in get_subblocks(element, 'ArrayValueRow', **kwargs)]
            sorted_rows = sorted(rows, key=itemgetter(0))
            indices, values = zip(*sorted_rows)
            if indices[0] < 0:
                raise NineMLRuntimeError(
                    "Negative indices found in array rows")
            if len(list(itertools.groupby(indices))) != len(indices):
                groups = [list(g) for g in itertools.groupby(indices)]
        """

        self.assertRaises(
            NineMLRuntimeError,
            ArrayValue.from_xml,
            element=None,
            document=None)

    def test_from_xml_ninemlruntimeerror3(self):
        """
        line #: 308
        message: Indices greater or equal to the number of array rows

        context:
        --------
    def from_xml(cls, element, document, **kwargs):  # @UnusedVariable
        if element.tag == 'ExternalArrayValue':
            url = get_xml_attr(element, 'url', document, **kwargs)
            with contextlib.closing(urlopen(url)) as f:
                # FIXME: Should use a non-numpy version of this load function
                values = numpy.loadtxt(f)
            return cls(values, (get_xml_attr(element, 'url', document,
                                             **kwargs),
                                get_xml_attr(element, 'mimetype', document,
                                             **kwargs),
                                get_xml_attr(element, 'columnName', document,
                                             **kwargs)))
        else:
            rows = [(get_xml_attr(e, 'index', document, dtype=int, **kwargs),
                     get_xml_attr(e, 'value', document, dtype=float, **kwargs))
                    for e in get_subblocks(element, 'ArrayValueRow', **kwargs)]
            sorted_rows = sorted(rows, key=itemgetter(0))
            indices, values = zip(*sorted_rows)
            if indices[0] < 0:
                raise NineMLRuntimeError(
                    "Negative indices found in array rows")
            if len(list(itertools.groupby(indices))) != len(indices):
                groups = [list(g) for g in itertools.groupby(indices)]
                raise NineMLRuntimeError(
                    "Duplicate indices ({}) found in array rows".format(
                        ', '.join(str(g[0]) for g in groups if len(g) > 1)))
            if indices[-1] >= len(indices):
        """

        self.assertRaises(
            NineMLRuntimeError,
            ArrayValue.from_xml,
            element=None,
            document=None)

    def test___float___typeerror(self):
        """
        line #: 321
        message: ArrayValues cannot be converted to a single float

        context:
        --------
    def __float__(self):
        """

        arrayvalue = next(instances_of_all_types['ArrayValue'].itervalues())
        self.assertRaises(
            TypeError,
            arrayvalue.__float__)

    def test__check_single_value_ninemlruntimeerror(self):
        """
        line #: 441
        message: Cannot use {} in array arithmetic operation, only values that can be converted to a single float are allowed

        context:
        --------
    def _check_single_value(self, num):
        try:
            float(num)
        except TypeError:
        """

        arrayvalue = next(instances_of_all_types['ArrayValue'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            arrayvalue._check_single_value,
            num=None)


class TestRandomValueExceptions(unittest.TestCase):

    def test___float___typeerror(self):
        """
        line #: 457
        message: RandomValues cannot be converted to a single float

        context:
        --------
    def __float__(self):
        """

        randomvalue = next(instances_of_all_types['RandomValue'].itervalues())
        self.assertRaises(
            TypeError,
            randomvalue.__float__)

    def test___iter___ninemlruntimeerror(self):
        """
        line #: 481
        message: Generator not set for RandomValue '{}'

        context:
        --------
    def __iter__(self):
        if self._generator is None:
        """

        randomvalue = next(instances_of_all_types['RandomValue'].itervalues())
        self.assertRaises(
            NineMLRuntimeError,
            randomvalue.__iter__)

    def test_inverse_notimplementederror(self):
        """
        line #: 503
        message: 

        context:
        --------
    def inverse(self):
        """

        randomvalue = next(instances_of_all_types['RandomValue'].itervalues())
        self.assertRaises(
            NotImplementedError,
            randomvalue.inverse)
