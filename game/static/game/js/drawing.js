'use strict'

var ocargo = ocargo || {}

let GRID_WIDTH = 10
let GRID_HEIGHT = 8
var GRID_SPACE_SIZE = 100
let PAPER_WIDTH = GRID_SPACE_SIZE * GRID_WIDTH
let PAPER_HEIGHT = GRID_SPACE_SIZE * GRID_HEIGHT
let PAPER_PADDING = 30
let EXTENDED_PAPER_WIDTH = PAPER_WIDTH + 2 * PAPER_PADDING
let EXTENDED_PAPER_HEIGHT = PAPER_HEIGHT + 2 * PAPER_PADDING

let DEFAULT_CHARACTER_WIDTH = 40
let DEFAULT_CHARACTER_HEIGHT = 20

let COW_WIDTH = 80
let COW_HEIGHT = 80

let zoom = 15

let currentWidth = PAPER_WIDTH
let currentHeight = PAPER_HEIGHT
let currentStartX = 0
let currentStartY = 0

ocargo.Drawing = function (startingPosition) {
  /*************/
  /* Constants */
  /*************/

  let characterWidth =
    typeof CHARACTER_WIDTH !== 'undefined'
      ? CHARACTER_WIDTH
      : DEFAULT_CHARACTER_WIDTH
  let characterHeight =
    typeof CHARACTER_HEIGHT !== 'undefined'
      ? CHARACTER_HEIGHT
      : DEFAULT_CHARACTER_HEIGHT

  let TRAFFIC_LIGHT_WIDTH = 60
  let TRAFFIC_LIGHT_HEIGHT = 22

  let INITIAL_CFC_OFFSET_X = -105
  let INITIAL_CFC_OFFSET_Y = -7

  let DESTINATION_NOT_VISITED_COLOUR = 'red'
  let DESTINATION_VISITED_COLOUR = 'green'

  /*********/
  /* State */
  /*********/

  let paper = new Raphael('paper', EXTENDED_PAPER_WIDTH, EXTENDED_PAPER_HEIGHT)
  let roadImages = []

  let lightImages = {}
  let destinationImages = {}

  let character

  if (!ocargo.Drawing.inLevelEditor()) {
    character = new ocargo.Character(
      paper,
      CHARACTER_URL,
      WRECKAGE_URL,
      characterWidth,
      characterHeight,
      startingPosition,
      NIGHT_MODE
    )
  }

  paper.setViewBox(
    currentStartX,
    currentStartY,
    1000,
    800
  )

  /**
   * Zooming
   */
  function zoomMap (shouldZoomOut) {
    if (shouldZoomOut) {
      let newX = currentStartX - zoom
      let newY = currentStartY - zoom

      currentHeight = currentHeight + zoom * 2
      currentWidth = currentWidth + zoom * 2

      paper.setViewBox(newX, newY, currentWidth, currentHeight)

      currentStartX = newX
      currentStartY = newY
    }
    else {
      let newX = currentStartX + zoom
      let newY = currentStartY + zoom

      currentHeight = currentHeight - zoom * 2
      currentWidth = currentWidth - zoom * 2

      paper.setViewBox(newX, newY, currentWidth, currentHeight)

      currentStartX = newX
      currentStartY = newY
    }
  }

  $('#zoomIn').click(function () {
    zoomMap(false)
  })
  $('#zoomOut').click(function () {
    zoomMap(true)
  })

  /**
   * Map moving
   */
  let currentMousePos = { x: -1, y: -1 }

  let isMouseDown = false
  let prevX = 0
  let prevY = 0

  this.enablePanning = function () {
    let $paper = $('#paper')

    $paper.mousedown(function (event) {
      isMouseDown = true
    })

    $paper.mouseup(function (event) {
      isMouseDown = false
    })

    $paper.mousemove(function (event) {
      prevX = currentMousePos.x
      prevY = currentMousePos.y
      currentMousePos.x = event.pageX
      currentMousePos.y = event.pageY

      if (isMouseDown) {
        let deltaX = prevX - currentMousePos.x
        let deltaY = prevY - currentMousePos.y
        currentStartX = currentStartX + deltaX
        currentStartY = currentStartY + deltaY
        paper.setViewBox(
          currentStartX,
          currentStartY,
          currentWidth,
          currentHeight
        )
      }
    })
  }

  this.reset = function () {
    character.reset()
  }

  /*********************/
  /* Preloading images */
  /*********************/
  // Used by level editor to preload road tiles to prevent jittery drawing

  this.preloadRoadTiles = function () {
    let tiles = ['dead_end', 'crossroads', 'straight', 't_junction', 'turn']
    let tileImages = []
    let path = ocargo.Drawing.raphaelImageDir + 'road_tiles/'

    for (let i = 0; i < tiles.length; i++) {
      tileImages.push(
        paper.image(
          path + 'road/' + tiles[i] + '.svg',
          0,
          0,
          GRID_SPACE_SIZE,
          GRID_SPACE_SIZE
        )
      )
      tileImages.push(
        paper.image(
          path + 'path/' + tiles[i] + '.svg',
          0,
          0,
          GRID_SPACE_SIZE,
          GRID_SPACE_SIZE
        )
      )
    }

    for (let i = 0; i < tileImages.length; i++) {
      tileImages[i].remove()
    }
  }

  function calculateCFCInitialPosition (startNode) {
    let coord = ocargo.Drawing.translate(startNode.coordinate)
    return {
      x: coord.x * GRID_SPACE_SIZE + INITIAL_CFC_OFFSET_X + PAPER_PADDING,
      y: coord.y * GRID_SPACE_SIZE + INITIAL_CFC_OFFSET_Y + PAPER_PADDING
    }
  }

  function calculateInitialRotation (previousNode, startNode) {
    let nodeAngleRadians = ocargo.calculateNodeAngle(previousNode, startNode)
    let nodeAngleDegrees = nodeAngleRadians * (180 / Math.PI)
    return -nodeAngleDegrees // Calculation is counterclockwise, transformations are clockwise
  }

  // Return a pair of letters which represent the orientation of the turn
  // Directions are relative to the centre point of the turn
  // E.g. an L-shape turn will be described as 'UR'
  // D: Down, U: Up, L: Left, R:Right
  function getRoadLetters (previous, node1, node2) {
    previous = ocargo.Drawing.translate(previous)
    node1 = ocargo.Drawing.translate(node1)
    node2 = ocargo.Drawing.translate(node2)

    if (
      isHorizontal(node1, node2) &&
      (previous === null || isHorizontal(previous, node1))
    ) {
      return 'H'
    } else if (
      isVertical(node1, node2) &&
      (previous === null || isVertical(previous, node1))
    ) {
      return 'V'
      // Handle turns.
    } else {
      if (isProgressive(previous.x, node1.x)) {
        return nextPointAbove(node1, node2) ? 'DL' : 'UL'
      }
      if (isProgressive(node1.x, previous.x)) {
        return nextPointAbove(node1, node2) ? 'DR' : 'UR'
      }
      if (isProgressive(previous.y, node1.y)) {
        return nextPointFurther(node1, node2) ? 'UR' : 'UL'
      }
      if (isProgressive(node1.y, previous.y)) {
        return nextPointFurther(node1, node2) ? 'DR' : 'DL'
      }
    }
  }

  function isHorizontal (prev, next) {
    return prev.y === next.y
  }

  function isVertical (prev, next) {
    return prev.x === next.x
  }

  function nextPointAbove (curr, next) {
    return curr.y < next.y
  }

  function nextPointFurther (curr, next) {
    return curr.x < next.x
  }

  function isProgressive (coord1, coord2) {
    return coord1 < coord2
  }

  // Returns the direction of the middle branch
  // E.g. T-shaped junction will be described as 'down'
  function tJunctionOrientation (middle, node1, node2, node3) {
    let res1 = getRoadLetters(node1, middle, node2)
    let res2 = getRoadLetters(node2, middle, node3)

    if (res1 === 'H' && res2 === 'DR') {
      return 'down'
    } else if (res1 === 'UR' && res2 === 'DR') {
      return 'right'
    } else if (res1 === 'UL' && res2 === 'V') {
      return 'left'
    } else {
      return 'up'
    }
  }
  /***************/
  /** Rendering **/
  /***************/

  this.renderDestinations = function (destinations) {
    for (let i = 0; i < destinations.length; i++) {
      let destination = destinations[i].node
      let variation = getDestinationPosition(destination)

      let destinationRect = paper
        .rect(
          destination.coordinate.x * GRID_SPACE_SIZE + PAPER_PADDING,
          PAPER_HEIGHT -
            destination.coordinate.y * GRID_SPACE_SIZE -
            100 +
            PAPER_PADDING,
          100,
          100
        )
        .attr({ stroke: DESTINATION_NOT_VISITED_COLOUR })

      let destinationHouse = paper
        .image(
          ocargo.Drawing.raphaelImageDir + HOUSE_URL,
          destination.coordinate.x * GRID_SPACE_SIZE +
            variation[0] +
            PAPER_PADDING,
          PAPER_HEIGHT -
            destination.coordinate.y * GRID_SPACE_SIZE -
            variation[1] +
            PAPER_PADDING,
          50,
          50
        )
        .transform('r' + variation[2])

      destinationImages[destinations[i].id] = {
        rect: destinationRect,
        house: destinationHouse
      }
    }

    //find a side of the road
    function getDestinationPosition (destination) {
      let roadLetters = []

      //might be best to just use the coordinates rather than get road letters and then convert back to directions
      if (destination.connectedNodes.length === 1) {
        let previousNode = destination.connectedNodes[0]
        let nextNode = {}
        nextNode.coordinate = new ocargo.Coordinate(
          destination.coordinate.x +
            (destination.coordinate.x - previousNode.coordinate.x),
          destination.coordinate.y +
            (destination.coordinate.y - previousNode.coordinate.y)
        )
        roadLetters.push(
          getRoadLetters(
            previousNode.coordinate,
            destination.coordinate,
            nextNode.coordinate
          )
        )
      } else {
        for (let i = 0; i < destination.connectedNodes.length; i++) {
          let previousNode = destination.connectedNodes[i]
          for (let j = i + 1; j < destination.connectedNodes.length; j++) {
            roadLetters.push(
              getRoadLetters(
                previousNode.coordinate,
                destination.coordinate,
                destination.connectedNodes[j].coordinate
              )
            )
          }
        }
      }
      let left = true
      let right = true
      let up = true
      let down = true

      //variation specifies x,y,rotation
      let variation = [25, 25, 90]

      // Set "default" variations of the house position
      // based on straight roads and turns
      if (roadLetters.indexOf('H') >= 0) {
        left = false
        right = false
        variation = [25, 25, 90]
      }
      if (roadLetters.indexOf('V') >= 0) {
        up = false
        down = false
        variation = [-25, 75, 180]
      }
      if (roadLetters.indexOf('UL') >= 0) {
        left = false
        up = false
        variation = [45, 55, 45]
      }
      if (roadLetters.indexOf('DL') >= 0) {
        left = false
        down = false
        variation = [45, 95, 315]
      }
      if (roadLetters.indexOf('UR') >= 0) {
        right = false
        up = false
        variation = [5, 55, 135]
      }
      if (roadLetters.indexOf('DR') >= 0) {
        right = false
        down = false
        variation = [5, 95, 225]
      }

      // Adapt for T-junctions and crossroads
      if (!(left || right || up || down)) {
        // 4-way junction, so hang it off to the bottom left
        variation = [-25, 25, 135]
      } else if (!(up || left || right)) {
        // T junction, road at bottom
        variation = [25, 25, 90]
      } else if (!(down || left || right)) {
        // T junction, road at top
        variation = [25, 125, 270]
      } else if (!(up || down || left)) {
        // T junction, road at right
        variation = [75, 75, 0]
      } else if (!(up || down || right)) {
        // T junction, road at left
        variation = [-25, 75, 180]
      }

      return variation
    }
  }

  this.renderOrigin = function (position) {
    let initialPosition = calculateCFCInitialPosition(position.currentNode)
    let cfc = paper.image(
      ocargo.Drawing.raphaelImageDir + CFC_URL,
      initialPosition.x,
      initialPosition.y,
      100,
      107
    )
    let rotation = calculateInitialRotation(
      position.previousNode,
      position.currentNode
    )
    let transformation = ocargo.Drawing.rotationTransformationAroundCentreOfGridSpace(
      rotation,
      position.currentNode.coordinate.x,
      position.currentNode.coordinate.y
    )
    cfc.transform(transformation)
    cfc.transform('... r90')
  }

  this.renderRoad = function (nodes) {
    for (let i = 0; i < roadImages.length; i++) {
      let image = roadImages[i]
      if (image) {
        image.remove()
      }
    }

    let path = ocargo.Drawing.raphaelImageDir + 'road_tiles/'

    path += CHARACTER_NAME === 'Van' ? 'road/' : 'path/'

    roadImages = []
    for (let i = 0; i < nodes.length; i++) {
      let node = nodes[i]
      let roadImage
      switch (node.connectedNodes.length) {
        case 1:
          roadImage = drawDeadEndRoad(node, path)
          break

        case 2:
          roadImage = drawSingleRoadSegment(
            node.connectedNodes[0],
            node,
            node.connectedNodes[1],
            path
          )
          break

        case 3:
          roadImage = drawTJunction(node, path)
          break

        case 4:
          roadImage = drawCrossRoads(node, path)
          break

        default:
          break
      }
      roadImages.push(roadImage)
    }

    function drawDeadEndRoad (node, path) {
      let previousNode = node.connectedNodes[0]

      let nextNode = {}
      nextNode.coordinate = new ocargo.Coordinate(
        node.coordinate.x + (node.coordinate.x - previousNode.coordinate.x),
        node.coordinate.y + (node.coordinate.y - previousNode.coordinate.y)
      )

      let roadLetters = getRoadLetters(
        previousNode.coordinate,
        node.coordinate,
        nextNode.coordinate
      )

      let prevFlipped = ocargo.Drawing.translate(previousNode.coordinate)
      let flipped = ocargo.Drawing.translate(node.coordinate)

      let road = paper.image(
        path + 'dead_end.svg',
        flipped.x * GRID_SPACE_SIZE + PAPER_PADDING,
        flipped.y * GRID_SPACE_SIZE + PAPER_PADDING,
        GRID_SPACE_SIZE,
        GRID_SPACE_SIZE
      )

      if (roadLetters === 'H' && prevFlipped.x < flipped.x) {
        road.rotate(
          90,
          flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING,
          flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING
        )
      } else if (roadLetters === 'H' && prevFlipped.x > flipped.x) {
        road.rotate(
          270,
          flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING,
          flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING
        )
      } else if (roadLetters === 'V' && prevFlipped.y < flipped.y) {
        road.rotate(
          180,
          flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING,
          flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING
        )
      }

      return road
    }

    function drawSingleRoadSegment (previousNode, node, nextNode, path) {
      let roadLetters = getRoadLetters(
        previousNode.coordinate,
        node.coordinate,
        nextNode.coordinate
      )

      let flipped = ocargo.Drawing.translate(node.coordinate)
      let roadSrc =
        path +
        (roadLetters === 'H' || roadLetters === 'V' ? 'straight' : 'turn') +
        '.svg'
      let road = paper.image(
        roadSrc,
        flipped.x * GRID_SPACE_SIZE + PAPER_PADDING,
        flipped.y * GRID_SPACE_SIZE + PAPER_PADDING,
        GRID_SPACE_SIZE,
        GRID_SPACE_SIZE
      )

      if (roadLetters === 'H') {
        road.rotate(90)
      } else if (roadLetters === 'UL') {
        road.rotate(
          90,
          flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING,
          flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING
        )
      } else if (roadLetters === 'UR') {
        road.rotate(
          180,
          flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING,
          flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING
        )
      } else if (roadLetters === 'DR') {
        road.rotate(
          270,
          flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING,
          flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING
        )
      }

      return road
    }

    function drawTJunction (node, path) {
      let node1 = node.connectedNodes[0]
      let node2 = node.connectedNodes[1]
      let node3 = node.connectedNodes[2]

      let flipped = ocargo.Drawing.translate(node.coordinate)

      let letters12 = getRoadLetters(
        node1.coordinate,
        node.coordinate,
        node3.coordinate
      )
      let letters13 = getRoadLetters(
        node1.coordinate,
        node.coordinate,
        node2.coordinate
      )

      let rotation = 0
      if (
        (letters12 === 'V' && (letters13 === 'UL' || letters13 === 'DL')) ||
        (letters12 === 'UL' && (letters13 === 'DL' || letters13 === 'V')) ||
        (letters12 === 'DL' && (letters13 === 'UL' || letters13 === 'V'))
      ) {
        rotation = 0
      } else if (
        (letters12 === 'H' && (letters13 === 'UL' || letters13 === 'UR')) ||
        (letters12 === 'UL' && (letters13 === 'UR' || letters13 === 'H')) ||
        (letters12 === 'UR' && (letters13 === 'UL' || letters13 === 'H'))
      ) {
        rotation = 90
      } else if (
        (letters12 === 'V' && (letters13 === 'UR' || letters13 === 'DR')) ||
        (letters12 === 'UR' && (letters13 === 'DR' || letters13 === 'V')) ||
        (letters12 === 'DR' && (letters13 === 'UR' || letters13 === 'V'))
      ) {
        rotation = 180
      } else if (
        (letters12 === 'H' && (letters13 === 'DL' || letters13 === 'DR')) ||
        (letters12 === 'DL' && (letters13 === 'DR' || letters13 === 'H')) ||
        (letters12 === 'DR' && (letters13 === 'DL' || letters13 === 'H'))
      ) {
        rotation = 270
      }

      let road = paper.image(
        path + 't_junction.svg',
        flipped.x * GRID_SPACE_SIZE + PAPER_PADDING,
        flipped.y * GRID_SPACE_SIZE + PAPER_PADDING,
        GRID_SPACE_SIZE,
        GRID_SPACE_SIZE
      )
      road.rotate(
        rotation,
        flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING,
        flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING
      )

      return road
    }

    function drawCrossRoads (node, path) {
      let flipped = ocargo.Drawing.translate(node.coordinate)

      return paper.image(
        path + 'crossroads.svg',
        flipped.x * GRID_SPACE_SIZE + PAPER_PADDING,
        flipped.y * GRID_SPACE_SIZE + PAPER_PADDING,
        GRID_SPACE_SIZE,
        GRID_SPACE_SIZE
      )
    }
  }

  this.renderBackground = function () {
    if (!ocargo.Drawing.isMobile()) {
      paper.rect(0, 0, EXTENDED_PAPER_WIDTH, EXTENDED_PAPER_HEIGHT).attr({
        fill: 'url(' + ocargo.Drawing.raphaelImageDir + BACKGROUND_URL + ')',
        stroke: 'none'
      })
    }
  }

  this.renderDecor = function (decors) {
    for (let i = 0; i < decors.length; i++) {
      let decor = decors[i]
      let src = ocargo.Drawing.raphaelImageDir + decor.url
      let x = decor.x + PAPER_PADDING
      let y = PAPER_HEIGHT - decor.y - decor.height + PAPER_PADDING
      let width = decor.width
      let height = decor.height
      paper.image(src, x, y, width, height)
    }
  }

  this.createTrafficLightImage = function (url) {
    return paper.image(url, 0, 0, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT)
  }

  this.setTrafficLightImagePosition = function (
    sourceCoordinate,
    controlledCoordinate,
    image
  ) {
    // get position based on nodes
    let x = (controlledCoordinate.x + sourceCoordinate.x) / 2.0
    let y = (controlledCoordinate.y + sourceCoordinate.y) / 2.0

    // get rotation based on nodes (should face source)
    let angle = sourceCoordinate.angleTo(controlledCoordinate) * (180 / Math.PI)
    let rotation = 90 - angle

    // draw red and green lights, keep reference to both
    let drawX = x * GRID_SPACE_SIZE + TRAFFIC_LIGHT_HEIGHT + PAPER_PADDING
    let drawY =
      PAPER_HEIGHT - y * GRID_SPACE_SIZE - TRAFFIC_LIGHT_WIDTH + PAPER_PADDING

    image.transform('t' + drawX + ',' + drawY + ' r' + rotation + 's-1,1')
  }

  this.renderTrafficLights = function (trafficLights) {
    for (let i = 0; i < trafficLights.length; i++) {
      let trafficLight = trafficLights[i]
      let sourceCoordinate = trafficLight.sourceNode.coordinate
      let controlledCoordinate = trafficLight.controlledNode.coordinate

      trafficLight.greenLightEl = this.createTrafficLightImage(
        ocargo.Drawing.raphaelImageDir + 'trafficLight_green.svg'
      )
      trafficLight.redLightEl = this.createTrafficLightImage(
        ocargo.Drawing.raphaelImageDir + 'trafficLight_red.svg'
      )
      trafficLight.greenLightEl.node.id = 'trafficLight_' + i + '_green'
      trafficLight.redLightEl.node.id = 'trafficLight_' + i + '_red'

      this.setTrafficLightImagePosition(
        sourceCoordinate,
        controlledCoordinate,
        trafficLight.greenLightEl
      )
      this.setTrafficLightImagePosition(
        sourceCoordinate,
        controlledCoordinate,
        trafficLight.redLightEl
      )

      // hide light which isn't the starting state
      if (trafficLight.startingState === ocargo.TrafficLight.RED) {
        trafficLight.greenLightEl.attr({ opacity: 0 })
      } else {
        trafficLight.redLightEl.attr({ opacity: 0 })
      }

      lightImages[trafficLight.id] = [
        trafficLight.greenLightEl,
        trafficLight.redLightEl
      ]
    }
  }

  this.determineCowOrientation = function (coordinate, node) {
    let x = coordinate.x
    let y = coordinate.y

    let xOffset = 0
    let yOffset = 0
    let rotation = 0

    if (node.connectedNodes.length === 1) {
      // Deadends
      let previousNode = node.connectedNodes[0]
      let nextNode = {}
      nextNode.coordinate = new ocargo.Coordinate(
        node.coordinate.x + (node.coordinate.x - previousNode.coordinate.x),
        node.coordinate.y + (node.coordinate.y - previousNode.coordinate.y)
      )

      let roadLetters = getRoadLetters(
        previousNode.coordinate,
        node.coordinate,
        nextNode.coordinate
      )

      if (roadLetters === 'V') {
        rotation = 90
      }
    } else if (node.connectedNodes.length === 2) {
      // Turns
      let previousNode = node.connectedNodes[0]
      let nextNode = node.connectedNodes[1]

      let roadLetters = getRoadLetters(
        previousNode.coordinate,
        node.coordinate,
        nextNode.coordinate
      )

      if (roadLetters === 'V') {
        rotation = 90
      } else if (roadLetters === 'UL') {
        xOffset = -0.15 * GRID_SPACE_SIZE
        yOffset = -0.15 * GRID_SPACE_SIZE
        rotation = -45
      } else if (roadLetters === 'UR') {
        xOffset = +0.15 * GRID_SPACE_SIZE
        yOffset = -0.15 * GRID_SPACE_SIZE
        rotation = 45
      } else if (roadLetters === 'DL') {
        xOffset = -0.15 * GRID_SPACE_SIZE
        yOffset = +0.15 * GRID_SPACE_SIZE
        rotation = -135
      } else if (roadLetters === 'DR') {
        xOffset = +0.15 * GRID_SPACE_SIZE
        yOffset = +0.15 * GRID_SPACE_SIZE
        rotation = 135
      }
    } else if (node.connectedNodes.length === 3) {
      // T-junctions
      let previousNode = node.connectedNodes[0]
      let nextNode = node.connectedNodes[1]
      let nextNextNode = node.connectedNodes[2]
      let res = tJunctionOrientation(
        node.coordinate,
        previousNode.coordinate,
        nextNode.coordinate,
        nextNextNode.coordinate
      )
      if (res === 'down') {
        rotation = 180
      } else if (res === 'right') {
        rotation = 90
      } else if (res === 'left') {
        rotation = -90
      } else if (res === 'top') {
      }
    }

    let drawX =
      (x + 0.5) * GRID_SPACE_SIZE - COW_WIDTH / 2 + xOffset + PAPER_PADDING
    let drawY =
      PAPER_HEIGHT -
      (y + 0.5) * GRID_SPACE_SIZE -
      COW_HEIGHT / 2 +
      yOffset +
      PAPER_PADDING

    return { drawX: drawX, drawY: drawY, rotation: rotation }
  }

  this.createCowImage = function (type) {
    return paper.image(
      ocargo.Drawing.raphaelImageDir + ocargo.Drawing.cowUrl(type),
      0,
      0,
      COW_WIDTH,
      COW_HEIGHT
    )
  }

  this.setCowImagePosition = function (coordinate, image, node) {
    let res = this.determineCowOrientation(coordinate, node)

    image.transform('t' + res.drawX + ',' + res.drawY + 'r' + res.rotation)
  }

  this.renderCow = function (id, coordinate, node, animationLength, type) {
    let res = this.determineCowOrientation(coordinate, node)
    let image = paper.image(
      ocargo.Drawing.raphaelImageDir + ocargo.Drawing.cowUrl(type),
      res.drawX,
      res.drawY,
      COW_WIDTH,
      COW_HEIGHT
    )
    let rot = 'r' + res.rotation
    image.transform(rot + 's0.1')
    image.animate({ transform: rot + 's1' }, animationLength, 'linear')

    return {
      coordinate: coordinate,
      image: image
    }
  }

  this.removeCow = function (cow, animationLength) {
    if (cow){
      cow.image.animate(
        { transform: 's0.01' },
        animationLength,
        'linear',
        function () {
          cow.image.remove()
        }
      )
    }
  }

  this.renderCharacter = function () {
    character.render()
  }

  this.createGrid = function () {
    let grid = []
    for (let i = 0; i < GRID_WIDTH; i++) {
      let row = []
      for (let j = 0; j < GRID_HEIGHT; j++) {
        let x = i * GRID_SPACE_SIZE + PAPER_PADDING
        let y = j * GRID_SPACE_SIZE + PAPER_PADDING

        row.push(paper.rect(x, y, GRID_SPACE_SIZE, GRID_SPACE_SIZE))
      }
      grid.push(row)
    }
    return grid
  }

  this.renderGrid = function (grid, currentTheme) {
    for (let i = 0; i < GRID_WIDTH; i++) {
      for (let j = 0; j < GRID_HEIGHT; j++) {
        grid[i][j].attr({
          stroke: currentTheme.border,
          fill: currentTheme.background,
          'fill-opacity': 1
        })
      }
    }
  }

  this.clearPaper = function () {
    paper.clear()
  }

  this.renderMap = function (map) {
    this.renderBackground()
    this.renderRoad(map.nodes)
  }

  this.createImage = function (url, x, y, width, height) {
    return paper.image(url, x, y, width, height)
  }

  /****************/
  /** Animations **/
  /****************/

  this.transitionTrafficLight = function (lightID, endState, animationLength) {
    if (endState === ocargo.TrafficLight.GREEN) {
      lightImages[lightID][0].animate(
        { opacity: 1 },
        animationLength / 2,
        'linear'
      )
      lightImages[lightID][1].animate({ opacity: 0 }, animationLength, 'linear')
    } else {
      lightImages[lightID][0].animate(
        { opacity: 0 },
        animationLength / 2,
        'linear'
      )
      lightImages[lightID][1].animate({ opacity: 1 }, animationLength, 'linear')
    }
  }

  this.transitionDestination = function (destinationID, visited, duration) {
    let destinationRect = destinationImages[destinationID].rect
    let colour = visited
      ? DESTINATION_VISITED_COLOUR
      : DESTINATION_NOT_VISITED_COLOUR

    destinationRect.animate({ stroke: colour }, duration, 'linear')
  }

  this.scrollToShowCharacter = function () {
    character.scrollToShow()
  }

  this.moveForward = function (callback, scalingFactor) {
    return character.moveForward(callback, scalingFactor)
  }

  this.turnLeft = function (callback, scalingFactor) {
    return character.turnLeft(callback, scalingFactor)
  }

  this.turnRight = function (callback, scalingFactor) {
    return character.turnRight(callback, scalingFactor)
  }

  this.turnAround = function (direction) {
    return character.turnAround(direction)
  }

  this.wait = function (duration, callback) {
    character.wait(duration, callback)
  }

  this.deliver = function (destinationId, duration) {
    this.transitionDestination(destinationId, true, duration)
  }

  this.collisionWithCow = function (
    previousNode,
    currentNode,
    attemptedAction
  ) {
    return character.collisionWithCow(
      previousNode,
      currentNode,
      attemptedAction
    )
  }

  this.crash = function (previousNode, currentNode, attemptedAction) {
    return character.crash(attemptedAction)
  }

  this.setCharacterManoeuvreDuration = function (speed) {
    character.setManoeuvreDuration(speed)
  }
}

