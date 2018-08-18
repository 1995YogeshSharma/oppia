from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/image_uploader_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="image-uploader-drop-area">\n  <div class="image-uploader-text" translate="I18N_DIRECTIVES_DRAG_IMAGE_HERE"></div>\n  <span ng-if="errorMessage" class="image-uploader-error-message">\n    <i class="material-icons">&#xE002;</i>\n    <[errorMessage]>\n  </span>\n  <span class="image-uploader-license-warning">\n    Before uploading images, please ensure that they are<br>\n    compatible with the <a href="/about#license" target="_blank">license terms</a> of the site.<br>\n    Please do not upload watermarked images.\n  </span>\n  <label for="image-file-input" translate="I18N_DIRECTIVES_UPLOAD_A_FILE" class="image-uploader-upload-label-button"></label>\n  <input type="file" id="image-file-input" class="image-uploader-file-input" ng-class="fileInputClassName">\n</div>\n\n<style>\n  .image-uploader-license-warning {\n    background-color: rgba(225, 250, 89, 0.41);\n    border: 1px solid rgba(200, 230, 59, 0.41);\n    border-radius: 6px;\n    bottom: 8px;\n    font-size: 12px;\n    font-style: italic;\n    left: 8px;\n    position: absolute;\n    text-align: left;\n    padding: 4px 6px;\n  }\n\n  .image-uploader-drop-area {\n    background: #eee;\n    color: black;\n    font-size: 16px;\n    height: 200px;\n    text-align: center;\n    padding-top: 74px;\n    position: relative;\n    width: 100%;\n  }\n\n  .image-uploader-text {\n    display: block;\n    font-size: 16px;\n    line-height: 28px;\n    margin-bottom: 12px;\n    text-align: center;\n    width: 100%;\n  }\n\n  .image-uploader-is-active {\n    background-color: #bbb;\n  }\n\n  .image-uploader-file-input {\n    height: 0.1px;\n    opacity: 0;\n    overflow: hidden;\n    position: absolute;\n    width: 0.1px;\n    z-index: -1;\n  }\n\n  label.image-uploader-upload-label-button {\n    background: grey;\n    background-image: -webkit-gradient(linear, left top, left bottom, color-stop(0, #F2F2F2), color-stop(1, #BFBFBF));\n    background-image: -o-linear-gradient(bottom, #F2F2F2 0%, #BFBFBF 100%);\n    background-image: -moz-linear-gradient(bottom, #F2F2F2 0%, #BFBFBF 100%);\n    background-image: -webkit-linear-gradient(bottom, #F2F2F2 0%, #BFBFBF 100%);\n    background-image: -ms-linear-gradient(bottom, #F2F2F2 0%, #BFBFBF 100%);\n    background-image: linear-gradient(to bottom, #F2F2F2 0%, #BFBFBF 100%);\n    border: solid #707070 1px;\n    border-radius: 2px;\n    bottom: 6px;\n    cursor: default;\n    display: inline;\n    font-size: 16px;\n    font-weight: normal;\n    padding: 4px 8px;\n    position: absolute;\n    right: 8px;\n    text-align: center;\n  }\n\n  label.image-uploader-upload-label-button:hover {\n    background-image: -webkit-gradient(linear, left top, left bottom, color-stop(0, #EAF6FD), color-stop(1, #A7D8F5));\n    background-image: -o-linear-gradient(bottom, #EAF6FD 0%, #A7D8F5 100%);\n    background-image: -moz-linear-gradient(bottom, #EAF6FD 0%, #A7D8F5 100%);\n    background-image: -webkit-linear-gradient(bottom, #EAF6FD 0%, #A7D8F5 100%);\n    background-image: -ms-linear-gradient(bottom, #EAF6FD 0%, #A7D8F5 100%);\n    background-image: linear-gradient(to bottom, #EAF6FD 0%, #A7D8F5 100%);\n    border: #3c7fb1 solid 1px;\n    cursor: pointer;\n  }\n\n  label.image-uploader-upload-label-button:active {\n    background-image: -webkit-gradient(linear, left top, left bottom, color-stop(0, #E5F4FC), color-stop(0.5, #C4E5F6), color-stop(0.51, #98D0EF), color-stop(1, #68B3DB));\n    background-image: -o-linear-gradient(bottom, #E5F4FC 0%, #C4E5F6 50%, #98D0EF 51%, #68B3DB 100%);\n    background-image: -moz-linear-gradient(bottom, #E5F4FC 0%, #C4E5F6 50%, #98D0EF 51%, #68B3DB 100%);\n    background-image: -webkit-linear-gradient(bottom, #E5F4FC 0%, #C4E5F6 50%, #98D0EF 51%, #68B3DB 100%);\n    background-image: -ms-linear-gradient(bottom, #E5F4FC 0%, #C4E5F6 50%, #98D0EF 51%, #68B3DB 100%);\n    background-image: linear-gradient(to bottom, #E5F4FC 0%, #C4E5F6 50%, #98D0EF 51%, #68B3DB 100%);\n    border: solid #2c628b 1px;\n    padding: 4px 8px;\n  }\n\n  .image-uploader-error-message {\n    color: red;\n    display: inline-block;\n    font-size: 16;\n    padding: 4px;\n  }\n\n  .image-uploader-error-message i {\n    font-size: 16px;\n    margin-right: 4px;\n  }\n</style>'

blocks = {}
debug_info = ''