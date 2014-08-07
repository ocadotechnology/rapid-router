'use strict';

var ocargo = ocargo || {};

ocargo.GameMenu = function() {
	this.BUTTON_HEIGHT = 50;
	this.GROUP_SPACING = 20;

	this.playBtn = $('play');
    this.pauseBtn = $('pause');
    this.resumeBtn = $('resume');
    this.stopBtn = $('stop');
    this.resetBtn = $('reset');
    this.stepBtn = $('step');

    this.loadBtn = $('load');
    this.saveBtn = $('save');
    this.clearBtn = $('clear');
    
    this.bigCodeModeBtn = $('big_code_mode');
    this.toggleConsoleBtn = $('toggle_console');
    
    this.helpBtn = $('help');
    this.muteBtn = $('mute');
    this.unmuteBtn = $('mute');
    this.quitBtn = $('quit');

    var group1 = [[this.playBtn, this.pauseBtn, this.resumeBtn],  [this.stopBtn,  this.resetBtn], [this.stepBtn]];
    var group2 = [[this.loadBtn], [this.saveBtn], [this.clearBtn]];
    var group3 = [[this.bigCodeModeBtn], [this.toggleConsoleBtn]];
    var group4 = [[this.helpBtn], [this.muteBtn, this.unmuteBtn], [this.quitBtn]];

    this.buttons = [group1, group2, group3, group4];
}


ocargo.GameMenu.pnrototype.displayMenu = function() {
	
}


ocargo.GameMenu.prototype.compileButtonHelp = function(name) {

}