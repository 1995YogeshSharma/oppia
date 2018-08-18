from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/skill/SkillSummaryObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating and mutating instances of frontend\n * skill summary domain objects.\n */\n\noppia.factory(\'SkillSummaryObjectFactory\', [\n  function() {\n    var SkillSummary = function(skillId, skillDescription) {\n      this._id = skillId;\n      this._description = skillDescription;\n    };\n\n    // Instance methods\n\n    SkillSummary.prototype.getId = function() {\n      return this._id;\n    };\n\n    SkillSummary.prototype.getDescription = function() {\n      return this._description;\n    };\n\n\n    SkillSummary.create = function(skillId, skillDescription) {\n      return new SkillSummary(skillId, skillDescription);\n    };\n\n    return SkillSummary;\n  }\n]);'

blocks = {}
debug_info = ''