"""
Copyright 2014 Quentin Kaiser

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from tag import Tag


class Folder(Tag):
    """
    A Nessus Folder instance.

    Attributes:

    _Google Python Style Guide:
    http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
    """

    def __init__(self, server):
        """Constructor"""
        super(Folder, self).__init__(server)

    def create(self):
        """
        Create a folder.
        Params:
        Returns:
        """
        if self._server.server_version[0] == "6":
            params = {
                "name": self.name
            }
            response = self.request("POST", "/folders", params)
            if response is not None:
                self.id = response["id"]
                return True
            else:
                return False
        else:
            return False

    def edit(self):
        """
        Edit a folder
        Params:
        Returns:
        """
        if self._server.server_version[0] == "6":
            params = {
                "name": self.name
            }
            response = self.request("PUT", "/folders/%d" % self.id, params)
            if response is None:
                return True
            else:
                return False
        else:
            return False

    def delete(self):
        """
        Delete a folder.
        Params:
        Returns:
        """
        if self._server.server_version[0] == "6":
            response = self.request("DELETE", "/folders/%d" % self.id, "")
            if response is None:
                return True
            else:
                return False
        else:
            return False