from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/state_graph_visualization_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<!-- NOTE TO DEVELOPERS: The svg defs needed for this directive are\nincluded at the bottom of exploration_editor.html. In order for the\nelements to render properly in Firefox, there cannot be multiple defs\nwith the same id on the page. -->\n\n<style>\n  .oppia-graph-viz .pannable-rect {\n    cursor: move;\n    fill: none;\n    fill-opacity: 0;\n    pointer-events: all;\n  }\n  .oppia-graph-viz path.link {\n    fill: none;\n    stroke: rgb(179, 179, 179);\n    stroke-width: 3px;\n  }\n  .oppia-graph-viz text {\n    font: 12px sans-serif;\n    pointer-events: none;\n  }\n  .oppia-graph-viz text.shadow {\n    stroke: #fff;\n    stroke-width: 3px;\n    stroke-opacity: .8;\n  }\n  .oppia-graph-viz .node rect {\n    fill: #fff;\n    pointer-events: all;\n    stroke: rgb(0, 0, 0);\n    -moz-transition: all 0.15s;\n    -webkit-transition: all 0.15s;\n    -o-transition: all 0.15s;\n    transition: all 0.15s;\n  }\n  .oppia-graph-viz .node rect.terminal-node {\n    fill: green; /* terminal nodes are green to signify them */\n  }\n  .oppia-graph-viz .node rect.bad-node {\n    fill: #F35F55;\n  }\n  .oppia-graph-viz .node rect.current-node:hover,\n  .oppia-graph-viz .node rect.init-node:hover,\n  .oppia-graph-viz .node rect.terminal-node:hover,\n  .oppia-graph-viz .node rect.bad-node:hover,\n  .oppia-graph-viz .node rect.normal-node:hover {\n    fill: #C8C4C4;\n  }\n  .oppia-graph-viz .clickable {\n    cursor: pointer;\n  }\n  .oppia-graph-viz .legend-bar {\n    fill: url(\'#nodegradient\');\n    stroke: black;\n    stroke-width: 0.5;\n  }\n\n  .oppia-state-graph-container .oppia-graph-resize-button {\n    border: 0;\n    padding: 9px 10px 6px 10px;\n    position: absolute;\n    right: 2px;\n    top: 2px;\n  }\n</style>\n\n<div style="height: <[getGraphHeightInPixels()]>px;" ng-show="graphLoaded">\n  <button ng-if="!!onMaximizeFunction" ng-click="onMaximizeFunction()"\n          class="btn btn-default btn-sm oppia-graph-resize-button">\n    <i title="Expand Map" class="material-icons" style="font-size: larger;">&#xE56B;</i>\n  </button>\n\n  <svg class="oppia-graph-viz" width="100%" height="100%">\n    <g>\n      <g ng-attr-transform="<[overallTransformStr]>">\n        <rect class="pannable-rect" ng-if="allowPanning"\n              ng-attr-width="<[VIEWPORT_WIDTH]>" ng-attr-height="<[VIEWPORT_HEIGHT]>"\n              ng-attr-x="<[VIEWPORT_X]>" ng-attr-y="<[VIEWPORT_Y]>">\n        </rect>\n\n        <g>\n          <g class="pannable-child" ng-attr-transform="<[innerTransformStr]>">\n            <g ng-repeat="link in augmentedLinks">\n              <path class="link protractor-test-link" ng-if="link.d" ng-attr-d="<[link.d]>" marker-end="url(#arrowhead)" ng-attr-style="<[link.style]>">\n              </path>\n            </g>\n\n            <g class="node protractor-test-node" ng-repeat="node in nodeList">\n              <rect rx="2" ry="2" ng-attr-height="<[node.height]>" ng-attr-width="<[node.width]>"\n                    class="protractor-test-node-background <[node.nodeClass]>"\n                    ng-attr-x="<[node.x0]>" ng-attr-y="<[node.y0]>"\n                    ng-class="{\'clickable\': canNavigateToNode(node.id)}"\n                    ng-attr-style="<[node.style]>"\n                    ng-click="onClickFunction(node.id)">\n              </rect>\n              <title><[getNodeTitle(node)]></title>\n              <text text-anchor="middle" ng-attr-x="<[node.xLabel]>" ng-attr-y="<[node.yLabel]>" class="protractor-test-node-label">\n                <tspan alignment-baseline="central"><[getTruncatedLabel(node.label)]></tspan>\n                <tspan ng-attr-x="<[node.xLabel]>" dy="1em" style="fill:gray"><[getTruncatedLabel(node.secondaryLabel)]></tspan>\n              </text>\n              <g ng-if="getNodeErrorMessage(node.label) && showWarningSign">\n                <rect ng-click="onClickFunction(node.id)" class="clickable"\n                      style="fill: yellow;" width="22" height="22"\n                      ng-attr-x="<[node.x0]>" ng-attr-y="<[node.y0 - 8]>"\n                      ng-attr-transform="<[getHighlightTransform(node.x0, node.y0)]>"\n                      uib-tooltip="<[getNodeErrorMessage(node.label)]>"\n                      tooltip-placement="top" tooltip-animation="true"\n                      tooltip-append-to-body="true">\n                </rect>\n                <text fill="firebrick" text-anchor="middle" ng-attr-x="<[node.x0 + 11]>"\n                    ng-attr-y="<[node.y0 + 9]>"\n                    style="font-size: 22px; font-weight: bold;"\n                    ng-attr-transform="<[getHighlightTextTransform(node.x0, node.y0)]>">\n                  \u26a0\n                </text>\n              </g>\n              <g ng-if="isEditable && onDeleteFunction && node.canDelete" class="protractor-test-delete-node">\n                <rect height="15" width="15" opacity="0" stroke-width="0"\n                      ng-attr-x="<[node.x0 + node.width]>" ng-attr-y="<[node.y0]>"\n                      transform="translate(0, -15)"\n                      class="clickable"\n                      style="fill: pink; cursor: pointer;"\n                      ng-click="onNodeDeletionClick(node.id)"></rect>\n                <text ng-attr-dx="<[node.x0 + node.width]>" ng-attr-dy="<[node.y0]>" text-anchor="right">\n                  x\n                </text>\n              </g>\n              <g ng-if="highlightStates && isStateFlagged(node.id)">\n                <rect ng-click="onClickFunction(node.id)" class="highlight clickable"\n                      width="22" height="22" ng-attr-x="<[node.x0]>" ng-attr-y="<[node.y0]>"\n                      ng-attr-transform="<[getHighlightTransform(node.x0, node.y0)]>">\n                </rect>\n                <text fill="firebrick" text-anchor="middle" ng-attr-x="<[node.x0 + 11]>"\n                      ng-attr-y="<[node.y0 + 17]>" style="font-size: 22px;"\n                      ng-attr-transform="<[getHighlightTextTransform(node.x0, node.y0)]>">\n                  \u26a0\n                </text>\n              </g>\n            </g>\n          </g>\n\n          <g ng-if="opacityMap">\n            <rect width="210" height="70" ng-attr-x="<[GRAPH_WIDTH - 250]>" y="10" style="fill: transparent; stroke: black;">\n            </rect>\n\n            <rect width="190" height="20" ng-attr-x="<[GRAPH_WIDTH - 240]>" y="20"\n                  class="legend-bar">\n            </rect>\n\n            <text ng-attr-x="<[GRAPH_WIDTH - 200]>" y="60">\n              <[opacityMap.legend]>\n            </text>\n          </g>\n        </g>\n      </g>\n    </g>\n  </svg>\n</div>'

blocks = {}
debug_info = ''