/********************************/
/* Static methods and constants */
/********************************/

// Flips the y coordinate upside down to match the raphael coordinate system
ocargo.Drawing.translate = function (coordinate) {
  return new ocargo.Coordinate(coordinate.x, GRID_HEIGHT - 1 - coordinate.y)
}

/*
 This is the function that starts the pop-up.
 Buttons should be passed in separately to the function instead of concatenating
 to the message so as to keep the layout of the pop-up consistent.
 The following elements will be displayed vertically from top to bottom in this order:
 1. title (bolded)
 2. subtitle (same font size as title)
 3. message (smaller font size than title and subtitle)
 4. buttons (in one row)
 Mascot will be displayed on the right hand side of the popup
 */
ocargo.Drawing.startPopup = function (
  title,
  subtitle,
  message,
  mascot,
  buttons
) {
  $('#myModal-title').html(title)
  $('#myModal-lead').html(subtitle)
  $('#myModal-mainText').html(message)

  $('#modal-mascot').hide()
  $('#modal-mascot--brain').hide()

  if (mascot) {
    if (EPISODE === 9) {
      $('#modal-mascot--brain').show()
    }
    else {
      $('#modal-mascot').show()
    }
  }

  const youtubeVideo = $("iframe")
  if (youtubeVideo[0]) {
    $("#modal-mascot").hide()
  }
  // buttons are passed as html string..
  // hence this terribleness
  // check if we pass an array of buttons or just one button
  if (Array.isArray(buttons)) {
    const icons = [
      $("<span>").addClass("iconify icon").attr("data-icon", "mdi:chevron-left"),
      "NOT USED",
      $("<span>").addClass("iconify icon").attr("data-icon", "mdi:chevron-right"),
    ]

    const links = [
      PREV_LEVEL_URL,
      "",
      NEXT_LEVEL_URL,
    ]

    const regexID = /id=\"*\w+_\w+\"/
    // create a wrapper for the buttons that will be appended
    let buttonDiv = $("<div>").addClass("modal-buttons")
    for (let i = 0; i < buttons.length; i++) {
      // get id with regex by stripping the html content
      let currentID = buttons[i].match(regexID)[0].slice(3).replaceAll('"', '')

      let currentButton = $(buttons[i])
      let classToBeAdded = currentID === "play_button" ? "navigation_button_portal long_button rapid-router-welcome" : "navigation_button_portal_secondary long_button rapid-router-welcome button--icon"

      currentButton.removeClass().addClass(classToBeAdded)
      if (currentID != "play_button") {
        // adding links to buttons
        currentButton.append(icons[i])
        let currentLink = links[i] === "" ? "" : `window.location.replace('${links[i]}')`
        currentButton.attr("onclick", currentLink)
      }

      // first level shouldn't have prev_button
      // and last level shouldn't have next_button
      if (currentButton.attr("onclick")) buttonDiv.append(currentButton)
    }
    // append the whole div to the popup
    $("#modal-buttons").html(buttonDiv)
  }

  else if (buttons) {
    $('#modal-buttons').html(buttons)
  } else {
    $('#modal-buttons').html(
      ocargo.button.dismissButtonHtml('close_button', gettext('Close'))
    )
  }
  // Show popup
  $("#myModal").show()
  $("#ocargo-modal").show()
  window.location.hash = 'myModal'
}

