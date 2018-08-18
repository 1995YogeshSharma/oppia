from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/skill/SkillRightsObjectFactorySpec.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Tests for SkillRightsObjectFactory.\n */\n\ndescribe(\'Skill rights object factory\', function() {\n  var SkillRightsObjectFactory = null;\n\n  beforeEach(module(\'oppia\'));\n\n  beforeEach(inject(function($injector) {\n    SkillRightsObjectFactory = $injector.get(\'SkillRightsObjectFactory\');\n  }));\n\n  it(\'should be able to set public\', function() {\n    var initialSkillRightsBackendObject = {\n      skill_id: 0,\n      can_edit_skill_description: true,\n      creator_id: 0,\n      skill_is_private: true\n    };\n\n    var skillRights = SkillRightsObjectFactory.createFromBackendDict(\n      initialSkillRightsBackendObject);\n\n    expect(skillRights.isPublic()).toBe(false);\n    expect(skillRights.isPrivate()).toBe(true);\n\n    skillRights.setPublic();\n\n    expect(skillRights.isPublic()).toBe(true);\n    expect(skillRights.isPrivate()).toBe(false);\n  });\n\n  it(\'should create an interstitial skill rights object\', function() {\n    var interstitialSkillRights =\n      SkillRightsObjectFactory.createInterstitialSkillRights();\n\n    expect(interstitialSkillRights.getSkillId()).toEqual(null);\n    expect(interstitialSkillRights.getCreatorId()).toEqual(null);\n    expect(interstitialSkillRights.isPrivate()).toBe(true);\n    expect(interstitialSkillRights.canEditSkillDescription()).toBe(false);\n  });\n\n  it(\'should make a copy from another skill rights object\', function() {\n    var sampleSkillRightsObject = {\n      skill_id: \'1\',\n      can_edit_skill_description: true,\n      creator_id: \'2\',\n      skill_is_private: false\n    };\n\n    var sampleSkillRights = SkillRightsObjectFactory.createFromBackendDict(\n      sampleSkillRightsObject);\n\n    var interstitialSkillRights =\n      SkillRightsObjectFactory.createInterstitialSkillRights();\n\n    interstitialSkillRights.copyFromSkillRights(sampleSkillRights);\n    expect(interstitialSkillRights.getSkillId()).toEqual(\'1\');\n    expect(interstitialSkillRights.getCreatorId()).toEqual(\'2\');\n    expect(interstitialSkillRights.canEditSkillDescription()).toBe(true);\n    expect(interstitialSkillRights.isPrivate()).toBe(false);\n  });\n});'

blocks = {}
debug_info = ''