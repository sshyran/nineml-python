"""
docstring needed

:copyright: Copyright 2010-2013 by the Python lib9ML team, see AUTHORS.
:license: BSD-3, see LICENSE for details.
"""
from ...componentclass.visitors.cloner import ComponentCloner


class ConnectionRuleCloner(ComponentCloner):

    def visit_componentclass(self, component_class, **kwargs):
        super(ConnectionRuleCloner, self).visit_componentclass(component_class)
        ccn = component_class.__class__(
            name=component_class.name,
            parameters=[p.accept_visitor(self, **kwargs)
                        for p in component_class.parameters],
            standard_libary=component_class.standard_library)
        return ccn
