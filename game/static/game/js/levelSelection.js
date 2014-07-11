
function showEpisodes(data, func) {
  var selection = d3.select('#container')
                    .selectAll("div.episode")
                    .data(data);
  selection.enter()
           .append("div")
           .attr("class", "episode");
  selection.on("click", func)
           .style("background-color", function(d){return d.colour})
           .html(function(d) { return d.name; });
  selection.exit().remove();
};


function showLevels(episodeID,levels, opacity) {
  var selection = d3.select('div.episode')
                    .selectAll("div.level")
                    .data(levels);
  selection.enter()
           .append("div")
           .attr("class", "level");
  selection.on("click", function(d) { window.location.href = d.id; })
           .style("background-color", function(d){return "rgba(99, 119, 0, " + opacity + ")"});
  selection.append("div")
           .attr("class", "levelTitle")
           .html(function(d) { return d.name + ": " + d.title; });
  selection.append("div")
           .attr("class", "levelScore")
           .html(function(d) { return d.score; });
  selection.exit()
           .remove();       
};

function clearLevels() {
  var selection = d3.select('#container')
                    .selectAll("div.level")
                    .data([]);
  selection.exit().remove();
};

function showLevelsForEpisode(episode, colour) {
  levels = episode.levels.slice()
  levels.push({name:"Random", title:"Try your hand at a random level.", score:"", id:"levels/random/"+episode.id});
  showLevels(episode.id,levels,colour);
};

function showEpisode(id) {
  var episodes = EPISODE_LIST.filter(function(episode) { return episode.id === id; });
  showEpisodes(episodes, function(d) { enterEpisodes(); });
  showLevelsForEpisode(episodes[0], episodes[0].opacity);
};

function enterEpisodes() {
  showEpisodes(EPISODE_LIST, function(d){ showEpisode(d.id); });
  clearLevels();
};

$(function() {
  enterEpisodes();
});
