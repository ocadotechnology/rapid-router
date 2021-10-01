describe("getOptimalPath", function() {
  /*
   * a b
   * c d
   */
  var a = new ocargo.Node(new ocargo.Coordinate(1, 1));
  var b = new ocargo.Node(new ocargo.Coordinate(1, 2));
  var c = new ocargo.Node(new ocargo.Coordinate(2, 1));
  var d = new ocargo.Node(new ocargo.Coordinate(2, 2));

  it("finds the optimal path along a super simple graph", function() {
    a.addConnectedNodeWithBacklink(b);
    var path = getOptimalPath([a, b], [new ocargo.Destination(0, b)]);

    expect(path).toEqual([a, b]);
  });

  it("finds the optimal path along a little more complicated graph", function() {
    a.addConnectedNodeWithBacklink(b);
    a.addConnectedNodeWithBacklink(c);
    c.addConnectedNodeWithBacklink(d);
    b.addConnectedNodeWithBacklink(d);
    var path = getOptimalPath([a, b, c, d], [new ocargo.Destination(0, b)]);

    expect(path).toEqual([a, b]);
  });

  /*it("finds the optimal path along a 3x3 graph", function() {
    nodes = [];
    for (var y = 0; y < 3; y++)
      for (var x = 0; x < 3; x++) {
        nodes.push(new ocargo.Node(new ocargo.Coordinate(x, y)));
      }

    for (var x = 0; x < 2; x++) {
      nodes[x].addConnectedNodeWithBacklink(nodes[x + 1]);
      nodes[x + 3].addConnectedNodeWithBacklink(nodes[x + 4]);
      nodes[x + 6].addConnectedNodeWithBacklink(nodes[x + 7]);
    }

    for (var y = 0; y < 6; y = y * 3) {
      nodes[y].addConnectedNodeWithBacklink(nodes[y + 3]);
      nodes[y + 1].addConnectedNodeWithBacklink(nodes[y + 4]);
      nodes[y + 2].addConnectedNodeWithBacklink(nodes[y + 5]);
    }

    destinations = []
    for (var i = 1; i < 9; i++) {
      destinations.push(new ocargo.Destination(i, nodes[i]));
    }

    var path = getOptimalPath(nodes, destinations);

    expect(path).toEqual(destinations);
  });*/
});

describe("aStar", function() {
  /*
   * a-b
   * |
   * c-d                                 e
   */
  var a = new ocargo.Node(new ocargo.Coordinate(1, 1));
  var b = new ocargo.Node(new ocargo.Coordinate(1, 2));
  var c = new ocargo.Node(new ocargo.Coordinate(2, 1));
  var d = new ocargo.Node(new ocargo.Coordinate(2, 2));
  var e = new ocargo.Node(new ocargo.Coordinate(20, 2));
  a.addConnectedNodeWithBacklink(b);
  a.addConnectedNodeWithBacklink(c);
  c.addConnectedNodeWithBacklink(d);

  it("works for origin equal to destination", function() {
    var path = aStar(a, a, [a]);
    expect(path).toEqual([a]);
  });

  it("works for single step", function() {
    var path = aStar(a, b, [a, b]);
    expect(path).toEqual([a, b]);
  });

  it("returns null for unconnected points", function () {
    var path = aStar(a, e, [a, b, c, d, e]);
    expect(path).toEqual(null);
  });

  it("works for more complicated graph", function () {
    var path = aStar(a, d, [a, b, c, d, e]);
    expect(path).toEqual([a, c, d]);
  });

});

describe("PriorityQueue", function() {
  it("insert nodes and return them in the correct order", function() {
    var queue = new PriorityQueue();
    queue.push(5, 5);
    queue.push(4, 4);
    queue.push(9, 9);
    queue.push(8, 8);
    var result = [];
    result.push(queue.pop());
    result.push(queue.pop());
    result.push(queue.pop());
    result.push(queue.pop());
    expect(result).toEqual([4, 5, 8, 9]);
    expect(queue.pop()).toEqual(null);
  });

  it("returns null when empty pop", function() {
    var queue = new PriorityQueue();
    expect(queue.pop()).toEqual(null);
  });

  it("pushes and pops single item", function() {
    var queue = new PriorityQueue();
    queue.push(1, 1);
    expect(queue.pop()).toEqual(1);
  });

  it("returns whether or not it is empty", function() {
    var queue = new PriorityQueue();
    expect(queue.isEmpty()).toEqual(true);
    queue.push(1, 1);
    expect(queue.isEmpty()).toEqual(false);
    queue.pop();
    expect(queue.isEmpty()).toEqual(true);
  });
});


describe("areDestinationsReachable", function() {
  /*
   * a-b
   * |
   * c-d                                 e
   */
  var a = new ocargo.Node(new ocargo.Coordinate(1, 1));
  var b = new ocargo.Node(new ocargo.Coordinate(1, 2));
  var c = new ocargo.Node(new ocargo.Coordinate(2, 1));
  var d = new ocargo.Node(new ocargo.Coordinate(2, 2));
  var e = new ocargo.Node(new ocargo.Coordinate(20, 2));
  a.addConnectedNodeWithBacklink(b);
  a.addConnectedNodeWithBacklink(c);
  c.addConnectedNodeWithBacklink(d);
  nodes = [a, b, c, d, e];

  it("works for empty destinations", function() {
    expect(areDestinationsReachable(a, [], nodes)).toEqual(true);
  });

  it("works for a single connected destination", function() {
    expect(areDestinationsReachable(a, [d], nodes)).toEqual(true);
  });

  it("works for a single unconnected destination", function() {
    expect(areDestinationsReachable(a, [e], nodes)).toEqual(false);
  });

  it("works for a multiple connected destination", function() {
    expect(areDestinationsReachable(a, [a, b, c, d], nodes)).toEqual(true);
  });

  it("works for a multiple unconnected destination", function() {
    expect(areDestinationsReachable(e, [a, b, c, d], nodes)).toEqual(false);
  });

  it("works for a destination the same as the start", function() {
    expect(areDestinationsReachable(a, [a], nodes)).toEqual(true);
  });
});
