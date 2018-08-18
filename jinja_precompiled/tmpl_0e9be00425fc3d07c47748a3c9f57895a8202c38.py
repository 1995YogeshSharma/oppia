from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/PlayerConstants.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Contstans to be used in the learner view.\n */\n\noppia.constant(\'CONTENT_FOCUS_LABEL_PREFIX\', \'content-focus-label-\');\n\noppia.constant(\'TWO_CARD_THRESHOLD_PX\', 960);\n\noppia.constant(\'CONTINUE_BUTTON_FOCUS_LABEL\', \'continueButton\');\n\n/* New card is available but user hasn\'t gone to it yet (when oppia\n   gives a feedback and waits for user to press \'continue\').\n   Not called when a card is selected by clicking progress dots */\noppia.constant(\'EVENT_NEW_CARD_AVAILABLE\', \'newCardAvailable\');\n/* Called when the learner moves to a new card that they haven\'t seen before. */\noppia.constant(\'EVENT_NEW_CARD_OPENED\', \'newCardOpened\');\n/* Called always when learner moves to a new card.\n   Also called when card is selected by clicking on progress dots */\noppia.constant(\'EVENT_ACTIVE_CARD_CHANGED\', \'activeCardChanged\');\n\n/* Called when a new audio-equippable component is loaded and displayed\n   to the user, allowing for the automatic playing of audio if necessary. */\noppia.constant(\'EVENT_AUTOPLAY_AUDIO\', \'autoPlayAudio\');\n\n// The enforced waiting period before the first hint request.\noppia.constant(\'WAIT_FOR_FIRST_HINT_MSEC\', 60000);\n// The enforced waiting period before each of the subsequent hint requests.\noppia.constant(\'WAIT_FOR_SUBSEQUENT_HINTS_MSEC\', 30000);\n\n// The time delay between the learner clicking the hint button\n// and the appearance of the hint.\noppia.constant(\'DELAY_FOR_HINT_FEEDBACK_MSEC\', 100);\n\n// Array of i18n IDs for the possible hint request strings.\noppia.constant(\n  \'HINT_REQUEST_STRING_I18N_IDS\', [\n    \'I18N_PLAYER_HINT_REQUEST_STRING_1\',\n    \'I18N_PLAYER_HINT_REQUEST_STRING_2\',\n    \'I18N_PLAYER_HINT_REQUEST_STRING_3\']);\n\noppia.constant(\n  \'EXPLORATION_DATA_URL_TEMPLATE\',\n  \'/explorehandler/init/<exploration_id>\');\noppia.constant(\n  \'EXPLORATION_VERSION_DATA_URL_TEMPLATE\',\n  \'/explorehandler/init/<exploration_id>?v=<version>\');\noppia.constant(\n  \'EDITABLE_EXPLORATION_DATA_URL_TEMPLATE\',\n  \'/createhandler/data/<exploration_id>\');\noppia.constant(\n  \'EDITABLE_EXPLORATION_DATA_DRAFT_URL_TEMPLATE\',\n  \'/createhandler/data/<exploration_id>?apply_draft=<apply_draft>\');\noppia.constant(\n  \'TRANSLATE_EXPLORATION_DATA_URL_TEMPLATE\',\n  \'/createhandler/translate/<exploration_id>\');\n\n\noppia.constant(\'EVENT_PROGRESS_NAV_SUBMITTED\', \'progress-nav-submit\');\n\n/* This should match the CSS class defined in the tutor card directive. */\noppia.constant(\n  \'AUDIO_HIGHLIGHT_CSS_CLASS\', \'conversation-skin-audio-highlight\');'

blocks = {}
debug_info = ''