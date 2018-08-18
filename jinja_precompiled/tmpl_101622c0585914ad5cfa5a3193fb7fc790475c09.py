from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/statistics_tab/statistics_tab.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div ng-controller="StatisticsTab" ng-cloak>\n  <md-card class="oppia-editor-card" ng-if="!loadingMessage">\n    <div ng-if="explorationHasBeenVisited">\n      <div class="oppia-statistics-display">\n        <h3>Exploration Completion Rate</h3>\n        <pie-chart data="pieChartData"\n                   options="COMPLETION_RATE_PIE_CHART_OPTIONS">\n        </pie-chart>\n        <p style="text-align: center;"><span ng-if="numPassersby" style="font-weight: bold;" class="protractor-test-num-passersby"><[numPassersby]></span><span ng-if="!numPassersby" style="font-weight: bold;">0</span> learners browsed this exploration. They left before reaching the second card.</p>\n\n        <h3>Card statistics</h3>\n        <div style="font-size: smaller" ng-if="lastUpdated">\n          <em>Last updated: <[getLocaleAbbreviatedDatetimeString(lastUpdated)]></em>\n        </div>\n        <div class="container">\n          <div class="row">\n            <div class="col-lg-12 col-md-12 col-sm-12">\n              <div state-graph-viz graph-data="statsGraphData"\n                   node-fill="darkseagreen"\n                   highlight-states="highlightStates"\n                   state-stats="stateStats"\n                   on-click-function="onClickStateInStatsGraph">\n              </div>\n            </div>\n          </div>\n          <div class="container">\n            <issues-directive/>\n          </div>\n        </div>\n      </div>\n    </div>\n    <div ng-if="!explorationHasBeenVisited">\n      <em>\n        This exploration has not been visited by anyone yet, so there are no statistics to display.\n      </em>\n    </div>\n  </md-card>\n</div>'

blocks = {}
debug_info = ''