# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Describe a key."""

from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.api_lib.cloudkms import base as cloudkms_base
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.kms import flags


class Describe(base.DescribeCommand):
  """Get metadata for a given key.

  Returns metadata for the given key.

  ## EXAMPLES

  The following command returns metadata for the key `frodo` within
  the keyring `fellowship` in the location `us-east1`:

    $ {command} frodo --keyring fellowship --location us-east1
  """

  @staticmethod
  def Args(parser):
    flags.AddCryptoKeyArgument(parser, 'to describe')

  def Run(self, args):
    client = cloudkms_base.GetClientInstance()
    messages = cloudkms_base.GetMessagesModule()

    crypto_key_ref = flags.ParseCryptoKeyName(args)
    if not crypto_key_ref.Name():
      raise exceptions.InvalidArgumentException('key',
                                                'key id must be non-empty.')
    return client.projects_locations_keyRings_cryptoKeys.Get(
        messages.CloudkmsProjectsLocationsKeyRingsCryptoKeysGetRequest(
            name=crypto_key_ref.RelativeName()))
