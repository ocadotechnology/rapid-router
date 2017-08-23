/*
 Code for Life
 Copyright (C) 2017, Ocado Innovation Limited
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
    var normalEpisodes = $('#episodes').children('h3').not('.customLevelsEpisode');
    var minOpacity = 0.1;
    var maxOpacity = 0.7;
    var numEpisodes = normalEpisodes.length;
    var bg = {'r':236, 'g':234, 'b':238};
    var baseColor = {'r': 70, 'g':44, 'b': 213};
    for (var i=0; i < numEpisodes; i++) {
        var opacity = minOpacity + i*(maxOpacity - minOpacity)/numEpisodes;
        var color = {'r':baseColor.r, 'g':baseColor.g, 'b':baseColor.b, 'a':opacity};
        var combinedColor = combineColors(bg, color);
        var newRGB = 'rgb('+Math.floor(combinedColor.r).toString()+', '+Math.floor(combinedColor.g).toString()+', '+Math.floor(combinedColor.b).toString()+')';
        normalEpisodes[i].style.background = newRGB;
    }

});

function combineColors(bg, color)
{
    var a = color.a;

    return {'r': (1 - a) * bg.r + a * color.r,
        'g': (1 - a) * bg.g + a * color.g,
        'b': (1 - a) * bg.b + a * color.b};
}

