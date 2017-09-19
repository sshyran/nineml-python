from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
try:
    import pickle as pkl
except ImportError:
    from . import pickle as pkl  # @UnusedImport
from .dict import DictSerializer, DictUnserializer  # @IgnorePep8

DEFAULT_PROTOCOL = -1  # Highest one available


class PickleSerializer(DictSerializer):
    """
    A Serializer class that serializes to JSON
    """

    def to_file(self, serial_elem, file, **options):  # @UnusedVariable  @IgnorePep8 @ReservedAssignment
        pkl.dump(self.to_elem(serial_elem, **options), file,
                 options.get('protocol', DEFAULT_PROTOCOL))

    def to_str(self, serial_elem, **options):  # @UnusedVariable  @IgnorePep8
        return pkl.dumps(self.to_elem(serial_elem, **options),
                         options.get('protocol', DEFAULT_PROTOCOL))


class PickleUnserializer(DictUnserializer):
    """
    A Unserializer class that unserializes JSON
    """

    def from_file(self, file, **options):  # @ReservedAssignment @UnusedVariable @IgnorePep8
        return self.from_elem(pkl.load(file), **options)

    def from_str(self, string, **options):  # @UnusedVariable
        return self.from_elem(pkl.loads(string), **options)
