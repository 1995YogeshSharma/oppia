from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/unresolved_answers_overview_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  unresolved-answers-overview .answer-container {\n    vertical-align: text-bottom;\n  }\n  unresolved-answers-overview .refresh-container {\n    font-size: 0.8em;\n    text-align: right;\n  }\n  unresolved-answers-overview .refresh-container a {\n    font-weight: bold;\n  }\n</style>\n\n<div ng-show="unresolvedAnswersData !== null">\n  <strong>Unresolved Student Answers</strong>\n  <ul>\n    <li ng-repeat="data in unresolvedAnswersData" class="answer-container">\n      <strong>(<[data.frequency]> times)</strong>: <span ng-bind-html="data.answer"></span>\n    </li>\n    <li ng-if="unresolvedAnswersData.length === 0">\n      <em>No outstanding answers requiring attention.</em>\n    </li>\n  </ul>\n  <div class="refresh-container">\n    <a ng-click="computeUnresolvedAnswers()">Refresh</a>; last updated: <[latestRefreshDate.toLocaleString()]>.\n  </div>\n</div>'

blocks = {}
debug_info = ''