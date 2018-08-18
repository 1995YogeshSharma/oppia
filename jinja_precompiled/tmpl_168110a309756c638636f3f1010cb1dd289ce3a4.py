from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/statistics_tab/playthrough_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header d-flex text-center oppia-issues-issue-dir">\n  <h3 class="modal-title">Sample Playthrough</h3>\n</div>\n\n<div class="modal-body" style="padding-bottom: 8rem; margin-left:0.5rem; margin-right: 0.5rem;">\n  <div ng-if="maxHidden != 0" class="row oppia-pt2">\n    <button type="button" name="button" ng-click="showRemainingActions(playthroughIndex)" class="oppia-issues-btn-arrow" id="arrowDiv" style="display: block;"><i class="fa fa-arrow-up"></i></button>\n  </div>\n  <div class="row oppia-pt2" style="margin-top: 0.5rem;">\n    <div ng-repeat="displayBlock in reversedDisplayBlocks" style="text-align: left; margin-left: 0.2rem;">\n      <div ng-if="!isDisplayBlockOnInitDisplay(displayBlock)" ng-bind-html="renderBlockHtml(displayBlock, createDisplayBlockNavId(displayBlock))" id="remainingActions<[playthroughIndex]><[getDisplayBlockIndex(displayBlock)]>" style="display: none;"></div>\n    </div>\n    <div ng-if="isDisplayBlockOnInitDisplay(displayBlocks[0])" ng-bind-html="renderBlockHtml(displayBlocks[0], 1)" class="oppia-issues-highlight"></div>\n  </div>\n</div>\n\n<div class="modal-footer">\n  <button type="button" class="oppia-issues-bg-clr oppia-issues-text-white oppia-ft-14 btn oppia-issues-btn-resolve" ng-click="cancel()">\n    Return to Playthroughs\n  </button>\n</div>'

blocks = {}
debug_info = ''