"""
-------------
Project tests
-------------
"""

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest


@pytest.mark.usefixtures('admin_only')
class TestAdminOnly(object):
    """Tests for admin only."""

    @pytest.mark.idempotent_id('fc80ee7d-ce5a-45eb-b476-427990b3b61d')
    def test_create_project(self, projects_steps_ui):
        """**Scenario:** Verify that admin can create project.

        **Steps:**

        #. Create project using UI
        #. Delete project using UI
        """
        project_name = projects_steps_ui.create_project()
        projects_steps_ui.delete_project(project_name)

    @pytest.mark.idempotent_id('fada00f4-4a73-41ba-af56-6fd915414da9')
    def test_try_to_disable_current_project(self, projects_steps_ui):
        """**Scenario:** Verify that project can't disable itself.

        **Steps:**

        #. Try to disable current project
        """
        projects_steps_ui.check_project_cant_disable_itself()

    @pytest.mark.idempotent_id('b3c20e6e-b2f1-4c74-89e6-e72eaad1dfb8')
    def test_manage_project_members(self, project, projects_steps_ui):
        """**Scenario:** Check we can manage project members.

        **Setup:**

        #. Create project with API

        **Steps:**

        #. Manage project members using UI

        **Teardown:**

        #. Delete project with UI
        """
        projects_steps_ui.manage_project_members(project)

    @pytest.mark.idempotent_id('83f706c1-6c1c-4a65-95e1-b045cd723fa1')
    def test_disable_enable_project(self, project, projects_steps_ui):
        """**Scenario:** Disable and enable created project.

        **Setup:**

        #. Create project with API

        **Steps:**

        #. Disable created project with UI
        #. Enable it using UI

        **Teardown:**

        #. Delete project via API
        """
        projects_steps_ui.toggle_project(project, enable=False)
        projects_steps_ui.toggle_project(project, enable=True)
