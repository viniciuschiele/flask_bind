# Copyright 2015 Vinicius Chiele. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask_io.validate import Complexity
from marshmallow.validate import ValidationError
from unittest import TestCase


class TestComplexity(TestCase):
    def test_upper(self):
        validator = Complexity(upper=1)
        self.assertEqual(validator('Hello'), 'Hello')

        validator = Complexity(upper=2)
        self.assertEqual(validator('HeLlo'), 'HeLlo')

        validator = Complexity(upper=1)
        self.assertRaises(ValidationError, validator, 'hello')

        validator = Complexity(upper=2)
        self.assertRaises(ValidationError, validator, 'Hello')

    def test_lower(self):
        validator = Complexity(lower=1)
        self.assertEqual(validator('hELLO'), 'hELLO')

        validator = Complexity(lower=2)
        self.assertEqual(validator('hELlO'), 'hELlO')

        validator = Complexity(lower=1)
        self.assertRaises(ValidationError, validator, 'HELLO')

        validator = Complexity(lower=2)
        self.assertRaises(ValidationError, validator, 'hELLO')

    def test_letters(self):
        validator = Complexity(letters=1)
        self.assertEqual(validator('123s'), '123s')

        validator = Complexity(letters=2)
        self.assertEqual(validator('i23s'), 'i23s')

        validator = Complexity(letters=1)
        self.assertRaises(ValidationError, validator, '1234')

        validator = Complexity(letters=2)
        self.assertRaises(ValidationError, validator, '123s')

    def test_digits(self):
        validator = Complexity(digits=1)
        self.assertEqual(validator('hell0'), 'hell0')

        validator = Complexity(digits=2)
        self.assertEqual(validator('he1l0'), 'he1l0')

        validator = Complexity(digits=1)
        self.assertRaises(ValidationError, validator, 'hello')

        validator = Complexity(digits=2)
        self.assertRaises(ValidationError, validator, 'hell0')

    def test_special(self):
        validator = Complexity(special=1)
        self.assertEqual(validator('hell@'), 'hell@')

        validator = Complexity(special=2)
        self.assertEqual(validator('he?l@'), 'he?l@')

        validator = Complexity(special=1)
        self.assertRaises(ValidationError, validator, 'hello')

        validator = Complexity(special=2)
        self.assertRaises(ValidationError, validator, 'hell@')