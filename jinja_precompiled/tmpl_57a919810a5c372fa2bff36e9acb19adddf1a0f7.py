from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/UserService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for user data.\n */\n\noppia.factory(\'UserService\', [\n  \'$http\', \'$q\', \'UrlInterpolationService\', \'DEFAULT_PROFILE_IMAGE_PATH\',\n  function($http, $q, UrlInterpolationService, DEFAULT_PROFILE_IMAGE_PATH) {\n    var _isLoggedIn = GLOBALS.userIsLoggedIn;\n    var PREFERENCES_DATA_URL = \'/preferenceshandler/data\';\n\n    return {\n      getProfileImageDataUrlAsync: function() {\n        var profilePictureDataUrl = (\n          UrlInterpolationService.getStaticImageUrl(\n            DEFAULT_PROFILE_IMAGE_PATH));\n\n        if (_isLoggedIn) {\n          return $http.get(\n            \'/preferenceshandler/profile_picture\'\n          ).then(function(response) {\n            if (response.data.profile_picture_data_url) {\n              profilePictureDataUrl = response.data.profile_picture_data_url;\n            }\n            return profilePictureDataUrl;\n          });\n        } else {\n          return $q.resolve(profilePictureDataUrl);\n        }\n      },\n      setProfileImageDataUrlAsync: function(newProfileImageDataUrl) {\n        return $http.put(PREFERENCES_DATA_URL, {\n          update_type: \'profile_picture_data_url\',\n          data: newProfileImageDataUrl\n        });\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''