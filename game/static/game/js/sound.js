var ocargo = ocargo || {};

ocargo.sound = {};

function Sound(source, initialVolume, loop) {
    var audio = new Audio(source);
    audio.volume = initialVolume;

    audio.loop = loop;

    // A fallback, incase audio.loop doesn't work,
    // which apparently it doesn't in some browsers
    if (loop) {
        audio.onended = function() {
            audio.src = audio.src;
            audio.play();
        }
    }

    this.play = function() {
        if (audio.duration) {
            if (audio.ended) {
                audio.src = audio.src;
            }
            else {
                audio.currentTime = 0;
            }

            audio.play();
        }
    };

    this.pause = function() {
        audio.pause();
    }

    this.setVolume = function(volume) {
        audio.volume = volume;
    };
}

ocargo.sound.startingSound = new Sound("/static/game/sound/starting.mp3", 1.0, false);
ocargo.sound.engineSound = new Sound("/static/game/sound/moving.wav", 1.0, true);
ocargo.sound.deliverySound = new Sound("/static/game/sound/delivery.mp3", 1.0, false);
ocargo.sound.winSound = new Sound("/static/game/sound/win.mp3", 1.0, false);
ocargo.sound.failureSound = new Sound("/static/game/sound/failure.mp3", 1.0, false);
ocargo.sound.crashSound = new Sound("/static/game/sound/crash.mp3", 1.0, false);
ocargo.sound.tensionSound = new Sound("/static/game/sound/tension.mp3", 1.0, false);

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
    ocargo.sound.startingSound.setVolume(volume);
    ocargo.sound.movingSound.setVolume(volume);
    ocargo.sound.turningSound.setVolume(volume);
    ocargo.sound.winSound.setVolume(volume);
    ocargo.sound.failureSound.setVolume(volume);
    ocargo.sound.tensionSound.setVolume(volume);
};

ocargo.sound.mute = function() {
    this.playAudioBackup = Blockly.SOUNDS_;
    Blockly.SOUNDS_ = {};
    ocargo.sound.setAllVolumes(0);
    $.cookie("muted", true);
};

ocargo.sound.unmute = function() {
    Blockly.SOUNDS_ = this.playAudioBackup;
    ocargo.sound.setAllVolumes(1.0);
    $.cookie("muted", false);
};
