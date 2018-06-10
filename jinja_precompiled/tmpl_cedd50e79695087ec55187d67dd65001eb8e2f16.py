from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/exploration_graph.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div ng-controller="ExplorationGraph" ng-show="isGraphShown()" class="oppia-state-graph-animate-show">\n  <span style="font-size: 16px;">\n    <strong>Exploration Overview</strong>\n  </span>\n\n  <md-card style="background-color: white; margin: 20px 0px; padding: 8px;">\n    <div class="oppia-state-graph-container protractor-test-exploration-graph">\n      <div state-graph-viz graph-data="getGraphData()" current-state-id="getActiveStateName()" on-click-function="onClickStateInMinimap" on-delete-function="deleteState" on-maximize-function="openStateGraphModal" allow-panning="true" center-at-current-state="true" style="height: 100%;" is-editable="isEditable()" show-warning-sign="true">\n      </div>\n    </div>\n  </md-card>\n</div>'

blocks = {}
debug_info = ''