
"""
Each 9ML abstraction layer module will define its own ComponentClass class.

This module provides the base class for these.

:copyright: Copyright 2010-2013 by the Python lib9ML team, see AUTHORS.
:license: BSD-3, see LICENSE for details.
"""
from abc import ABCMeta
from .. import BaseALObject
from nineml.base import ContainerObject
from nineml.utils import (
    filter_discrete_types, ensure_valid_identifier,
    normalise_parameter_as_list)
from ..expressions import Alias, Constant
from nineml.base import DocumentLevelObject
from nineml.exceptions import name_error
from ..base import Parameter  # @IgnorePep8


class ComponentClass(BaseALObject, DocumentLevelObject, ContainerObject):
    """Base class for ComponentClasses in different 9ML modules."""

    __metaclass__ = ABCMeta  # Abstract base class

    defining_attributes = ('_name', '_parameters', '_aliases', '_constants')
    class_to_member = {'Parameter': 'parameter', 'Alias': 'alias',
                       'Constant': 'constant'}
    v1_nineml_type = 'ComponentClass'
    # New NineML types
    nineml_children = (Parameter, Alias, Constant)
    nineml_attr = ('name',)

    def __init__(self, name, parameters=None, aliases=None, constants=None):
        ensure_valid_identifier(name)
        self._name = name
        BaseALObject.__init__(self)
        DocumentLevelObject.__init__(self)
        ContainerObject.__init__(self)

        self._parameters = {}
        self._aliases = {}
        self._constants = {}

        # Turn any strings in the parameter list into Parameters:
        if parameters is None:
            parameters = []
        else:
            param_types = (basestring, Parameter)
            param_td = filter_discrete_types(parameters, param_types)
            params_from_strings = [Parameter(s) for s in param_td[basestring]]
            parameters = param_td[Parameter] + params_from_strings

        aliases = normalise_parameter_as_list(aliases)
        constants = normalise_parameter_as_list(constants)

        # Load the aliases as objects or strings:
        alias_td = filter_discrete_types(aliases, (basestring, Alias))
        aliases_from_strs = [Alias.from_str(o) for o in alias_td[basestring]]
        aliases = alias_td[Alias] + aliases_from_strs

        self.add(*parameters)
        self.add(*aliases)
        self.add(*constants)

    @property
    def name(self):
        """Returns the name of the component"""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def num_parameters(self):
        return len(self._parameters)

    @property
    def num_aliases(self):
        return len(self._aliases)

    @property
    def num_constants(self):
        return len(self._constants)

    @property
    def parameters(self):
        """Returns an iterator over the local |Parameter| objects"""
        return self._parameters.itervalues()

    @property
    def aliases(self):
        return self._aliases.itervalues()

    @property
    def constants(self):
        return self._constants.itervalues()

    @name_error
    def parameter(self, name):
        return self._parameters[name]

    @name_error
    def alias(self, name):
        return self._aliases[name]

    @name_error
    def constant(self, name):
        return self._constants[name]

    @property
    def parameter_names(self):
        return self._parameters.iterkeys()

    @property
    def alias_names(self):
        return self._aliases.iterkeys()

    @property
    def constant_names(self):
        return self._constants.iterkeys()

    @property
    def dimensions(self):
        return set(a.dimension for a in self.attributes_with_dimension)

    @property
    def attributes_with_dimension(self):
        return self.parameters

    @property
    def attributes_with_units(self):
        return self.constants

    def standardize_unit_dimensions(self, reference_set=None):
        """
        Replaces dimension objects with ones from a reference set so that their
        names do not conflict when writing to file
        """
        if reference_set is None:
            reference_set = self.dimensions
        for a in self.attributes_with_dimension:
            try:
                std_dim = next(d for d in reference_set if d == a.dimension)
            except StopIteration:
                continue
            a.set_dimension(std_dim)
