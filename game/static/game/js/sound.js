var ocargo = ocargo || {};

ocargo.sound = {};

ocargo.sound.startingSound = new Howl({
    urls: ['/static/game/sound/starting.mp3', '/static/game/sound/starting.ogg']
});

ocargo.sound.electricVanStartingSound = new Howl({
    urls: ['/static/game/sound/electric_van_starting.mp3', '/static/game/electric_van_starting.ogg']
})

ocargo.sound.engineSound = new Howl({
    urls: ['/static/game/sound/moving.mp3', '/static/game/sound/moving.ogg'],
    loop: true
});

ocargo.sound.deliverySound = new Howl({
    urls: ['/static/game/sound/delivery.mp3', '/static/game/sound/delivery.ogg']
});

ocargo.sound.hornSound = new Howl({
    urls: ['/static/game/sound/horn.mp3', '/static/game/sound/horn.ogg']
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

ocargo.sound.cowSound = new Howl({
    urls: ['/static/game/sound/cow.mp3', '/static/game/sound/cow.ogg']
});

ocargo.sound.pigeonSound = new Howl({
    urls: ['/static/game/sound/pigeon.mp3', '/static/game/sound/pigeon.ogg']
});

/// festive sounds ///**
ocargo.sound.clownHornSound = new Howl({
    urls: ['/static/game/sound/clown_horn.mp3', '/static/game/sound/clown_horn.ogg']
});

ocargo.sound.sleighBellsSound = new Howl({
    urls: ['/static/game/sound/sleigh_bells.mp3', '/static/game/sound/sleigh_bells.ogg']
});

ocargo.sound.sleighCrashSound = new Howl({
    urls: ['/static/game/sound/sleigh_crash.mp3', '/static/game/sound/sleigh_crash.ogg']
});

function isDecember()
{
    const currentMonth = new Date().getMonth(); 
    return currentMonth === 11;
}

function safePlay(sound) {
    try {
        sound.play();
    }
    catch (err) {}
}

function safeStop(sound) {
    try {
        sound.stop();
    }
    catch (err) {}
}


ocargo.sound.starting = function() {
    if (!isDecember()) {
        if (CHARACTER_NAME === 'Van') {
            safePlay(ocargo.sound.startingSound);
        } else if (CHARACTER_NAME === "Electric van") {
            safePlay(ocargo.sound.electricVanStartingSound);
        }
    }
};

ocargo.sound.start_engine = function() {
    if (isDecember()) {
        safePlay(ocargo.sound.sleighBellsSound);
    } else if (CHARACTER_NAME === 'Van') {
        safePlay(ocargo.sound.engineSound);
    }
};

ocargo.sound.stop_engine = function() {
    if (CHARACTER_NAME === 'Van') {
        safeStop(ocargo.sound.engineSound);
    } else if (CHARACTER_NAME === "Electric van") {
        safeStop(ocargo.sound.electricVanStartingSound);
    }
};

ocargo.sound.delivery = function() {
    safePlay(ocargo.sound.deliverySound);
};

ocargo.sound.win = function() {
    safePlay(ocargo.sound.winSound);
};

ocargo.sound.failure = function() {
    safePlay(ocargo.sound.failureSound);
};

ocargo.sound.cow = function() {
    safePlay(ocargo.sound.cowSound);
};

ocargo.sound.pigeon = function() {
    safePlay(ocargo.sound.pigeonSound);
}

ocargo.sound.sound_horn = function() {
if (isDecember()) {
    safePlay(ocargo.sound.clownHornSound);
} else {
    safePlay(ocargo.sound.hornSound);
}
};

ocargo.sound.crash = function (animationDuration) {
    setTimeout(ocargo.sound._crashSound, animationDuration);
};

ocargo.sound.crashIntoCow = function (animationDuration) {
    ocargo.sound._crashSound();
};

ocargo.sound._crashSound = function () {
    if (isDecember()) {
        safePlay(ocargo.sound.sleighCrashSound);
    } else {
        if (CHARACTER_NAME === 'Van') {
            safePlay(ocargo.sound.crashSound);
    } else {
        safePlay(ocargo.sound.failureSound);
    }
}
};

ocargo.sound.tension = function() {
    safePlay(ocargo.sound.tensionSound);
};

ocargo.sound.mute = function() {
    this.playAudioBackup = Blockly.mainWorkspace.SOUNDS_;
    Blockly.mainWorkspace.SOUNDS_ = {};

    Howler.mute();
};

ocargo.sound.unmute = function() {
    Blockly.mainWorkspace.SOUNDS_ = this.playAudioBackup || Blockly.mainWorkspace.SOUNDS_;

    Howler.unmute();
};
