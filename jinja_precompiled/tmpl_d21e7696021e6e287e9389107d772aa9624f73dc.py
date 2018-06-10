from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/collection_editor/settings_tab/collection_permissions_card_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<md-card class="oppia-page-card oppia-long-text" ng-if="hasPageLoaded()">\n  <h2>Collection Permissions</h2>\n  <div class="row">\n    <div class="col-lg-5 col-md-5 col-sm-5">\n      <h3>Managers</h3>\n      <ul>\n        <li ng-repeat="ownerName in collectionRights.getOwnerNames() track by $index">\n          <[ownerName]>\n        </li>\n      </ul>\n    </div>\n\n    <div class="col-lg-7 col-md-7 col-sm-7">\n      <h3>Permissions</h3>\n      <div ng-if="collectionRights.isPrivate()">\n        This collection is <strong>private</strong>.\n        <br>\n        <br>\n        It is <strong>not shown</strong> in the Oppia library.\n      </div>\n      <div ng-if="collectionRights.isPublic()">\n        This collection is <strong>public</strong>: anyone can access it.\n        <br>\n        <br>\n        It is <strong>available</strong> in the Oppia library.\n      </div>\n    </div>\n  </div>\n</md-card>'

blocks = {}
debug_info = ''