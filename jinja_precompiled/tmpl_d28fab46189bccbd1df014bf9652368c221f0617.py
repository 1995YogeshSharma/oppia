from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/state_name_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div>\n  <span class="protractor-test-state-name-container">\n    <span ng-if="EditabilityService.isEditable()">\n      <span ng-if="!stateNameEditorIsShown" ng-click="openStateNameEditor()" class="oppia-editable-section">\n        <strong style="font-size: 1.2em;"><[stateName]></strong>\n        <i ng-if="EditabilityService.isEditable()" class="material-icons oppia-editor-edit-icon"\n           title="Edit State Name">&#xE254;\n        </i>\n      </span>\n\n      <span ng-if="stateNameEditorIsShown">\n        <form class="form-horizontal" role="form" ng-submit="saveStateNameAndRefresh($parent.$parent.tmpStateName)">\n          <input type="text" ng-model="$parent.$parent.tmpStateName" focus-on="stateNameEditorOpened" class="protractor-test-state-name-input">\n          <button type="submit" class="btn btn-success btn-sm protractor-test-state-name-submit">Save</button>\n        </form>\n      </span>\n    </span>\n\n    <span ng-if="!EditabilityService.isEditable()">\n      <strong><[stateName]></strong>\n    </span>\n  </span>\n</div>'

blocks = {}
debug_info = ''