var ocargo = ocargo || {};

ocargo.sound = {};

// Stolen from: http://stackoverflow.com/questions/11330917/how-to-play-a-mp3-using-javascript
function Sound(source, initialVolume, loop) {
    // Create the audio tag
    this.soundFile = document.createElement("audio");
    this.soundFile.preload = "auto";

    // Load the sound file (using a source element for expandability)
    var src = document.createElement("source");
    src.src = source;
    this.soundFile.appendChild(src);
    this.soundFile.volume = initialVolume;

    this.play = function() {
        var self = this;
        setTimeout(function() {
            self.soundFile.pause();
            if (self.soundFile.duration) {
                self.soundFile.currentTime = 0;
            }
            self.soundFile.play();
        }, 1);
    };

    this.setVolume = function(volume) {
        this.soundFile.volume = volume;
    };
}

// *****

ocargo.sound.startingSound = new Sound("/static/game/sound/starting.mp3", 1.0, false);
ocargo.sound.movingSound = new Sound("/static/game/sound/moving.mp3", 1.0, false);
ocargo.sound.turningSound = new Sound("/static/game/sound/turning.mp3", 1.0, false);
ocargo.sound.winSound = new Sound("/static/game/sound/win.mp3", 1.0, false);
ocargo.sound.failureSound = new Sound("/static/game/sound/failure.mp3", 1.0, false);

ocargo.sound.starting = function() {
    // TODO: Reimplement when actual sounds exist
};

ocargo.sound.moving = function() {
    // TODO: Reimplement when actual sounds exist
};

ocargo.sound.turning = function() {
    // TODO: Reimplement when actual sounds exist
};

ocargo.sound.win = function() {
    // TODO: Reimplement when actual sounds exist
};

ocargo.sound.failure = function() {
    // TODO: Reimplement when actual sounds exist
};

ocargo.sound.setAllVolumes = function(volume, loop) {
    ocargo.sound.startingSound.setVolume(volume);
    ocargo.sound.movingSound.setVolume(volume);
    ocargo.sound.winSound.setVolume(volume);
    ocargo.sound.failureSound.setVolume(volume);
    ocargo.sound.turningSound.setVolume(volume);
};

ocargo.sound.mute = function() {
    ocargo.sound.playAudioBackup = Blockly.playAudio;
    Blockly.playAudio = function(name, options) {};
    ocargo.sound.volume = 0;
    ocargo.sound.setAllVolumes(0);
    $.cookie("muted", true);
};

ocargo.sound.unmute = function() {
    Blockly.playAudio = ocargo.sound.playAudioBackup;
    ocargo.sound.volume = 1;
    ocargo.sound.setAllVolumes(1.0);
    $.cookie("muted", false);
};
