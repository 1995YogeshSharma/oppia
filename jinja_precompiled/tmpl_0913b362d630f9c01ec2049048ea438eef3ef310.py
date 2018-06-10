from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/history_tab/revert_exploration_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Revert Exploration</h3>\n</div>\n\n<div class="modal-body oppia-long-text">\n  <p>\n    You are about to revert this exploration to version <[version]>. All changes made since that older version will be retracted and you will lose any unsaved changes.\n  </p>\n  <p>\n    Before reverting, you can preview the exploration you are reverting to by following <a ng-href="<[getExplorationUrl(version)]>" target="_blank">this link</a>. (It opens in a new window.)\n  </p>\n  <p>\n    Are you sure you want to revert this exploration to version <[version]>?\n  </p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-danger protractor-test-confirm-revert" ng-click="revert()">Revert</button>\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n</div>'

blocks = {}
debug_info = ''