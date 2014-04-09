'use strict';

function Level(map, van, destination) {
    this.map = map;
    this.van = van;
    this.destination = destination;

    this.play = function(program){
        while(program.canStep()){
            var instruction = program.step();
            var nextNode = instruction.getNextNode(this.van.previousNode, this.van.currentNode);
            van.move(nextNode);
        }
    };
}