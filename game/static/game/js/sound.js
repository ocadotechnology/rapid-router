/*
Code for Life

Copyright (C) 2015, Ocado Innovation Limited

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

ADDITIONAL TERMS – Section 7 GNU General Public Licence

This licence does not grant any right, title or interest in any “Ocado” logos,
trade names or the trademark “Ocado” or any other trademarks or domain names
owned by Ocado Innovation Limited or the Ocado group of companies or any other
distinctive brand features of “Ocado” as may be secured from time to time. You
must not distribute any modification of this program using the trademark
“Ocado” or claim any affiliation or association with Ocado or its employees.

You are not authorised to use the name Ocado (or any of its trade names) or
the names of any author or contributor in advertising or for publicity purposes
pertaining to the distribution of this program, without the prior written
authorisation of Ocado.

Any propagation, distribution or conveyance of this program must include this
copyright notice and these terms. You must not misrepresent the origins of this
program; modified versions of the program must be marked as such and not
identified as the original program.
*/
var ocargo = ocargo || {};

ocargo.sound = {};

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
    if (CHARACTER_NAME === 'Van') {
        safePlay(ocargo.sound.startingSound);
    }
};

ocargo.sound.start_engine = function() {
    if (CHARACTER_NAME === 'Van') {
        safePlay(ocargo.sound.engineSound);
    }
};

ocargo.sound.stop_engine = function() {
    if (CHARACTER_NAME === 'Van') {
        safeStop(ocargo.sound.engineSound);
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

ocargo.sound.sound_horn = function() {
    safePlay(ocargo.sound.hornSound);
};

ocargo.sound.crash = function (animationDuration) {
    setTimeout(ocargo.sound._crashSound, animationDuration);
};

ocargo.sound.crashIntoCow = function (animationDuration) {
    ocargo.sound._crashSound();
};

ocargo.sound._crashSound = function () {
    if (CHARACTER_NAME === 'Van') {
        safePlay(ocargo.sound.crashSound);
    } else {
        safePlay(ocargo.sound.failureSound);
    }
};

ocargo.sound.tension = function() {
    safePlay(ocargo.sound.tensionSound);
};

ocargo.sound.mute = function() {
    this.playAudioBackup = Blockly.SOUNDS_;
    Blockly.SOUNDS_ = {};

    Howler.mute();
};

ocargo.sound.unmute = function() {
    Blockly.SOUNDS_ = this.playAudioBackup || Blockly.SOUNDS_;

    Howler.unmute();
};
