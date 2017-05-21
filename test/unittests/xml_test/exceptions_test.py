import unittest
from nineml.serialization.xml import Unserializer as Uxml
from nineml.exceptions import (
    NineMLMissingSerializationError, NineMLSerializationError)


class TestPopulation(unittest.TestCase):

    def setUp(self):
        self.unserializer = Uxml(root=bad_xml)

#     def test_bad_block(self):
#         self.assertRaises(NineMLSerializationError,
#                           self.unserializer.unserialize,
#                           'BadBlock')
# 
#     def test_bad_attribute(self):
#         self.assertRaises(NineMLMissingSerializationError,
#                           self.doc.__getitem__,
#                           'BadAttribute1')
#         self.assertRaises(NineMLMissingSerializationError,
#                           self.doc.__getitem__,
#                           'BadAttribute2')
# 
#     def test_missing_attribute(self):
#         self.assertRaises(NineMLMissingSerializationError,
#                           self.doc.__getitem__,
#                           'MissingAttribute')

    def test_missing_block(self):
        self.assertRaises(NineMLMissingSerializationError,
                          self.unserializer.unserialize)

bad_xml = """<?xml version="1.0" encoding="UTF-8"?>
<NineML xmlns="http://nineml.net/9ML/2.0">
  <Population name="BadBlock">
    <Size>10</Size>
    <Cell>
      <Reference name="SimpleProperties"/>
    </Cell>
    <BadBlock/>
  </Population>
  <Population name="BadAttribute1" bad_attribute="test">
    <Size>10</Size>
    <Cell>
      <Reference name="SimpleProperties"/>
    </Cell>
  </Population>
  <Population name="BadAttribute2">
    <Size>10</Size>
    <Cell bad_attribute="test">
      <Reference name="SimpleProperties"/>
    </Cell>
  </Population>
  <Population name="MissingAttribute">
    <Size>10</Size>
    <Cell>
      <Reference/>
    </Cell>
  </Population>
  <Population name="MissingBlock1">
    <Size>10</Size>
  </Population>
  <Population name="MissingBlock2">
    <Cell>
      <Reference name="SimpleProperties"/>
    </Cell>
  </Population>
  <Dynamics name="Simple">
    <Parameter name="rate" dimension="time"/>
    <StateVariable name="x" dimension="dimensionless"/>
    <Regime name="sole">
      <TimeDerivative variable="x">
        <MathInline>x/rate</MathInline>
      </TimeDerivative>
    </Regime>
  </Dynamics>
  <DynamicsProperties name="SimpleProperties">
    <Definition name="Simple"/>
    <Property name="rate">
      <Quantity units="ms">
        <SingleValue>1.0</SingleValue>
      </Quantity>
    </Property>
  </DynamicsProperties>
  <Dimension name="time" t="1"/>
  <Dimension name="dimensionless"/>
  <Unit symbol="ms" dimension="time" power="-3"/>
</NineML>
"""
