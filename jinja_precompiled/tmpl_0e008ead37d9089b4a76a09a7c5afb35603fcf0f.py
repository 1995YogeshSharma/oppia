from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/exploration_graph_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Exploration Overview</h3>\n</div>\n\n<div class="modal-body" style="overflow-y: hidden; padding-bottom: 0;">\n  <div state-graph-viz style="height: 300px;" graph-data="graphData" allow-panning="true" current-state-id="currentStateName" on-click-function="selectState" on-delete-function="deleteState" center-at-current-state="true" is-editable="isEditable">\n  </div>\n</div>\n\n<div class="modal-footer" style="margin-top: 0; text-align: inherit;">\n  <span class="pull-right">\n    <button class="btn btn-default" ng-click="cancel()">Close</button>\n  </span>\n</div>'

blocks = {}
debug_info = ''