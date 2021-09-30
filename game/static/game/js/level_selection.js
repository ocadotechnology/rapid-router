$(function() {
    setupCoins();
});

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
