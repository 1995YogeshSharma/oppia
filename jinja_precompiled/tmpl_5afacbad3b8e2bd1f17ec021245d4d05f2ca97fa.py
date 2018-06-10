from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/audio_file_uploader_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div>\n  <form id="<[inputFieldFormId]>">\n    <input type="file" ng-class="inputFieldClassName">\n  </form>\n  <div class="license-warning">\n    Please only upload audio files that you created yourself and that you are willing to license under the site\'s\n    <a href="/about#license" target="_blank">license terms</a>.\n    Audio translation files should be less than <b>five minutes</b> long.\n  </div>\n\n  <div ng-if="errorMessage" class="error-message">\n    <i class="material-icons">&#xE002;</i>\n    <[errorMessage]>\n  </div>\n</div>\n\n<style>\n  audio-file-uploader .license-warning {\n    background-color: rgba(225, 250, 89, 0.41);\n    border: 1px solid rgba(200, 230, 59, 0.41);\n    border-radius: 6px;\n    font-size: 12px;\n    font-style: italic;\n    left: 8px;\n    margin-top: 6px;\n    text-align: left;\n    padding: 4px 6px;\n  }\n\n  audio-file-uploader .error-message {\n    color: red;\n    display: inline-block;\n    font-size: 14px;\n    padding: 4px;\n  }\n  audio-file-uploader .error-message i {\n    margin-right: 4px;\n  }\n</style>'

blocks = {}
debug_info = ''