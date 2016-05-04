#!/usr/bin/env python
# encoding: utf-8

name = "acetylene"
shortDesc = u"fake reactions to cause photolysis"
longDesc = u"""
This library was created to force a fake photolysis reaction for acetylene.

Half life is set to 10 seconds
"""
entry(
    index = 1,
    label = "acetylene <=> hydrogen + acetyl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(.1, '1/s'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)
