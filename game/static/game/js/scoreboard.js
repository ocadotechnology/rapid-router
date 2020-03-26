/*
 Code for Life

 Copyright (C) 2019, Ocado Innovation Limited

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
$(':checkbox').on('change', function() {
    $(this).closest('li').toggleClass('checked', $(this).is(':checked'))
})

$('.all-class > label, .all-level').on('change', function() {
    var check = $(this).find('input').is(':checked')
    $(this).closest('ul').find(':checkbox').prop('checked', check).closest('li').toggleClass('checked', check)
})

$('.episode').on('change', function() {
    var check = $(this).find('input').is(':checked')
    var first = $(this).attr('data-first')
    var last = $(this).attr('data-last')
    for (var i = first; i <= last; i++) {
        $('.level-'+i).find(':checkbox').prop('checked', check).closest('li').toggleClass('checked', check)
    }
})

$('.expander').on('click', function() {
    var el = $(this).closest('li')
    var first = el.attr('data-first')
    var last = el.attr('data-last')
    if ($('.level-'+first).is(':visible')) {
        el.find('span').switchClass('glyphicon-triangle-bottom', 'glyphicon-triangle-left')
    } else {
        el.find('span').switchClass('glyphicon-triangle-left', 'glyphicon-triangle-bottom')
    }
    for (var i = first; i <= last; i++) {
        $('.level-'+i).toggle('blind')
    }
})
