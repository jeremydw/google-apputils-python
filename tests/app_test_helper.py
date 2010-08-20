#!/usr/bin/env python
# Copyright 2005 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Helper script used by app_unittest.sh"""



import sys

import gflags as flags
from google.apputils import app

FLAGS = flags.FLAGS
flags.DEFINE_boolean("raise_exception", False, "throw MyException from main")

class MyException(Exception):
  pass

def main(args):
  if FLAGS.raise_exception:
    raise MyException


if __name__ == '__main__':
  app.run()
