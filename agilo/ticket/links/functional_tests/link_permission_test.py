#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#   Copyright 2008 Agile42 GmbH, Berlin (Germany)
#   Copyright 2007 Andrea Tomasini <andrea.tomasini_at_agile42.com>
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
#   Author: 
#       - Felix Schwarz <felix.schwarz__at__agile42.com>

from trac.tests.functional import tc
from twill.errors import TwillAssertionError

from agilo.utils import Type
from agilo.test import Usernames
from agilo.test.functional import AgiloFunctionalTestCase


class TestTeamMembersCanNotDeleteLinks(AgiloFunctionalTestCase):
    def runTest(self):
        self._tester.login_as(Usernames.product_owner)
        story_id = self._tester.create_new_agilo_userstory('as a product owner...')
        self._tester.assign_ticket_to(story_id, Usernames.team_member)
        
        self._tester.login_as(Usernames.team_member)
        task_id = self._tester.create_referenced_ticket(story_id, Type.TASK, 'we should do that.')
        self._tester.go_to_view_ticket_page(task_id)
        self.assertRaises(TwillAssertionError, tc.formvalue, 'delete_link', 'cmd', 'submit')


class TestProductOwnerCanDeleteLinks(AgiloFunctionalTestCase):
    def runTest(self):
        self._tester.login_as(Usernames.product_owner)
        story_id = self._tester.create_new_agilo_userstory('as a product owner...')
        self._tester.assign_ticket_to(story_id, Usernames.team_member)
        
        self._tester.login_as(Usernames.team_member)
        self._tester.create_referenced_ticket(story_id, Type.TASK, 'we should do that.')
        
        self._tester.login_as(Usernames.product_owner)
        self._tester.go_to_view_ticket_page(story_id)
        tc.formvalue('delete_link', 'cmd', 'submit')
        tc.submit('cmd')


if __name__ == '__main__':
    from agilo.test.testfinder import run_all_tests
    run_all_tests(__file__)

