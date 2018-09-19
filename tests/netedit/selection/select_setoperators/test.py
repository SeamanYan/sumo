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
import time

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# first rebuild network
netedit.rebuildNetwork()

# go to select mode
netedit.selectMode()

# first check that invert works
netedit.selectionInvert()

# invert again and delete selected items (all must be unselected)
netedit.selectionInvert()
netedit.deleteSelectedItems()

# invert again and clear selection
netedit.selectionInvert()
netedit.selectionClear()

# use a rectangle to select central elements
netedit.selectionRectangle(referencePosition, 250, 150, 400, 300)

# invert selection to select only extern nodes and delete it
netedit.selectionInvert()
netedit.deleteSelectedItems()

# extra wait for debug
time.sleep(5)

# check undo and redo
netedit.undo(referencePosition, 1)

# extra wait for debug
time.sleep(5)

netedit.redo(referencePosition, 1)

# extra wait for debug
time.sleep(5)

netedit.redo(referencePosition, 1)

# extra wait for debug
time.sleep(5)

# save additionals
netedit.saveAdditionals()

# save shapes
netedit.saveShapes()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
