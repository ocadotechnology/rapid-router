'use strict';

function Level(map, van, destination, ui) {
    this.map = map;
    this.van = van;
    this.destination = destination;
    this.ui = ui;
}

Level.prototype.play = function(program){
	$.post('/game/submit', JSON.stringify(program.instructions));
	
    while(program.canStep()) {
        var instruction = program.step();
        console.debug('Calculating next node for instruction ' + instruction.name);
        var nextNode = instruction.getNextNode(this.van.previousNode, this.van.currentNode);

        if (nextNode === this.destination && !program.canStep()) {
            console.debug('You win!');
            break;
        } else if (!nextNode) {
            console.debug('Oh dear! :(');
            break;
        }

        this.van.move(nextNode, instruction);
    }
    
    this.ui.animateUpdates();
};
