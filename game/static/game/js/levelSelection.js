/*
Code for Life

Copyright (C) 2015, Ocado Innovation Limited

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

ADDITIONAL TERMS – Section 7 GNU General Public Licence

This licence does not grant any right, title or interest in any “Ocado” logos,
trade names or the trademark “Ocado” or any other trademarks or domain names
owned by Ocado Innovation Limited or the Ocado group of companies or any other
distinctive brand features of “Ocado” as may be secured from time to time. You
must not distribute any modification of this program using the trademark
“Ocado” or claim any affiliation or association with Ocado or its employees.

You are not authorised to use the name Ocado (or any of its trade names) or
the names of any author or contributor in advertising or for publicity purposes
pertaining to the distribution of this program, without the prior written
authorisation of Ocado.

Any propagation, distribution or conveyance of this program must include this
copyright notice and these terms. You must not misrepresent the origins of this
program; modified versions of the program must be marked as such and not
identified as the original program.
*/
$(function() {
    $('#episodes').accordion({ collapsible: true, heightStyle: "content", active: false });
    normalEpisodes = $('#episodes').children('h3').not('.customLevelsEpisode');
    minOpacity = 0.1;
    maxOpacity = 0.7;
    numEpisodes = normalEpisodes.length;
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
        var episodeToOpen;
        for(var j = 0; j < episode.levels.length; j++) {
            var level = episode.levels[j];
            
            imageStr = getImageStr(level.score, level.maxScore);
            if(imageStr !== '') {
                $('.level_image.coin_image[value=' + level.name + ']').attr('src', imageStr);
            }
            else {
                $('.level_image.coin_image[value=' + level.name + ']').remove();
                minScore = "None";
                if(!episodeToOpen) {
                    episodeToOpen =  episode;
                }
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

    for(var i = 0; i < OTHER_LEVELS.length; i++) {
        var level = OTHER_LEVELS[i];

        imageStr = getImageStr(level.score, level.maxScore);
        if(imageStr !== '') {
            $('.level_image.coin_image[value=' + level.id + ']').attr('src', imageStr);
        }
        else {
            $('.level_image.coin_image[value=' + level.id + ']').remove();
        }
    }

    if(episodeToOpen && (USER_STATUS === 'SCHOOL_STUDENT' || USER_STATUS === 'INDEPENDENT_STUDENT')) {
        $('#episode' + episodeToOpen.id).click();
    }

    function getImageStr(score, maxScore) {
        var imageStr = "/static/game/image/coins/coin_";
        percentage = 100.0 * score / maxScore;
        if(score == "None") {
            return "";
        }
        else if(percentage >= 99.99999) {
            return imageStr + 'gold.svg';
        }
        else if(percentage > 0.5) {
            return imageStr + 'silver.svg';
        }
        else if(percentage >= 0.0) {
            return imageStr + 'copper.svg';
        }
        return '';
    }
}
