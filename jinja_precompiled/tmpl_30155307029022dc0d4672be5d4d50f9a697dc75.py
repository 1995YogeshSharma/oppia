from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/preview_tab/preview_set_parameters_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-body oppia-preview-set-params-modal">\n  <p>Please enter values for the following parameters:</p>\n  <table class="oppia-preview-set-params-modal-table">\n    <tr ng-repeat="paramChange in manualParamChanges">\n      <td class="oppia-preview-set-params-modal-td">\n        <[paramChange.name]>\n      </td>\n      <td class="oppia-preview-set-params-modal-td">\n        <input type="text" ng-model="paramChange.customizationArgs.value">\n      </td>\n    </tr>\n  </table>\n  <button class="btn btn-success" ng-click="previewParamModalOk()">\n    OK\n  </button>\n  <button class="btn btn-danger" ng-click="previewParamModalCancel()">\n    Cancel\n  </button>\n</div>\n\n<style>\n  .oppia-preview-set-params-modal {\n    padding: 15px 10px 15px 10px;\n  }\n  .oppia-preview-set-params-modal .oppia-preview-set-params-modal-table {\n    margin: 5px 0px 15px 0px\n  }\n  .oppia-preview-set-params-modal .oppia-preview-set-params-modal-td {\n    padding: 1px 5px;\n  }\n</style>'

blocks = {}
debug_info = ''