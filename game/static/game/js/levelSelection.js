$(function() {
  $('#episodes').accordion({ collapsible: true, heightStyle: "content", active: false });
  normalEpisodes = $('#episodes').children('h3').not('.customLevelsEpisode');
  minOpacity = 0.1;
  maxOpacity = 0.7;
  numEpisodes = normalEpisodes.length
  for (var i=0; i < numEpisodes; i++) {
  	opacity = minOpacity + i*(maxOpacity - minOpacity)/numEpisodes;
  	normalEpisodes[i].style.background = 'rgba(99, 119, 0, '+opacity+')';
  }
});
