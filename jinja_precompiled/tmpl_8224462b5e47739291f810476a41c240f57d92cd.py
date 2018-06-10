from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/creator_dashboard/create_activity_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-create-activity-modal">\n  <div class="modal-body oppia-long-text protractor-test-creation-modal">\n    <div class="row">\n      <div class="col-sm-12">\n        <h1 translate="I18N_CREATE_ACTIVITY_TITLE"></h1>\n        <p translate="I18N_CREATE_ACTIVITY_QUESTION"></p>\n      </div>\n\n      <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 text-center">\n        <img ng-src="<[explorationImgUrl]>" ng-click="chooseExploration()">\n        <button type="button" ng-click="chooseExploration()"\n                class="btn oppia-transition-200 protractor-test-create-exploration">\n          <span translate="I18N_CREATE_EXPLORATION"></span>\n        </button>\n      </div>\n\n      <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12 text-center" ng-if="canCreateCollections">\n        <img ng-src="<[collectionImgUrl]>" ng-click="chooseCollection()">\n        <button type="button" ng-click="chooseCollection()"\n                class="btn oppia-transition-200 protractor-test-create-collection">\n          <span translate="I18N_CREATE_COLLECTION"></span>\n        </button>\n      </div>\n    </div>\n  </div>\n</div>\n\n<style>\n  .oppia-create-activity-modal .modal-body {\n    font-family: "Capriola", "Roboto", Arial, sans-serif;\n    height: 100%;\n    margin: 0 auto;\n    top: 7%;\n    width: 95%;\n  }\n\n  .oppia-create-activity-modal h1 {\n    color: #015c53;\n  }\n\n  .oppia-create-activity-modal p {\n    font-size: 0.9em;\n    margin-top: 0;\n    margin-bottom: 6px;\n  }\n\n  .oppia-create-activity-modal button {\n    background-color: #015c53;\n    border-radius: 0;\n    color: #fff;\n    font-family: "Capriola", "Roboto", Arial, sans-serif;\n    font-size: 14px;\n    margin-top: 10px;\n    text-transform: uppercase;\n    width: 100%;\n    text-align: center;\n  }\n\n  .oppia-create-activity-modal button:hover,\n  .oppia-create-activity-modal button:focus,\n  .oppia-create-activity-modal button:active {\n    background-color: rgba(5, 190, 178, 1);\n    color: #fff;\n  }\n\n  .oppia-create-activity-modal img {\n    width: 100%;\n    max-height: 300px;\n    padding-top: 10px;\n  }\n\n  @media (max-width: 770px) {\n    .oppia-create-activity-modal .modal-body {\n      top: 5%;\n    }\n  }\n</style>'

blocks = {}
debug_info = ''