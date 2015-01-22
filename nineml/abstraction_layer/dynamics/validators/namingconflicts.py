"""
docstring needed

:copyright: Copyright 2010-2013 by the Python lib9ML team, see AUTHORS.
:license: BSD-3, see LICENSE for details.
"""
from nineml.utility import assert_no_duplicates
from nineml.exceptions import NineMLRuntimeError
from ...componentclass.validators import (
    LocalNameConflictsComponentValidator,
    DimensionNameConflictsComponentValidator)
from . import PerNamespaceDynamicsValidator


# Check that the sub-components stored are all of the
# right types:
class LocalNameConflictsDynamicsValidator(
        LocalNameConflictsComponentValidator):

    """
    Check for conflicts between Aliases, StateVariables, Parameters, and
    EventPorts, and analog input ports

    We do not need to check for comflicts with output AnalogPorts, since, these
    will use names.
    """

    def action_statevariable(self, state_variable, namespace, **kwargs):  # @UnusedVariable @IgnorePep8
        self.check_conflicting_symbol(namespace=namespace,
                                      symbol=state_variable.name)

    def action_analogreceiveport(self, port, namespace, **kwargs):  # @UnusedVariable @IgnorePep8
        self.check_conflicting_symbol(namespace=namespace, symbol=port.name)

    def action_analogreduceport(self, port, namespace, **kwargs):  # @UnusedVariable @IgnorePep8
        self.check_conflicting_symbol(namespace=namespace, symbol=port.name)

    def action_eventreceiveport(self, port, namespace, **kwargs):  # @UnusedVariable @IgnorePep8
        self.check_conflicting_symbol(namespace=namespace, symbol=port.name)


class DimensionNameConflictsDynamicsValidator(
        DimensionNameConflictsComponentValidator):

    def __init__(self, componentclass):
        super(DimensionNameConflictsDynamicsValidator, self).__init__(
            componentclass)
        self.dimensions = {}
        self.visit(componentclass)

    def check_conflicting_dimension(self, dimension):
        try:
            if dimension != self.dimensions[dimension.name]:
                err = ("Duplication of dimension name '{}' for differing "
                       "dimensions ('{}', '{}')"
                       .format(dimension.name, dimension,
                               self.dimensions[dimension.name]))
                raise NineMLRuntimeError(err)
        except KeyError:
            self.dimensions[dimension.name] = dimension

    def action_statevariable(self, state_variable, **kwargs):  # @UnusedVariable @IgnorePep8
        self.check_conflicting_dimension(state_variable.dimension)

    def action_analogreceiveport(self, port, **kwargs):  # @UnusedVariable @IgnorePep8
        self.check_conflicting_dimension(port.dimension)

    def action_analogreduceport(self, port, **kwargs):  # @UnusedVariable @IgnorePep8
        self.check_conflicting_dimension(port.dimension)

    def action_analogsendport(self, port, **kwargs):  # @UnusedVariable @IgnorePep8
        self.check_conflicting_dimension(port.dimension)


class DuplicateRegimeNamesDynamicsValidator(PerNamespaceDynamicsValidator):

    def __init__(self, componentclass):
        super(DuplicateRegimeNamesDynamicsValidator, self).__init__(
            require_explicit_overrides=False)
        self.visit(componentclass)

    def action_componentclass(self, componentclass, namespace):  # @UnusedVariable @IgnorePep8
        regime_names = [r.name for r in componentclass.regimes]
        assert_no_duplicates(regime_names)
