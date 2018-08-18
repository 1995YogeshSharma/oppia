from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/UserServiceSpecs.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Tests that the user service is working as expected.\n */\n\ndescribe(\'User Service\', function() {\n  var UserService;\n\n  beforeEach(module(\'oppia\'));\n  beforeEach(inject(function($injector) {\n    UserService = $injector.get(\'UserService\');\n    UrlInterpolationService = $injector.get(\n      \'UrlInterpolationService\');\n    $httpBackend = $injector.get(\'$httpBackend\');\n  }));\n\n  it(\'should return image data\', function() {\n    var requestUrl = \'/preferenceshandler/profile_picture\';\n    $httpBackend.expect(\'GET\', requestUrl).respond(200, {\n      profile_picture_data_url: \'image data\'\n    });\n\n    UserService.getProfileImageDataUrlAsync().then(function(dataUrl) {\n      expect(dataUrl).toBe(\'image data\');\n    });\n    $httpBackend.flush();\n\n    $httpBackend.expect(\'GET\', requestUrl).respond(404);\n\n    UserService.getProfileImageDataUrlAsync().then(function(dataUrl) {\n      expect(dataUrl).toBe(UrlInterpolationService.getStaticImageUrl(\n        \'/avatar/user_blue_72px.png\'));\n    });\n    $httpBackend.flush();\n  });\n});'

blocks = {}
debug_info = ''