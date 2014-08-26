var ocargo = ocargo || {};

ocargo.sound = {};

ocargo.sound.soundNodes = [];

$(function() {
    ocargo.sound.soundNodes.push(document.getElementById('startingSound'));
    ocargo.sound.soundNodes.push(document.getElementById('engineSound'));
    ocargo.sound.soundNodes.push(document.getElementById('deliverySound'));
    ocargo.sound.soundNodes.push(document.getElementById('winSound'));
    ocargo.sound.soundNodes.push(document.getElementById('failureSound'));
    ocargo.sound.soundNodes.push(document.getElementById('crashSound'));
    ocargo.sound.soundNodes.push(document.getElementById('tensionSound'));
    
    document.getElementById('engineSound').loop = true;
});

ocargo.sound.starting = function() {
    document.getElementById('startingSound').cloneNode(true).play();
};

ocargo.sound.start_engine = function() {
    document.getElementById('engineSound').play();
};

ocargo.sound.stop_engine = function() {
    document.getElementById('engineSound').pause();
};

ocargo.sound.delivery = function() {
    document.getElementById('deliverySound').cloneNode(true).play();
};

ocargo.sound.win = function() {
    document.getElementById('winSound').cloneNode(true).play();
};

ocargo.sound.failure = function() {
    document.getElementById('failureSound').cloneNode(true).play();
};

ocargo.sound.crash = function() {
    document.getElementById('crashSound').cloneNode(true).play();
};

ocargo.sound.tension = function() {
    document.getElementById('tensionSound').cloneNode(true).play();
};

ocargo.sound.setAllVolumes = function(volume) {
    for (var i in ocargo.sound.soundNodes) {
        ocargo.sound.soundNodes[i].volume = volume;
    }
};

ocargo.sound.mute = function() {
    this.playAudioBackup = Blockly.SOUNDS_;
    Blockly.SOUNDS_ = {};
    ocargo.sound.setAllVolumes(0);
    $.cookie("muted", 'true');
};

ocargo.sound.unmute = function() {
    Blockly.SOUNDS_ = this.playAudioBackup;
    ocargo.sound.setAllVolumes(1.0);
    $.cookie("muted", 'false');
};
