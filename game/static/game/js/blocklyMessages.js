/*global Blockly:true*/

// Logic Blocks.
Blockly.Msg.CONTROLS_IF_TOOLTIP_1 = gettext('If a value is true, then do some statements.');
Blockly.Msg.CONTROLS_IF_TOOLTIP_2 = gettext('If a value is true, then do the first block of statements. Otherwise, do the second block of statements.');
Blockly.Msg.CONTROLS_IF_TOOLTIP_3 = gettext('If the first value is true, then do the first block of statements. Otherwise, if the second value is true, do the second block of statements.');
Blockly.Msg.CONTROLS_IF_TOOLTIP_4 = gettext('If the first value is true, then do the first block of statements. Otherwise, if the second value is true, do the second block of statements. If none of the values are true, do the last block of statements.');
Blockly.Msg.CONTROLS_IF_MSG_IF = gettext('if');
Blockly.Msg.CONTROLS_IF_MSG_ELSEIF = gettext('else if');
Blockly.Msg.CONTROLS_IF_MSG_ELSE = gettext('else');
Blockly.Msg.CONTROLS_IF_MSG_THEN = gettext('do');

// Loop Blocks.
Blockly.Msg.CONTROLS_REPEAT_TITLE = interpolate(gettext('repeat %(number_of_times)s times'), {number_of_times: '%1'}, true);
Blockly.Msg.CONTROLS_REPEAT_INPUT_DO = gettext('do');
Blockly.Msg.CONTROLS_REPEAT_TOOLTIP = gettext('Do some statements several times.');
