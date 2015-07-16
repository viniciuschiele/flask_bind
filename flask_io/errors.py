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


class FlaskIOError(Exception):
    pass


class ContentTypeNotSupported(FlaskIOError):
    def __init__(self, content_type, *args, **kwargs):
        super().__init__(args, kwargs)
        self.content_type = content_type


class InvalidArgumentError(FlaskIOError):
    def __init__(self, arg_name, *args, **kwargs):
        super().__init__(arg_name, args, kwargs)
        self.arg_name = arg_name


class RequiredArgumentError(FlaskIOError):
    def __init__(self, arg_name, *args, **kwargs):
        super().__init__(arg_name, args, kwargs)
        self.arg_name = arg_name


class RequiredPayloadError(FlaskIOError):
    pass


class InvalidPayloadError(FlaskIOError):
    pass