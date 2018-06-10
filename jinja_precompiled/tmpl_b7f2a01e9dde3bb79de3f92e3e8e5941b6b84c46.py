from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/version_diff_visualization_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div ng-hide="diffGraphData" class="oppia-align-center">\n  Loading\n  <loading-dots></loading-dots>\n</div>\n\n<div class="row">\n  <div class="col-sm-8 col-md-8 col-lg-8">\n    <div state-graph-viz class="protractor-test-history-graph diff-graph"\n         graph-data="diffGraphData" node-colors="diffGraphNodeColors"\n         node-secondary-labels="diffGraphSecondaryLabels"\n         init-state-id2="v1InitStateId"\n         link-property-mapping="DIFF_GRAPH_LINK_PROPERTY_MAPPING"\n         on-click-function="onClickStateInDiffGraph">\n    </div>\n  </div>\n\n  <div class="col-sm-4 col-md-4 col-lg-4">\n    <div class="legend-graph" ng-show="diffGraphData">\n      <h4>Exploration Graph Legend</h4>\n      <div state-graph-viz graph-data="legendGraph"\n           node-colors="LEGEND_GRAPH_COLORS"\n           node-secondary-labels="LEGEND_GRAPH_SECONDARY_LABELS"\n           link-property-mapping="LEGEND_GRAPH_LINK_PROPERTY_MAPPING"\n           id="legend-graph">\n      </div>\n    </div>\n  </div>\n</div>\n\n<style>\n  .legend-graph .node rect {\n    pointer-events: none;\n  }\n  .legend-graph {\n    position: absolute;\n    right: -100px;\n    top: 10px;\n  }\n</style>'

blocks = {}
debug_info = ''