from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/flag_exploration_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    <span><[\'I18N_PLAYER_REPORT_MODAL_HEADER\' | translate]></span>\n  </h3>\n</div>\n<div class="modal-body oppia-long-text">\n  <h4>\n    <span><b><[\'I18N_PLAYER_REPORT_MODAL_BODY_HEADER\' | translate]></b></span>\n  </h4>\n  <form>\n    <div class="radio">\n      <label>\n        <input type="radio" value="ad" ng-model="flag" ng-change="showFlagMessageTextarea(flag)">\n        <[\'I18N_PLAYER_REPORT_MODAL_BODY_AD\' | translate]>\n      </label>\n    </div>\n    <div class="radio">\n      <label>\n        <input type="radio" value="poor_experience" ng-model="flag" ng-change="showFlagMessageTextarea(flag)">\n        <[\'I18N_PLAYER_REPORT_MODAL_BODY_POOR_EXPERIENCE\' | translate]>\n      </label>\n    </div>\n    <div class="radio">\n      <label>\n        <input type="radio" value="other" ng-model="flag" ng-change="showFlagMessageTextarea(flag)">\n        <[\'I18N_PLAYER_REPORT_MODAL_BODY_OTHER\' | translate]>\n      </label>\n      <p ng-show="flagMessageTextareaIsShown">\n        <[\'I18N_PLAYER_REPORT_MODAL_BODY_ADDITIONAL_DETAILS\' | translate]>\n        <textarea rows="3" cols="50" ng-model="flagMessage" class="form-control" focus-on="flagMessageTextarea">\n        </textarea>\n      </p>\n    </div>\n  </form>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">\n    <[\'I18N_PLAYER_REPORT_MODAL_FOOTER_CANCEL\' | translate]>\n  </button>\n  <button class="btn btn-success" ng-click="submitReport()" ng-disabled="!flagMessage">\n    <[\'I18N_PLAYER_REPORT_MODAL_FOOTER_SUBMIT\' | translate]>\n  </button>\n</div>'

blocks = {}
debug_info = ''