// This is the function that starts the pop-up with a yes and a no button
ocargo.Drawing.startYesNoPopup = function (
  title,
  subtitle,
  message,
  yesFunction,
  noFunction,
  mascot
) {
  let buttonHtml =
    '<button id="modal-yesBtn" class="navigation_button long_button">Yes</button> <button id="modal-noBtn" class="navigation_button long_button">No</button>'
  ocargo.Drawing.startPopup(title, subtitle, message, mascot, buttonHtml)
  $('#modal-yesBtn').click(yesFunction)
  $('#modal-noBtn').click(noFunction)
}

// This provides a pop-up with 2 options
ocargo.Drawing.startOptionsPopup = function (
  title,
  subtitle,
  message,
  optionAFunction,
  optionBFunction,
  optionAText,
  optionBText,
  mascot
) {
  let buttonHtml =
    '<button id="modal-optionABtn" class="navigation_button long_button">' + optionAText + '</button> <button id="modal-optionBBtn" class="navigation_button long_button">' + optionBText + '</button>'
  ocargo.Drawing.startPopup(title, subtitle, message, mascot, buttonHtml)
  $('#modal-optionABtn').click(optionAFunction)
  $('#modal-optionBBtn').click(optionBFunction)
}

// This is the function that starts the pop-up when there is no internet connection while playing the game
ocargo.Drawing.startInternetDownPopup = function () {
  ocargo.Drawing.startPopup(
    gettext('Error'),
    '',
    gettext(
      'Could not connect to server. Your internet might not be working properly.'
    )
  )
}

