var ocargo = ocargo || {};

ocargo.sound = {}

// Stolen from: http://stackoverflow.com/questions/11330917/how-to-play-a-mp3-using-javascript

function Sound(source,volume,loop)
{
    this.source=source;
    this.volume=volume;
    this.loop=loop;
    var son;
    this.son=son;
    this.finish=false;

    this.stop=function()
    {
        if (this.son != null) {
            document.body.removeChild(this.son);
            this.son = null;
        }
    }
    this.create=function(autostart)
    {
        this.son=document.createElement("embed");
        this.son.setAttribute("src",this.source);
        this.son.setAttribute("hidden","true");
        this.son.setAttribute("volume",this.volume);
        this.son.setAttribute("autostart",autostart);
        this.son.setAttribute("loop",this.loop);
        document.body.appendChild(this.son);
    }
    this.start=function()
    {
        if(this.finish)return false;
        this.create("true");
    }
    this.remove=function()
    {
        if (this.son != null) {
            document.body.removeChild(this.son);
            this.son = null;
        }
        this.finish=true;
    }
    this.init=function(volume,loop)
    {
        this.finish=false;
        this.volume=volume;
        this.loop=loop;
    }
};

// *****

ocargo.sound.startingSound = new Sound("/static/game/sound/starting.mp3", 100, false);
ocargo.sound.movingSound = new Sound("/static/game/sound/turning.mp3", 100, false);
ocargo.sound.winSound = new Sound("/static/game/sound/win.mp3", 100, false);
ocargo.sound.failureSound = new Sound("/static/game/sound/failure.mp3", 100, false);
ocargo.sound.turningSound = new Sound("/static/game/sound/turning.mp3", 100, false);

ocargo.sound.stopAll = function() {
    ocargo.sound.movingSound.stop();
    ocargo.sound.winSound.stop();
    ocargo.sound.failureSound.stop();
    ocargo.sound.turningSound.stop();
};

ocargo.sound.starting = function() {
    ocargo.sound.stopAll();
    console.debug("Playing 'starting' sound.");
    ocargo.sound.startingSound.start();
};

ocargo.sound.moving = function() {
    ocargo.sound.stopAll();
    console.debug("Playing 'moving' sound.");
    ocargo.sound.movingSound.start();
};

ocargo.sound.turning = function() {
    ocargo.sound.stopAll();
    console.debug("Playing 'turning' sound.");
    ocargo.sound.turningSound.start();
};

ocargo.sound.win = function() {
    ocargo.sound.stopAll();
    console.debug("Playing 'win' sound.");
    ocargo.sound.winSound.start();
};

ocargo.sound.failure = function() {
    ocargo.sound.stopAll();
    console.debug("Playing 'failure' sound.");
    ocargo.sound.failureSound.start();
};

ocargo.sound.initialiseSounds = function(volume, loop) {
    ocargo.sound.volume = volume;
    ocargo.sound.startingSound.init(volume, loop);
    ocargo.sound.movingSound.init(volume,loop);
    ocargo.sound.winSound.init(volume, loop);
    ocargo.sound.failureSound.init(volume, loop);
    ocargo.sound.turningSound.init(volume, loop)
};
ocargo.sound.mute = function() {
    ocargo.sound.initialiseSounds(0, false);
};

ocargo.sound.unmute = function() {
    ocargo.sound.initialiseSounds(100, false);
};

