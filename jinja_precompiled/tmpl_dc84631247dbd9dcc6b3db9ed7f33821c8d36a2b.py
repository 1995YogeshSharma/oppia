from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/admin/config_tab/admin_config_tab_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<md-card class="oppia-page-card oppia-long-text" style="max-width: 1050px">\n  <h3>Configuration properties</h3>\n  <div class="container" ng-if="isNonemptyObject(configProperties)" style="margin-left: 0;">\n    <div ng-repeat="(configPropertyId, configPropertyData) in configProperties">\n      <div class="row protractor-test-config-property" style="padding-bottom: 10px;">\n        <span class="col-lg-2 col-md-2 col-sm-2">\n          <em class="protractor-test-config-title"><[configPropertyData.description]></em>\n        </span>\n        <span class="col-lg-6 col-md-6 col-sm-6">\n          <schema-based-editor schema="configPropertyData.schema" local-value="configPropertyData.value">\n          </schema-based-editor>\n        </span>\n        <span class="col-lg-2 col-md-2 col-sm-2">\n          <button type="button" class="btn btn-default" ng-click="revertToDefaultConfigPropertyValue(configPropertyId)">\n            Revert to default\n          </button>\n        </span>\n      </div>\n    </div>\n\n    <button ng-click="saveConfigProperties()" class="protractor-test-save-all-configs">Save</button>\n    <button ng-click="reloadConfigProperties()">Undo changes</button>\n  </div>\n\n  <div ng-if="!isNonemptyObject(configProperties)">\n    No configuration properties are available.\n  </div>\n</md-card>'

blocks = {}
debug_info = ''