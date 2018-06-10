from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/admin/roles_tab/role_graph_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  .oppia-static-graph path.link {\n    fill: none;\n    stroke: rgb(179, 179, 179);\n    stroke-width: 3px;\n  }\n  .oppia-static-graph text {\n    font: 12px sans-serif;\n    pointer-events: none;\n  }\n  .oppia-static-graph text.shadow {\n    stroke: #fff;\n    stroke-width: 3px;\n    stroke-opacity: .8;\n  }\n  .oppia-static-graph .node rect {\n    fill: #fff;\n    pointer-events: all;\n    stroke: rgb(0, 0, 0);\n    -moz-transition: all 0.15s;\n    -webkit-transition: all 0.15s;\n    -o-transition: all 0.15s;\n    transition: all 0.15s;\n  }\n</style>\n\n<div style="height: <[getGraphHeightInPixels()]>px;">\n\n  <svg class="oppia-static-graph" width="100%" height="100%">\n    <g>\n      <g ng-repeat="link in augmentedLinks">\n        <path class="link protractor-test-link" ng-if="link.d" ng-attr-d="<[link.d]>" marker-end="url(#arrowhead)" ng-attr-style="<[link.style]>">\n        </path>\n      </g>\n\n      <g class="node protractor-test-node" ng-repeat="node in nodeList">\n        <rect rx="2" ry="2" ng-attr-height="<[node.height]>" ng-attr-width="<[node.width]>"\n              class="protractor-test-node-background <[node.nodeClass]>"\n              ng-attr-x="<[node.x0]>" ng-attr-y="<[node.y0]>"\n              ng-attr-style="<[node.style]>">\n        </rect>\n        <title><[getNodeTitle(node)]></title>\n        <text text-anchor="middle" ng-attr-x="<[node.xLabel]>" ng-attr-y="<[node.yLabel]>" class="protractor-test-node-label">\n          <tspan alignment-baseline="central"><[getTruncatedLabel(node.label)]></tspan>\n        </text>\n      </g>\n    </g>\n  </svg>\n</div>'

blocks = {}
debug_info = ''