from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/creator_dashboard/upload_activity_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Upload an Exploration</h3>\n</div>\n\n<div class="modal-body">\n  <p>\n    This form allows you to upload the YAML file corresponding to an exploration. However, you will need to manually upload any additional image files separately.\n  </p>\n\n  <br>\n  <br>\n\n  <p>\n    <form role="form" class="form-horizontal">\n      <fieldset>\n        <div class="form-group">\n          <label for="newFileInput" class="col-lg-2 col-md-2 col-sm-2">\n            Upload YAML file\n          </label>\n          <div class="col-lg-10 col-md-10 col-sm-10">\n            <input id="newFileInput" type="file">\n          </div>\n        </div>\n      </fieldset>\n    </form>\n  </p>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default protractor-test-cancel-create" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success protractor-test-submit-new-exploration" type="submit"\n          ng-click="save()">\n    Upload Exploration\n  </button>\n</div>'

blocks = {}
debug_info = ''