from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/translation_tab/state_translation_status_graph_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<span style="font-size: 16px;">\n  <strong>Exploration Overview</strong>\n</span>\n\n<md-card style="background-color: white; margin: 20px 0px; padding: 8px;">\n  <div class="oppia-translation-state-graph-container protractor-test-translation-graph">\n    <div state-graph-viz graph-data="getGraphData()" current-state-id="getActiveStateName()" on-click-function="onClickStateInMap" allow-panning="true" center-at-current-state="true" node-colors="nodeColors()" show-translation-warnings="true" style="height: 100%;">\n    </div>\n  </div>\n</md-card>'

blocks = {}
debug_info = ''