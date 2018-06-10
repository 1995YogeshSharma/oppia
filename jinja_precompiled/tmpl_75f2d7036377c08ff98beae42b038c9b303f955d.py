from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/preferences/edit_profile_picture_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3 translate="I18N_PREFERENCES_PROFILE_PICTURE_UPLOAD"></h3>\n</div>\n\n<div class="modal-body" style="min-height: 300px;">\n  <div class="oppia-profile-image-uploader">\n    <div ng-hide="uploadedImage">\n      <image-uploader on-file-changed="onFileChanged">\n      </image-uploader>\n    </div>\n\n    <div class="oppia-form-error" ng-if="invalidImageWarningIsShown" style="margin-top: 15px;" translate="I18N_PREFERENCES_PROFILE_PICTURE_ERROR"></div>\n\n    <div ng-show="uploadedImage">\n      <span translate="I18N_PREFERENCES_PROFILE_PICTURE_DRAG"></span>\n      <div class="oppia-profile-picture-crop-area" ng-show="uploadedImage">\n        <button class="btn btn-default oppia-profile-picture-reset-button" ng-click="reset()">\n          <i class="material-icons oppia-vcenter">&#xE14C;</i>\n        </button>\n        <img-crop image="uploadedImage" result-image="croppedImageDataUrl"\n                  area-type="square" result-image-size="150"\n                  on-load-error="onInvalidImageLoaded()"\n                  result-image-format="image/png">\n        </img-crop>\n      </div>\n    </div>\n  </div>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()" translate="I18N_PREFERENCES_CANCEL_BUTTON"></button>\n  <!--\n    The two checks for ng-disabled are necessary. The former is needed because\n    img-crop loads a default white image even when nothing is uploaded. The latter\n    is needed to prevent the saving of invalid files.\n  -->\n  <button class="btn btn-success" ng-click="confirm()" ng-disabled="!uploadedImage || !croppedImageDataUrl" translate="I18N_PREFERENCES_PROFILE_PICTURE_ADD"></button>\n</div>'

blocks = {}
debug_info = ''