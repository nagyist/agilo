# -*- coding: utf-8 -*-
#   Copyright 2008 Agile42 GmbH, Berlin (Germany)
#   Copyright 2007 Andrea Tomasini <andrea.tomasini__at__agile42.com>
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
#   
#    Authors: 
#           Andrea Tomasini <andrea.tomasini__at__agile42.com>
"""
Module containing core controller components
"""

from agilo.api import controller


class PersistentObjectController(controller.Controller):
    """
    Persistent Object Controller, is an abstract class that provides
    standard command implementations for Get, Create, Delete and Select
    of a PersistentObject
    """
    pass