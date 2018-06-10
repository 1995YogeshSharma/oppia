from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/state_diff_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    Card name: <[newStateName]>\n    <span ng-show="oldStateName">(was: <[oldStateName]>)</span>\n  </h3>\n</div>\n\n<table class="table" style="margin-left: 20px; table-layout: fixed; width: 97%">\n  <!--\n    Spacing on the left of table and in the middle of the table is to\n    ensure text above each pane is aligned to codemirror gutter.\n   -->\n  <td style="width: 47%; word-wrap: break-word">\n    <div>\n      <[headers.leftPane]>\n    </div>\n  </td>\n  <td style="width: 6%"></td>\n  <td style="width: 47%; word-wrap: break-word">\n    <div>\n      <[headers.rightPane]>\n    </div>\n  </td>\n</table>\n\n<div class="modal-body" style="margin-top: -30px" ng-cloak>\n  <codemirror-mergeview options="CODEMIRROR_MERGEVIEW_OPTIONS"\n                        left-value="yamlStrs.leftPane"\n                        right-value="yamlStrs.rightPane">\n  </codemirror-mergeview>\n  <div align="center" style="margin-bottom: 20px">\n    <strong>Click arrows to desynchronize scrolling</strong>\n  </div>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default protractor-test-close-history-state-modal"\n          ng-click="cancel()">\n    Done\n  </button>\n</div>\n\n<style>\n  .CodeMirror-merge-copy {\n    display: none;\n  }\n  .CodeMirror-merge, .CodeMirror-merge .CodeMirror {\n    height: 55vh;\n  }\n  .state-diff-modal .modal-dialog {\n    max-width: 1200px;\n    width: 90%;\n  }\n  .state-diff-modal .modal-body {\n    height: 60vh;\n  }\n</style>'

blocks = {}
debug_info = ''