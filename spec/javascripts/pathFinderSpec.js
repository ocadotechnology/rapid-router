describe("Path finder suite", function() {
  /*
   * a b
   * c d
   */
  var a = new ocargo.Node(new ocargo.Coordinate(1, 1));
  var b = new ocargo.Node(new ocargo.Coordinate(1, 2));
  var c = new ocargo.Node(new ocargo.Coordinate(2, 1));
  var d = new ocargo.Node(new ocargo.Coordinate(2, 2));

  it("finds the optimal path along a super simple graph", function() {
    a.addConnectedNodeWithBacklink(b)
    var path = getOptimalPath([a, b], [new ocargo.Destination(0, b)]);

    expect(path).toEqual([a, b]);
  });

  it("finds the optimal path along a little more complicated graph", function() {
    a.addConnectedNodeWithBacklink(b)
    a.addConnectedNodeWithBacklink(c)
    c.addConnectedNodeWithBacklink(d)
    b.addConnectedNodeWithBacklink(d)
    var path = getOptimalPath([a, b, c, d], [new ocargo.Destination(0, b)]);

    expect(path).toEqual([a, b]);
  });

  it("finds the optimal path along a 3x3 graph", function() {
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
  });
});
