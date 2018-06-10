from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'services/AutoplayedVideosService.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n// About this service:\n// In the exploration player, a video should only autoplay when it is first seen\n// on a new card, and not when the learner clicks back to previous cards in\n// their exploration playthrough. This service maintains a list of videos that\n// have been played, so that we know not to autoplay them on a second pass.\n//\n// Caveat: if the same video is shown twice in the exploration, the second and\n// subsequent instances of that video will not autoplay. We believe this\n// occurrence is rare, and have not accounted for it here. If it turns out\n// to be an issue, we may need to instead assign a unique id to each rich-text\n// component and use that id instead to determine whether to suppress\n// autoplaying.\n\noppia.factory(\'AutoplayedVideosService\', [function() {\n  var autoplayedVideosDict = {};\n  return {\n    addAutoplayedVideo: function(videoId) {\n      autoplayedVideosDict[videoId] = true;\n    },\n\n    hasVideoBeenAutoplayed: function(videoId) {\n      return Boolean(autoplayedVideosDict[videoId]);\n    }\n  };\n}]);'

blocks = {}
debug_info = ''