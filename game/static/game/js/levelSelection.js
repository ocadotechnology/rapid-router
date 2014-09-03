$(function() {
    $('#episodes').accordion({ collapsible: true, heightStyle: "content", active: false });
    normalEpisodes = $('#episodes').children('h3').not('.customLevelsEpisode');
    minOpacity = 0.1;
    maxOpacity = 0.7;
    numEpisodes = normalEpisodes.length
    background = $('body').css('background-color');
    bg = {'r':236, 'g':234, 'b':238};
    baseColor = {'r': 99, 'g':119, 'b': 0};
    for (var i=0; i < numEpisodes; i++) {
      	opacity = minOpacity + i*(maxOpacity - minOpacity)/numEpisodes;
      	var color = {'r':baseColor.r, 'g':baseColor.g, 'b':baseColor.b, 'a':opacity};
      	combinedColor = combineColors(bg, color);
      	var newRGB = 'rgb('+Math.floor(combinedColor.r).toString()+', '+Math.floor(combinedColor.g).toString()+', '+Math.floor(combinedColor.b).toString()+')';
      	normalEpisodes[i].style.background = newRGB;
    }

    setupCoins();
});

function combineColors(bg, color)
{
    var a = color.a;

    return {'r': (1 - a) * bg.r + a * color.r,
	        'g': (1 - a) * bg.g + a * color.g,
		    'b': (1 - a) * bg.b + a * color.b};
}

function setupCoins() {
    for(var i = 0; i < EPISODES.length; i++) {
        var episode = EPISODES[i];

        var minScore = 20;
        for(var j = 0; j < episode.levels.length; j++) {
            var level = episode.levels[j];
            
            if(level.score !== "None") {
                $('.level_image.coin_image[value=' + level.id + ']').attr('src', getImageStr(level.score));
            }
            else {
                $('.level_image.coin_image[value=' + level.id + ']').remove();
                minScore = "None";
            }

            if(minScore != "None" && level.score < minScore) {
                minScore = level.score;
            }
        }

        if(minScore !== "None") {
            $('.episode_image.coin_image[value=' + episode.id + ']').attr('src', getImageStr(minScore))
        }
        else {
            $('.episode_image.coin_image[value=' + episode.id + ']').remove();
        }
    }

    function getImageStr(score) {
        var imageStr = "/static/game/image/coins/coin_";
        if(score == "None") {
            return "";
        }
        else if(score == 20) {
            return imageStr + 'gold.svg';
        }
        else if(score > 10) {
            return imageStr + 'silver.svg';
        }
        else if(score) {
            return imageStr + 'copper.svg';
        }
    }
}
