# -*- encoding: utf-8 -*-
#   Copyright 2008 Agile42 GmbH, Berlin (Germany)
#   Copyright 2011 Agilo Software GmbH All rights reserved
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#   Authors: 
#       - Roberto Bettazzoni <roberto.bettazzoni__at__agile42.com>

import os, sys

dirInSysPath = lambda d : [p for p in sys.path if os.path.normcase(p) == d]

def removeSysPath(path):
    pf = dirInSysPath(path)
    if pf:
        sys.path.remove(pf[0])

def setPathAsFirstSysPath(path):
    removeSysPath(path)
    sys.path.insert(0, path)

def setSysPathAsFirstOnlyIfNotPresent(path):
    pf = dirInSysPath(path)
    if pf:
        sys.path.insert(0, path)
    return pf != []


#def setPathAsLastSysPath(path):
#    removeSysPath(path)
#    sys.path.append(path)

tests_path = os.path.dirname(os.path.normcase(os.path.abspath(__file__)))
prj_path   = os.path.dirname(tests_path)

setPathAsFirstSysPath(prj_path)
setPathAsFirstSysPath(tests_path)

