from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/skill_editor/editor_tab/skill_description_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-editor-header">\n  <span>\n    <span ng-if="!skillDescriptionEditorIsShown" ng-click="openSkillDescriptionEditor()" class="canEditSkillDescription()">\n      <strong style="font-size: 1.2em;"><[skill.getDescription()]></strong>\n      <i ng-if="canEditSkillDescription()"\n         class="material-icons oppia-editor-edit-icon"\n         title="Edit Skill Description">&#xE254;\n      </i>\n    </span>\n    <span ng-if="skillDescriptionEditorIsShown">\n      <form class="form-horizontal" role="form" ng-submit="saveSkillDescription($parent.tmpSkillDescription)">\n        <input type="text" ng-model="$parent.tmpSkillDescription" focus-on="skillDescriptionEditorOpened">\n        <button type="submit" class="btn btn-success btn-sm">Save</button>\n        <button class="btn btn-default btn-sm" ng-click="closeSkillDescriptionEditor()">Cancel</button>\n      </form>\n    </span>\n  </span>\n</div>\n<style>\n  skill-description-editor .oppia-editor-header {\n    margin-left: 12vw;\n  }\n</style>'

blocks = {}
debug_info = ''