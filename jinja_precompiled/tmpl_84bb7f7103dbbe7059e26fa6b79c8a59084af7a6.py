from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/customize_rte_component_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Customize This Component</h3>\n</div>\n\n<div class="modal-body">\n  <!-- Provide a sink to move the focus into while the modal loads. -->\n  <input ng-if="modalIsLoading" type="text" focus-on="tmpFocusPoint">\n  <form name="form.schemaForm">\n    <div ng-repeat="customizationArgSpec in customizationArgSpecs track by $index" style="margin-bottom: 25px;">\n      <strong><[customizationArgSpec.description]></strong>\n      <div style="margin-top: 15px;">\n        <schema-based-editor local-value="tmpCustomizationArgs[$index].value" schema="customizationArgSpec.schema">\n        </schema-based-editor>\n      </div>\n    </div>\n  </form>\n</div>\n\n<div class="modal-footer">\n  <input type="submit" class="btn btn-default" value="Cancel" ng-click="cancel()">\n  <input type="submit" class="btn btn-success protractor-test-close-rich-text-component-editor" value="Done" ng-click="save()" ng-disabled="form.schemaForm.$invalid">\n</div>'

blocks = {}
debug_info = ''