from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/statistics_tab/cyclic_transitions_issue_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="row oppia-issues-row-eq-height oppia-issues-bor-left oppia-issues-issue-dir">\n  <div class="col-md-3 oppia-issues-bor-btm oppia-issues-bor-right text-center oppia-pt2 oppia-pb2 oppia-issues-bg-clr oppia-issues-text-white">\n    <div style="font-size: 1.3em;">\n      Issue <[currentIssueIdentifier]>\n    </div>\n  </div>\n  <div class="col-md-9 oppia-issues-bor-left text-center d-flex justify-content-center oppia-issues-bor-btm oppia-pt2 oppia-pb2 protractor-test-issue-title">\n    <[issueStatement]>\n  </div>\n</div>\n<div class="row oppia-pt4">\n  <p class="oppia-issues-suggestion-header">To resolve this issue, the suggested approach is: </p>\n  <div class="oppia-pt2">\n    <ul class="oppia-issues-tips">\n      <li ng-repeat="suggestion in suggestions" ng-bind-html="suggestion"></li>\n    </ul>\n  </div>\n</div>\n<div class="row oppia-pt2">\n  <p class="oppia-issues-suggestion-header">Sample Playthroughs: </p>\n</div>\n<div class="text-center">\n  <div class="row">\n    <div ng-repeat="playthroughId in playthroughIds" class="col-md-4" style="margin-left: -40px;">\n      <div class="oppia-hexagon">\n        <div class="oppia-issues-hexagon-text">\n          <button type="button" ng-click="showPlaythrough(playthroughId)" class="oppia-issues-playthrough-modal-btn oppia-issues-playthrough-content" style="padding-top: 20px; padding-right: 5px;">\n            View <br> Playthrough <[createPlaythroughNavId(playthroughId)]>\n          </button>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="row">\n    <div class="oppia-pt4 oppia-pb2">\n      <button type="button" ng-click="resolveIssue()" class="oppia-issues-bg-clr oppia-issues-text-white oppia-ft-14 oppia-issues-btn-resolve protractor-test-issue-resolve">\n          Mark as Resolved\n      </button>\n    </div>\n  </div>\n</div>'

blocks = {}
debug_info = ''