ocargo.Drawing.isMobile = function () {
  let mobileDetect = new MobileDetect(window.navigator.userAgent)
  return !!mobileDetect.mobile()
}

ocargo.Drawing.isChrome = function () {
  return navigator.userAgent.indexOf('Chrome') > -1
}

ocargo.Drawing.renderCoins = function (coins) {
  let html = '<div>'
  let i
  for (i = 0; i < coins.whole; i++) {
    html +=
      "<img src='" +
      ocargo.Drawing.imageDir +
      "coins/coin_gold.svg' width='50'>"
  }
  if (coins.half) {
    html +=
      "<img src='" +
      ocargo.Drawing.imageDir +
      "coins/coin_5050_dots.svg' width='50'>"
  }
  for (i = 0; i < coins.zero; i++) {
    html +=
      "<img src='" +
      ocargo.Drawing.imageDir +
      "coins/coin_empty_dots.svg' width='50'>"
  }

  return html
}

ocargo.Drawing.cowUrl = function (type) {
  switch (type) {
    case ocargo.Cow.WHITE:
      return ocargo.Drawing.whiteCowUrl
    case ocargo.Cow.BROWN:
      return ocargo.Drawing.brownCowUrl
    default:
      return ocargo.Drawing.whiteCowUrl
  }
}

