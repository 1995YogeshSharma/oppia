from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/share/sharing_links_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<ul class="oppia-sharing-links" layout="<[layoutType]>" layout-align="<[layoutAlignType]>">\n  <li>\n    <a ng-href="https://plus.google.com/share?url=<[serverName]>/<[activityType]>/<[activityId]>" onclick="return !window.open(this.href, \'\', \'height=600, width=600, menubar=no, toolbar=no, resizable=yes, scrollbars=yes\')" ng-click="registerShareEvent(\'gplus\')" target="_window">\n      <i class="oppia-share-icons fa fa-google-plus-square"></i>\n      <span class="oppia-icon-accessibility-label">Google+</span>\n    </a>\n  </li>\n\n  <li>\n    <a ng-href="https://www.facebook.com/sharer/sharer.php?sdk=joey&u=<[serverName]>/<[activityType]>/<[activityId]>&display=popup&ref=plugin&src=share_button" onclick="return !window.open(this.href, \'\', \'height=336, width=640\')" ng-click="registerShareEvent(\'facebook\')" target="_window">\n      <i class="oppia-share-icons fa fa-facebook-square"></i>\n      <span class="oppia-icon-accessibility-label">Facebook</span>\n    </a>\n  </li>\n\n  <li>\n    <a ng-href="https://twitter.com/share?text=<[escapedTwitterText]>&url=<[serverName]>/<[activityType]>/<[activityId]>" onclick="return !window.open(this.href, \'\', \'height=460, width=640\')" ng-click="registerShareEvent(\'twitter\')" target="_window">\n      <i class="oppia-share-icons fa fa-twitter-square"></i>\n      <span class="oppia-icon-accessibility-label">Twitter</span>\n    </a>\n  </li>\n\n  <li>\n    <a ng-href="https://classroom.google.com/share?url=<[serverName]>/<[activityType]>/<[activityId]>" onclick="return !window.open(this.href, \'\', \'height=460, width=640\')" ng-click="registerShareEvent(\'classroom\')" target="_window">\n      <img class="share-option-img" ng-src="<[classroomUrl]>" alt="Classroom">\n    </a>\n  </li>\n\n  <li ng-if="shareType === \'exploration\'">\n    <a href="" ng-click="showEmbedExplorationModal(explorationId)" tabindex="0">\n      <i class="material-icons md-48 embed-link">&#xE86F;</i>\n      <span class="oppia-icon-accessibility-label">Embed this Exploration</span>\n    </a>\n  </li>\n</ul>\n\n<style>\n  .oppia-sharing-links .embed-link {\n    color: white;\n    background: #009688;\n    border-radius: 6px;\n    height: 34px;\n    margin: 3px;\n    padding-top: -webkit-calc(50% - 15px);\n    padding-top: -moz-calc(50% - 15px);\n    padding-top: -o-calc(50% - 15px);\n    padding-top: calc(50% - 15px);\n    text-align: center;\n    width: 34px;\n}\n\n  .oppia-sharing-links .share-option-img {\n    border-radius: 5px;\n    height: 34px;\n    margin: 0 3px;\n    width: 34px;\n}\n\n  .oppia-sharing-links a:focus .share-option-img,\n  .oppia-sharing-links a:focus .embed-link {\n    outline: 1px dotted #212121;\n    outline: auto 5px -webkit-focus-ring-color;\n  }\n\n  ul.oppia-sharing-links {\n    list-style: none;\n    padding-top: 15px;\n  }\n\n  ul.oppia-sharing-links i.oppia-share-icons {\n    font-size:  40px;\n    padding: 0 5px;\n  }\n\n  i.oppia-share-icons.fa.fa-google-plus-square {\n    color: #dd4b39;\n  }\n\n  i.oppia-share-icons.fa.fa-facebook-square {\n    color: #3b5998;\n  }\n\n  i.oppia-share-icons.fa.fa-twitter-square {\n    color: #1da1f2;\n  }\n\n  i.oppia-share-icons.fa.fa-chalkboard-teacher {\n    color: #50a15f;\n  }\n\n</style>'

blocks = {}
debug_info = ''