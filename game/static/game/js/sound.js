var ocargo = ocargo || {};

ocargo.sound = {};

ocargo.sound.allSounds = [];

ocargo.sound.startingSound = new Howl({
    urls: ['/static/game/sound/starting.mp3', '/static/game/sound/starting.ogg']
});

ocargo.sound.engineSound = new Howl({
    urls: ['/static/game/sound/moving.mp3', '/static/game/sound/moving.ogg'],
    loop: true
});

ocargo.sound.deliverySound = new Howl({
    urls: ['/static/game/sound/delivery.mp3', '/static/game/sound/delivery.ogg']
});

ocargo.sound.winSound = new Howl({
    urls: ['/static/game/sound/win.mp3', '/static/game/sound/win.ogg']
});

ocargo.sound.failureSound = new Howl({
    urls: ['/static/game/sound/failure.mp3', '/static/game/sound/failure.ogg']
});

ocargo.sound.crashSound = new Howl({
    urls: ['/static/game/sound/crash.mp3', '/static/game/sound/crash.ogg']
});

ocargo.sound.tensionSound = new Howl({
    urls: ['/static/game/sound/tension.mp3', '/static/game/sound/tension.ogg']
});

ocargo.sound.allSounds.push(ocargo.sound.startingSound);
ocargo.sound.allSounds.push(ocargo.sound.engineSound);
ocargo.sound.allSounds.push(ocargo.sound.deliverySound);
ocargo.sound.allSounds.push(ocargo.sound.winSound);
ocargo.sound.allSounds.push(ocargo.sound.failureSound);
ocargo.sound.allSounds.push(ocargo.sound.crashSound);
ocargo.sound.allSounds.push(ocargo.sound.tensionSound);

ocargo.sound.starting = function() {
    ocargo.sound.startingSound.play();
};

ocargo.sound.start_engine = function() {
    ocargo.sound.engineSound.play();
};

ocargo.sound.stop_engine = function() {
    ocargo.sound.engineSound.pause();
};

ocargo.sound.delivery = function() {
    ocargo.sound.deliverySound.play();
};

ocargo.sound.win = function() {
    ocargo.sound.winSound.play();
};

ocargo.sound.failure = function() {
    ocargo.sound.failureSound.play();
};

ocargo.sound.crash = function() {
    ocargo.sound.crashSound.play();
};

ocargo.sound.tension = function() {
    ocargo.sound.tensionSound.play();
};

ocargo.sound.setAllVolumes = function(volume) {
    for (var i in ocargo.sound.allSounds) {
        ocargo.sound.allSounds[i].volume(volume);
    }
};

ocargo.sound.mute = function() {
    this.playAudioBackup = Blockly.SOUNDS_;
    Blockly.SOUNDS_ = {};
    ocargo.sound.setAllVolumes(0);
};

ocargo.sound.unmute = function() {
    Blockly.SOUNDS_ = this.playAudioBackup;
    ocargo.sound.setAllVolumes(1.0);
};
