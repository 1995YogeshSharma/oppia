from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/help_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-body oppia-long-text">\n  <div class="oppia-help-modal-header-container">\n    <h1>Need Help?</h1>\n  </div>\n  <p>\n    Check out the resources in our help center or\n    take a tour of the exploration editor.\n  </p>\n  <a href="https://oppia.github.io/#/" target="_blank" class="btn oppia-help-modal-button oppia-help-dismiss" ng-click="goToHelpCenter()">Visit the Help Center</a>\n  <button class="btn oppia-help-modal-button" ng-click="beginTutorial()">Take the Tour</button>\n</div>\n<style>\n  .oppia-help-modal-header-container {\n    text-align: center;\n  }\n\n  .oppia-help-modal .modal-body {\n    height: 100%;\n    margin: 5% auto;\n    width: 90%;\n  }\n\n  .oppia-help-modal .modal-content {\n    border-radius: 0;\n    height: 100%;\n  }\n\n  .oppia-help-modal .modal-dialog {\n    height: 330px;\n  }\n\n  .oppia-help-modal .oppia-help-modal-button {\n    background-color: #015c53;\n    border-radius: 0;\n    color: #fff;\n    font-family: "Capriola", "Roboto", Arial, sans-serif;\n    font-size: 14px;\n    margin-top: 10px;\n    margin-right: 10px;\n    text-transform: uppercase;\n    width: 220px;\n  }\n  .oppia-help-modal .oppia-help-modal-button:hover,\n  .oppia-help-modal .oppia-help-modal-button:focus,\n  .oppia-help-modal .oppia-help-modal-button:active {\n    background-color: rgba(5, 190, 178, 1);\n    color: #fff;\n  }\n\n  @media (max-width: 760px) {\n    .oppia-help-modal .modal-dialog {\n      margin: 10% auto;\n      width: 80%;\n    }\n  }\n\n  @media (max-width: 550px) {\n    .oppia-help-dismiss {\n      margin-bottom: 1em;\n    }\n\n    .oppia-help-modal .oppia-help-modal-button {\n      width: 100%;\n    }\n  }\n</style>'

blocks = {}
debug_info = ''