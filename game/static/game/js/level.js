'use strict';

function Level(map, van, destination, ui) {
    this.map = map;
    this.van = van;
    this.destination = destination;
    this.ui = ui;

    this.play = function(program){
        while(program.canStep()) {
            var instruction = program.step();
            console.debug('Calculating next node for instruction ' + instruction.name);
            var nextNode = instruction.getNextNode(this.van.previousNode, this.van.currentNode);
            
            if (nextNode === destination && !program.canStep()) {
                console.debug('You win!');
                break;
            } else if (!nextNode) {
                console.debug('Oh dear! :(');
                break;
            }

            // HACK for now, pass in instruction
            van.move(nextNode, instruction);
        }
        this.ui.animateUpdates();
    };
}