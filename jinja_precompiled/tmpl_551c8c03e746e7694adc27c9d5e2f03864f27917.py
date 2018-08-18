from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/story_editor/main_editor/story_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div role="form" class="form-horizontal">\n  <md-card class="oppia-page-card oppia-long-text">\n    <div class="story-title">\n      <span ng-if="!storyTitleEditorIsShown" ng-click="openStoryTitleEditor()"\n            class="oppia-editable-section">\n        <strong class="form-heading"><[story.getTitle()]></strong>\n        <i class="material-icons oppia-editor-edit-icon"\n           title="Edit Story Title">&#xE254;\n        </i>\n      </span>\n      <span ng-if="storyTitleEditorIsShown">\n        <form class="form-horizontal" role="form" ng-submit="updateStoryTitle(editableTitle)">\n          <input type="text" ng-model="editableTitle">\n          <button type="submit" class="btn btn-success btn-sm">Save</button>\n          <button class="btn btn-default btn-sm" ng-click="closeStoryTitleEditor()">Cancel</button>\n        </form>\n      </span>\n    </div>\n\n    <div class="story-description" ng-class="{\'has-error\': editableDescriptionIsEmpty && storyDescriptionChanged}">\n      <label for="storyDescription" class="form-heading">Description</label>\n      <textarea type="text" class="form-control"\n                ng-model="editableDescription"\n                ng-change="updateStoryDescriptionStatus(editableDescription)"\n                ng-blur="updateStoryDescription(editableDescription)"\n                placeholder="Enter the description of the story">\n      </textarea>\n      <span ng-if="editableDescriptionIsEmpty && storyDescriptionChanged" class="help-block" style="font-size: smaller">\n        What does this story contain?\n      </span>\n    </div>\n\n    <div class="story-notes">\n      <label for="storyNotes" class="form-heading">Notes</label>\n      <div ng-if="!notesEditorIsShown" class="preview">\n        <angular-html-bind html-data="notes">\n        </angular-html-bind>\n        <button type="button"\n                class="btn btn-default save-button"\n                ng-click="closePreviewNotes(notes)">\n          Edit\n        </button>\n      </div>\n      <div ng-if="notesEditorIsShown" class="oppia-editor-card-body">\n        <schema-based-editor schema="NOTES_SCHEMA"\n                             local-value="editableNotes">\n        </schema-based-editor>\n        <button type="button"\n                class="btn btn-default save-button"\n                ng-click="openPreviewNotes(editableNotes)">\n          Preview\n        </button>\n        <button type="button"\n                class="btn btn-success save-button"\n                ng-disabled="!editableNotes"\n                ng-click="updateNotes(editableNotes)">\n          Save\n        </button>\n      </div>\n    </div>\n    <div class="story-nodes-title">\n      <label for="storyNodes" class="form-heading">Story Nodes</label>\n      <br>\n      Click on the check box to mark it as initial node\n    </div>\n    <div class="story-node-editor">\n      <br>\n      <div class="story-nodes-container">\n        <div ng-repeat="node in nodes">\n          <md-card class="story-editor-node"\n                   ng-class="{\'selected-node\': (node.getId() === idOfNodeToEdit)}"\n                   ng-click="setNodeToEdit(node.getId())">\n            <div class="story-editor-node-title">\n              <[node.getId()]>\n            </div>\n            <span class="story-editor-initial-node">\n              <span ng-click="markAsInitialNode(node.getId())" aria-hidden="true">\n                <i ng-if="!isInitialNode(node.getId())" class="material-icons md-18">check_box_outline_blank</i>\n                <i ng-if="isInitialNode(node.getId())" class="material-icons md-18">check_box</i>\n              </span>\n            </span>\n            <span class="story-editor-delete-node">\n              <span ng-click="deleteNode(node.getId())" aria-hidden="true">\n                <i class="material-icons md-18">&#xE14C;</i>\n              </span>\n            </span>\n          </md-card>\n        </div>\n      </div>\n      <div class="node-editor">\n        <div ng-repeat="node in nodes">\n          <story-node-editor ng-if="node.getId() === idOfNodeToEdit"\n                             node-id="node.getId()"\n                             outline="node.getOutline()"\n                             exploration-id="node.getExplorationId()"\n                             outline-finalized="node.getOutlineStatus()"\n                             destination-node-ids="node.getDestinationNodeIds()">\n          </story-node-editor>\n        </div>\n      </div>\n    </div>\n  </md-card>\n</div>\n\n<style>\n  story-editor md-card {\n    margin-left: 10%;\n    margin-top: -1%;\n    width: 80%;\n  }\n\n  story-editor .story-editor-node {\n    background-color: #F5F5F5;\n    color: #424242;\n    display: inline-block;\n    font-family: "Capriola", "Roboto", Arial, sans-serif;\n    font-size: 0.8em;\n    margin: 0;\n    padding-top: 5px;\n    padding-bottom: 5px;\n    position: relative;\n    text-align: center;\n    width: 15vw;\n  }\n\n  story-editor .selected-node {\n    background-color: #d4d4d4;\n  }\n\n  story-editor .story-editor-delete-node {\n    color: #ef5350;\n    position: absolute;\n    right: 0;\n    top: 0;\n  }\n\n  story-editor .story-editor-initial-node {\n    position: absolute;\n    left: 0;\n    top: 0;\n  }\n\n  story-editor .story-editor-node-title {\n    color: blue;\n    padding: 16px 16px 20px 16px;\n  }\n\n  story-editor .story-nodes-container {\n    background-color: white;\n    border-right: 1px solid #BDBDBD;\n    display: inline-block;\n    float: left;\n    overflow-y: auto;\n    padding: 70px 20px;\n    position: relative;\n    text-align: center;\n    white-space: nowrap;\n    width: 35%;\n  }\n\n  story-editor .node-editor {\n    display: inline-block;\n    min-height: 25vh;\n    padding-left: 5%;\n    width: 65%;\n  }\n\n  story-editor .story-node-editor {\n    display: flex;\n  }\n\n  story-editor .form-heading {\n    font-size: 1.2em;\n  }\n\n  story-editor .story-title {\n    margin-bottom: 1.5%;\n  }\n\n  story-editor .story-notes {\n    margin-top: 1.5%;\n    height: auto;\n    margin-bottom: 2%;\n  }\n\n  story-editor .story-nodes-title {\n    margin-bottom: 2%;\n  }\n\n  story-editor .story-notes .save-button {\n    margin-top: 1.5vh;\n  }\n\n  story-editor .story-description textarea {\n    height: 10vh;\n  }\n</style>'

blocks = {}
debug_info = ''