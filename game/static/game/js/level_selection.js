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

document.addEventListener("DOMContentLoaded", function() {
    const storedEpisode = localStorage.getItem('currentEpisode');
    const allCollapsibles = document.querySelectorAll('.collapse');

    // Function to close all except the given ID
    function closeAllExcept(openId) {
        allCollapsibles.forEach(function(collapsible) {
            if (collapsible.id !== openId) {
                collapsible.classList.remove('in');
                const toggle = document.querySelector(`[data-target="#${collapsible.id}"]`);
                toggle.classList.add('collapsed');
                toggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // Open the accordion for the stored episode
    const accordionToOpen = storedEpisode ? document.querySelector(`#collapse-${storedEpisode}`) : null;
    if (accordionToOpen) {
        accordionToOpen.classList.add('in');
        const toggle = document.querySelector(`[data-target="#${accordionToOpen.id}"]`);
        toggle.classList.remove('collapsed');
        toggle.setAttribute('aria-expanded', 'true');
    } else {
        closeAllExcept(); // Close all of no epissodes are stored
    }

    // Set up event listeners for accordion toggles
    const accordionToggles = document.querySelectorAll('.episode-title');
    accordionToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function() {
            const collapseId = toggle.getAttribute('data-target').replace('#', '');
            const isOpened = toggle.getAttribute('aria-expanded') === 'false'; // Notice the change here
            localStorage.setItem('currentEpisode', isOpened ? collapseId.split('-')[1] : null);
            if (isOpened) {
                closeAllExcept(collapseId);
            }
        });
    });

});
