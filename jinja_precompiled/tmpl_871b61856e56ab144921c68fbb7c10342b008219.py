from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/LearnerViewRatingService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Service for the rating functionality in the learner view.\n */\n\noppia.factory(\'LearnerViewRatingService\', [\n  \'$http\', \'$rootScope\', \'ExplorationEngineService\',\n  function($http, $rootScope, ExplorationEngineService) {\n    var explorationId = ExplorationEngineService.getExplorationId();\n    var ratingsUrl = \'/explorehandler/rating/\' + explorationId;\n    var userRating;\n    return {\n      init: function(successCallback) {\n        $http.get(ratingsUrl).then(function(response) {\n          successCallback(response.data.user_rating);\n          userRating = response.data.user_rating;\n          $rootScope.$broadcast(\'ratingServiceInitialized\');\n        });\n      },\n      submitUserRating: function(ratingValue) {\n        $http.put(ratingsUrl, {\n          user_rating: ratingValue\n        });\n        userRating = ratingValue;\n        $rootScope.$broadcast(\'ratingUpdated\');\n      },\n      getUserRating: function() {\n        return userRating;\n      }\n    };\n  }\n]);'

blocks = {}
debug_info = ''