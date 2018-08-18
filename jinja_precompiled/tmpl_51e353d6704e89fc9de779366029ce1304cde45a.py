from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/skill/SkillObjectFactorySpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n* @fileoverview Unit tests for SkillObjectFactory.\n*/\n\ndescribe(\'Skill object factory\', function() {\n  beforeEach(module(\'oppia\'));\n\n  describe(\'SkillObjectFactory\', function() {\n    var SkillObjectFactory = null;\n    var MisconceptionObjectFactory = null;\n    var ConceptCardObjectFactory = null;\n    var misconceptionDict1 = null;\n    var misconceptionDict2 = null;\n    var skillContentsDict = null;\n    var skillDict = null;\n\n    beforeEach(inject(function($injector) {\n      SkillObjectFactory = $injector.get(\'SkillObjectFactory\');\n      MisconceptionObjectFactory = $injector.get(\'MisconceptionObjectFactory\');\n      ConceptCardObjectFactory = $injector.get(\'ConceptCardObjectFactory\');\n\n      misconceptionDict1 = {\n        id: 2,\n        name: \'test name\',\n        notes: \'test notes\',\n        feedback: \'test feedback\'\n      };\n\n      misconceptionDict2 = {\n        id: 4,\n        name: \'test name\',\n        notes: \'test notes\',\n        feedback: \'test feedback\'\n      };\n\n      skillContentsDict = {\n        explanation: \'test explanation\',\n        worked_examples: [\'test worked_example 1\', \'test worked example 2\']\n      };\n\n      skillDict = {\n        id: \'1\',\n        description: \'test description\',\n        misconceptions: [misconceptionDict1, misconceptionDict2],\n        skill_contents: skillContentsDict,\n        language_code: \'en\',\n        version: 3,\n        next_misconception_id: 6\n      };\n    }));\n\n    it(\'should create a new skill from a backend dictionary\', function() {\n      var skill = SkillObjectFactory.createFromBackendDict(skillDict);\n      expect(skill.getId()).toEqual(\'1\');\n      expect(skill.getDescription()).toEqual(\'test description\');\n      expect(skill.getMisconceptions()).toEqual(\n        [MisconceptionObjectFactory.createFromBackendDict(\n          misconceptionDict1),\n        MisconceptionObjectFactory.createFromBackendDict(\n          misconceptionDict2)]);\n      expect(skill.getConceptCard()).toEqual(\n        ConceptCardObjectFactory.createFromBackendDict(skillContentsDict));\n      expect(skill.getLanguageCode()).toEqual(\'en\');\n      expect(skill.getVersion()).toEqual(3);\n    });\n\n    it(\'should delete a misconception given its id\', function() {\n      var skill = SkillObjectFactory.createFromBackendDict(skillDict);\n      skill.deleteMisconception(2);\n      expect(skill.getMisconceptions()).toEqual(\n        [MisconceptionObjectFactory.createFromBackendDict(\n          misconceptionDict2)]);\n    });\n\n    it(\'should get the correct next misconception id\', function() {\n      var skill = SkillObjectFactory.createFromBackendDict(skillDict);\n      expect(skill.getNextMisconceptionId()).toEqual(6);\n      skill.deleteMisconception(4);\n      expect(skill.getNextMisconceptionId()).toEqual(6);\n\n      var misconceptionToAdd1 = MisconceptionObjectFactory\n        .createFromBackendDict({\n          id: skill.getNextMisconceptionId(),\n          name: \'test name\',\n          notes: \'test notes\',\n          feedback: \'test feedback\',\n        });\n\n      skill.appendMisconception(misconceptionToAdd1);\n      expect(skill.getNextMisconceptionId()).toEqual(7);\n      skill.deleteMisconception(6);\n      expect(skill.getNextMisconceptionId()).toEqual(7);\n    });\n\n    it(\'should convert to a backend dictionary\', function() {\n      var skill = SkillObjectFactory.createFromBackendDict(skillDict);\n      expect(skill.toBackendDict()).toEqual(skillDict);\n    });\n\n    it(\'should be able to create an interstitial skill\', function() {\n      var skill = SkillObjectFactory.createInterstitialSkill();\n      expect(skill.getId()).toEqual(null);\n      expect(skill.getDescription()).toEqual(\'Skill description loading\');\n      expect(skill.getMisconceptions()).toEqual([]);\n      expect(skill.getConceptCard()).toEqual(\n        ConceptCardObjectFactory.createInterstitialConceptCard());\n      expect(skill.getLanguageCode()).toEqual(\'en\');\n      expect(skill.getVersion()).toEqual(1);\n    });\n  });\n});'

blocks = {}
debug_info = ''