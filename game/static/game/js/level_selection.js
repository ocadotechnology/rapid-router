$(function() {
    setupCoins();
});

function setupCoins() {
    for(var i = 0; i < EPISODES.length; i++) {
        var episode = EPISODES[i];

        var minScore = 20;
        var episodeToOpen;
        var ratios = [];
        for(var j = 0; j < episode.levels.length; j++) {
            var level = episode.levels[j];
            if (level.score === "None"){
                $('.level_image.coin_image[value=' + level.name + ']').remove();
                if(!episodeToOpen) {
                    episodeToOpen =  episode;
                }
                ratios.push(-1);
            } else {
                var ratio = level.score / level.maxScore;
                ratios.push(ratio);
                imageStr = getImageStr(ratio);
                $('.level_image.coin_image[value=' + level.name + ']').attr('src', imageStr);
            }
        }

        if (ratios.length > 0 && !ratios.includes(-1)){
            var sum =0;
            ratios.forEach ((item) => sum += item);
            var ave_ratio = sum/ratios.length;
            img = getImageStr(ave_ratio);
            $('.episode_image.coin_image[value=' + episode.id + ']').attr('src', img)
        } else {
            $('.episode_image.coin_image[value=' + episode.id + ']').remove();
        }
    }

    for(var i = 0; i < OTHER_LEVELS.length; i++) {
        var level = OTHER_LEVELS[i];

        imageStr = getImageStr(level.score / level.maxScore);
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

    function getImageStr(fraction) {
        var imageStr = "/static/game/image/coins/coin_";
        if(fraction >= 0.99) {
            return imageStr + 'gold.svg';
        }
        else if(fraction > 0.5) {
            return imageStr + 'silver.svg';
        }
        else if(fraction >= 0.0) {
            return imageStr + 'copper.svg';
        }
    }
}
