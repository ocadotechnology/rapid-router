With the current structure of the code it is impossible to integrate python into it and have the same functionality, specifically it is because skulpt runs instantaneously and cannot be made to wait for animations to happen as blockly does. Therefore the only way to get it to work was to queue/buffer animations, what we're proposing to do is to extend this to all aspects of the view including van and traffic light animations, popups, code line highlighting and skulpt console printing. This will also make it easy to animate multiple vans at once.

The proposed design is one of model-view-controller, each part of which I will describe. For both python and blockly we will execute the entire program at once before any animation and send all of that off to the view. To implement stepping of either we will just step through the animations, although not actually stepping the code this will ideally be indistinguishable from it. To simulate multiple vans, their queues of animations will be merged before animating.

### Controller
Will be one of either blockly or python, and now both will operate in precisely the same way.
- Responsibilities:
  - Maintain a program that can be run (or optionally stepped), containing instructions that can either query the model about the state of the world, or change the model by giving an action for the van to perform, such as moving forwards.
  - Program executing should halt cleanly if it tries to perform an invalid action, such as driving off of the road or running out of fuel.
  - Program execution should be bounded, that is it must not be possible to get into an infinite loop which would break the browser. This is only really an issue for python and could be solved by limiting execution time to 2 seconds or so.
- Public interface:
  - RunProgram() - creates or resets a model and the program before running the program to completion, outputs a list of animations.

### Model
- Responsibilities:
  - Maintain a graph of the current road map.
  - Maintain location of the van and the state of things such as traffic lights.
    - This will require the model having knowledge of time, but it will only have one clock.
    - Because there is only one van, the state of traffic lights can be updated as the van moves much as it is now.
  - Can be queried by a controller about the state of the world and accepts commands to move a van. Commands take the form Model.methodName(action, callback) and respect the following conditions:
    - the callback will be called when the animation for that event starts to happen, the reasoning being that it could be used for line highlighting, console printing, etc...
    - the function must happen immediately, that is no timeouts or event are to be used, when the function returns all changes must have been made to the model and future function calls should reflect these changes.
  - Maintain a list of animations that the program executed so far has generated. Once the program terminates (for any reason) this list can be sent to the view for display.
    - When the van moves and time increments, calculate events for other things (eg: traffic lights) and add those events to the list
- Public interface:
  - makeObservation, performAction - these follow the methodName(action, callback) structure from above and may increment time
  - resetModel() - used by the controller before starting execution
  - signalEndOfProgram() - tells the model that all instructions have been executed, the model should now decide if the user has won or lose the game and add those events to the list before returning the list of events

### View
- Responsibilities:
  - Maintain some graphics, eg: roads, vans, popups, ..., which are moved around
  - Takes a list of visual events to process, each one linked to a timestamp, eg: animations, waiting, popups, winning/losing game, console logging
  - Maintain an animation clock that can be run or stepped:
    - events should be processed once the clock reaches their timestamp.
    - all animations for a timestamp should be performed in parallel.
    - the clock may be moved forward only one timestep at a time to implement stepping though a program
  - Make sure animations completely finish so graphics stay in sync, eg: vans don't drive off of the road, this is solved for raphael.
- Public interface:
  - initialise(level) - sets the initial map, the positions of the van and states of traffic lights, etc...
  - processEvents(events) - takes a list of events and prepares to process them, doesn't start any animation
  - resetAnimation() - sets the state back to how it was initialised
  - startAnimation() - resumes the animation from wherever it got to (either the start or where it was paused)
  - pauseAnimation() - stops animation but it can be resumed
  - stepAnimation() - if currently paused, performs only one step of animation and stops again