ocargo.Drawing.createAbsoluteRotationTransformation = function (
  degrees,
  rotationPointX,
  rotationPointY
) {
  let transformation = '... R' + degrees
  if (rotationPointX !== undefined && rotationPointY !== undefined) {
    transformation += ',' + rotationPointX
    transformation += ',' + rotationPointY
  }
  return transformation
}

ocargo.Drawing.rotationTransformationAroundCentreOfGridSpace = function (
  degrees,
  x,
  y
) {
  let rotationPointX = (x + 1 / 2) * GRID_SPACE_SIZE + PAPER_PADDING
  let rotationPointY =
    (GRID_HEIGHT - (y + 1 / 2)) * GRID_SPACE_SIZE + PAPER_PADDING //flipping y
  let result = ocargo.Drawing.createAbsoluteRotationTransformation(
    degrees,
    rotationPointX,
    rotationPointY
  )
  return result
}

ocargo.Drawing.inLevelEditor = function () {
  return typeof CHARACTER_URL === 'undefined'
}

ocargo.Drawing.FRONT_VIEW = 'front_view'
ocargo.Drawing.TOP_VIEW = 'top_view'

ocargo.Drawing.whiteCowUrl = 'Clarice.svg'
ocargo.Drawing.brownCowUrl = 'Clarice_Jersey.svg'

ocargo.Drawing.imageDir = '/static/game/image/'
ocargo.Drawing.raphaelImageDir = '/static/game/raphael_image/'
