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
from nessusobject import NessusObject

class Agent(NessusObject):
    """
    A Nessus scanning agent.

    Attributes:
        id(int): identification
        distros(str) :
        ip(str):
        last_scanned(int):
        name(str): agent's name
        platform(str):
        token(str):
        uuid(str):
        scanner_id(int):

    _Google Python Style Guide:
    http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
    """

    def __init__(self, server):
        """Constructor"""
        super(Agent, self).__init__(server)
        self._distros = None
        self._id = None
        self._ip = None
        self._last_scanned = None
        self._name = None
        self._platform = None
        self._token = None
        self._uuid = None
        self._scanner_id = None

    def delete(self):
        """
        Delete the agent instance.
        Params:
        Returns:
        """
        response = self._server._api_request(
            "DELETE",
            "/scanners/%d/agents/%d" % (self._scanner_id, self.id),
            ""
        )
        if response is not None:
            return True
        else:
            return False

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = int(value)

    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = str(value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value)

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = str(value)

    @property
    def last_scanned(self):
        return self._last_scanned

    @last_scanned.setter
    def last_scanned(self, value):
        self._last_scanned = str(value)

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = int(value)

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = str(value)

    @property
    def scanner_id(self):
        return self._scanner_id

    @scanner_id.setter
    def scanner_id(self, value):
        self._scanner_id = int(value)