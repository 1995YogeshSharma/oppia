from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/tests/form_builder_test_page.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/tests/form_builder_test_page.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div class="container" ng-controller="FormBuilderTests">\n    <h3>Test page for object editors</h3>\n\n    <h4>Editors sharing a common value</h4>\n    <table class="table">\n      <tr>\n        <th>Form name</th>\n        <th>Read-only version</th>\n        <th>Preview version</th>\n        <th>Editable version</th>\n      </tr>\n      <tr>\n        <td class="col-sm-3 col-md-3 col-lg-3">\n          <h5>Unicode form (copy 1)</h5>\n          <em>Saved value:</em> <[unicodeForm.value]>\n        </td>\n        <td class="col-sm-3 col-md-3 col-lg-3">\n          <schema-based-viewer schema="unicodeForm.schema" local-value="unicodeForm.value">\n          </schema-based-viewer>\n        </td>\n        <td class="col-sm-3 col-md-3 col-lg-3">\n          <form-overlay definition="unicodeForm.schema" saved-value="unicodeForm.value" is-disabled="true">\n          </form-overlay>\n        </td>\n        <td class="col-sm-3 col-md-3 col-lg-3">\n          <form-overlay definition="unicodeForm.schema" saved-value="unicodeForm.value">\n          </form-overlay>\n        </td>\n      </tr>\n      <tr>\n        <td class="col-sm-3 col-md-3 col-lg-3">\n          <h5>Unicode form (copy 2)</h5>\n          <em>Saved value:</em> <[unicodeForm.value]>\n        <td class="col-sm-3 col-md-3 col-lg-3">\n          <schema-based-viewer schema="unicodeForm.schema" local-value="unicodeForm.value">\n          </schema-based-viewer>\n        </td>\n        <td class="col-sm-3 col-md-3 col-lg-3">\n          <form-overlay definition="unicodeForm.schema" saved-value="unicodeForm.value" is-disabled="true">\n          </form-overlay>\n        </td>\n        <td class="col-sm-3 col-md-3 col-lg-3">\n          <form-overlay definition="unicodeForm.schema" saved-value="unicodeForm.value">\n          </form-overlay>\n        </td>\n      </tr>\n    </table>\n\n    <div ng-repeat="formset in formsets">\n      <h4><[formset.name]></h4>\n      <table class="table">\n        <tr>\n          <th>Form name</th>\n          <th>Read-only version</th>\n          <th>Preview version</th>\n          <th>Editable version</th>\n        </tr>\n        <tr ng-repeat="form in formset.forms">\n          <td class="col-sm-3 col-md-3 col-lg-3">\n            <h5><[form.name]></h5>\n            <div>\n              <em>Saved value:</em>\n              <div style="max-width: 300px; word-wrap: break-word;">\n                <[form.value]>\n              </span>\n            </div>\n          </td>\n          <td class="col-sm-3 col-md-3 col-lg-3">\n            <schema-based-viewer schema="form.schema" local-value="form.value">\n            </schema-based-viewer>\n          </td>\n          <td class="col-sm-3 col-md-3 col-lg-3">\n            <form-overlay definition="form.schema" saved-value="form.value" is-disabled="true">\n            </form-overlay>\n          </td>\n          <td class="col-sm-3 col-md-3 col-lg-3">\n            <form-overlay definition="form.schema" saved-value="form.value">\n            </form-overlay>\n          </td>\n        </tr>\n      </table>\n    </div>\n  </div>\n\n'

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    l_0_TEMPLATE_DIR_PREFIX = resolve('TEMPLATE_DIR_PREFIX')
    pass
    yield u'\n  <script src="/third_party/static/code-mirror-3.19.0/lib/codemirror.js"></script>\n  <script src="/third_party/static/code-mirror-3.19.0/mode/python/python.js"></script>\n  <script src="/third_party/static/ui-codemirror-0.1.2/src/ui-codemirror.js"></script>\n  %s\n  <script src="%s/components/forms/FormBuilder.js"></script>\n  <script src="%s/filters.js"></script>\n  <script src="%s/pages/tests/FormBuilderTestPage.js"></script>\n\n  <script src="%s/components/forms/schema_editors/SchemaBasedBoolEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_editors/SchemaBasedChoicesEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_editors/SchemaBasedCustomEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_editors/SchemaBasedDictEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_editors/SchemaBasedEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_editors/SchemaBasedExpressionEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_editors/SchemaBasedFloatEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_editors/SchemaBasedHtmlEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_editors/SchemaBasedIntEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_editors/SchemaBasedListEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_editors/SchemaBasedUnicodeEditorDirective.js"></script>\n  <script src="%s/components/forms/schema_viewers/SchemaBasedCustomViewerDirective.js"></script>\n  <script src="%s/components/forms/schema_viewers/SchemaBasedDictViewerDirective.js"></script>\n  <script src="%s/components/forms/schema_viewers/SchemaBasedHtmlViewerDirective.js"></script>\n  <script src="%s/components/forms/schema_viewers/SchemaBasedListViewerDirective.js"></script>\n  <script src="%s/components/forms/schema_viewers/SchemaBasedPrimitiveViewerDirective.js"></script>\n  <script src="%s/components/forms/schema_viewers/SchemaBasedUnicodeViewerDirective.js"></script>\n  <script src="%s/components/forms/schema_viewers/SchemaBasedViewerDirective.js"></script>\n\n' % (
        escape(context.call(l_0_super)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
    )

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Tests for the Form Builder - Oppia\n'

def block_header_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('header_js', block_header_js)
    pass
    yield u"\n  <script>\n    GLOBALS.ADDITIONAL_ANGULAR_MODULES = ['ui.codemirror'];\n  </script>\n  %s\n" % (
        escape(context.call(l_0_super)), 
    )

blocks = {'content': block_content, 'footer_js': block_footer_js, 'maintitle': block_maintitle, 'header_js': block_header_js}
debug_info = '1=11&14=17&101=24&105=32&106=33&107=34&108=35&110=36&111=37&112=38&113=39&114=40&115=41&116=42&117=43&118=44&119=45&120=46&121=47&122=48&123=49&124=50&125=51&126=52&127=53&3=56&7=63&11=70'