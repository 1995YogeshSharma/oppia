from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topic_editor/main_editor/new_story_title_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>\n    Enter Story Title\n  </h3>\n</div>\n<div class="modal-body new-story-title-editor" ng-class="{\'has-error\': isStoryTitleEmpty(storyTitle)}">\n  <p>\n    Enter the title for the story: &nbsp;\n    <input class="form-group" ng-model="storyTitle">\n    <span ng-if="isStoryTitleEmpty(storyTitle)" class="help-block" style="font-size: smaller">\n     A title is required to create a story.\n    </span>\n  </p>\n</div>\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success" ng-disabled="isStoryTitleEmpty(storyTitle)" ng-click="save(storyTitle)">\n    <span>Create Story</span>\n  </button>\n</div>\n<style>\n  .new-story-title-editor .help-block {\n    margin-left: 37.5%;\n    margin-top: -3%;\n  }\n</style>'

blocks = {}
debug_info = ''