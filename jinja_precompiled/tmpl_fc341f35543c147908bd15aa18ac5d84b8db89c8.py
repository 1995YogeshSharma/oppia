from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/translation_tab/add_audio_translation_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Add Audio Translation</h3>\n</div>\n\n<div class="modal-body">\n  <div class="row">\n    <div class="col-lg-12 col-md-12 col-sm-12">\n      <div role="form" class="form-horizontal">\n        <div class="form-group">\n          <label for="audioTranslationFileField" class="col-lg-2 col-md-2 col-sm-2">Audio File</label>\n          <div class="col-lg-10 col-md-10 col-sm-10">\n            <audio-file-uploader id="audioTranslationFileField"\n                                 dropped-file="droppedFile"\n                                 on-file-changed="updateUploadedFile"\n                                 on-file-cleared="clearUploadedFile">\n            </audio-file-uploader>\n            <div ng-if="isAudioAvailable"\n                 class="oppia-updated-audio-file-upload-message">\n              <strong>Note:</strong> Uploading a new audio file will replace the existing audio file.\n            </div>\n            <div ng-if="errorMessage"\n                 class="oppia-audio-file-upload-field-error-message">\n              <i class="material-icons">&#xE002;</i>\n              <[errorMessage]>\n            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success" ng-click="save()" ng-disabled="!isAudioTranslationValid() || saveInProgress"><[saveButtonText]></button>\n</div>\n\n<style>\n  .oppia-audio-file-upload-field-error-message,\n  .oppia-updated-audio-file-upload-message {\n    color: red;\n    display: inline-block;\n    font-size: 14px;\n    padding: 4px;\n  }\n  .oppia-audio-file-upload-field-error-message i {\n    margin-right: 4px;\n  }\n</style>'

blocks = {}
debug_info = ''