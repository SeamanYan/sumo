#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# apply zoom
netedit.setZoom("25", "0", "25")

# go to additional mode
netedit.additionalMode()

# select BusStop
netedit.changeAdditional("busStop")

# create BusStop with default parameters
netedit.leftClick(referencePosition, 275, 250)

# select Access detector
netedit.changeAdditional("access")

# Create Access detector
netedit.selectAdditionalChild(7, 0)
netedit.leftClick(referencePosition, 50, 200)

# go to inspect mode
netedit.inspectMode()

# inspect Access
netedit.leftClick(referencePosition, 46, 181)

# Change block movement
netedit.modifyBoolAttribute(7)

# go to move mode
netedit.moveMode()

# try to move Acces
netedit.moveElement(referencePosition, -147, 163, 100, 163)

# go to inspect mode
netedit.inspectMode()

# inspect Access
netedit.leftClick(referencePosition, 46, 181)

# Change block movement
netedit.modifyBoolAttribute(7)

# go to move mode
netedit.moveMode()

# move Acces
netedit.moveElement(referencePosition, -147, 163, 100, 163)

# Check undo redo
netedit.undo(referencePosition, 5)
netedit.redo(referencePosition, 5)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
