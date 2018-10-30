/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 4 May 2018
 *
 * A little bit of Javascript showing one small example of AJAX
 * within the "books and authors" sample for Carleton CS257,
 * Spring Term 2017.
 *
 * This example uses a very simple-minded approach to Javascript
 * program structure, which suffers from the problem of
 * "global namespace pollution". We'll talk more about this after
 * you get a feel for some Javascript basics.
 */

// IMPORTANT CONFIGURATION INFORMATION
// The contents of getBaseURL below reflects our assumption that
// the web application (books_website.py) and the API (books_api.py)
// will be running on the same host but on different ports.
//
// But if you take a look at the contents of getBaseURL, you may
// ask: where does the value of api_port come from? The answer is
// a little bit convoluted. (1) The command-line syntax of
// books_website.py includes an argument for the API port;
// and (2) the index.html Flask/Jinja2 template includes a tiny
// bit of Javascript that declares api_port and assigns that
// command-line API port argument to api_port. This happens
// before books.js is loaded, so the functions in books.js (like
// getBaseURL) can access api_port as needed.

// initialize();
//
// function initialize() {
//     var element = document.getElementById('authors_button');
//     if (element) {
//         element.onclick = onAuthorsButtonClicked;
//     }
// }
//
// function getBaseURL() {
//     var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
//     return baseURL;
// }
//
// function onAuthorsButtonClicked() {
//     var url = getBaseURL() + '/authors/';
//
//     // Send the request to the Books API /authors/ endpoint
//     fetch(url, {method: 'get'})
//
//     // When the results come back, transform them from JSON string into
//     // a Javascript object (in this case, a list of author dictionaries).
//     .then((response) => response.json())
//
//     // Once you have your list of author dictionaries, use it to build
//     // an HTML table displaying the author names and lifespan.
//     .then(function(authorsList) {
//         // Build the table body.
//         var tableBody = '';
//         for (var k = 0; k < authorsList.length; k++) {
//             tableBody += '<tr>';
//
//             tableBody += '<td><a onclick="getAuthor(' + authorsList[k]['id'] + ",'"
//                             + authorsList[k]['first_name'] + ' ' + authorsList[k]['last_name'] + "')\">"
//                             + authorsList[k]['last_name'] + ', '
//                             + authorsList[k]['first_name'] + '</a></td>';
//
//             tableBody += '<td>' + authorsList[k]['birth_year'] + '-';
//             if (authorsList[k]['death_year'] != 0) {
//                 tableBody += authorsList[k]['death_year'];
//             }
//             tableBody += '</td>';
//             tableBody += '</tr>';
//         }
//
//         // Put the table body we just built inside the table that's already on the page.
//         var resultsTableElement = document.getElementById('results_table');
//         if (resultsTableElement) {
//             resultsTableElement.innerHTML = tableBody;
//         }
//     })
//
//     // Log the error if anything went wrong during the fetch.
//     .catch(function(error) {
//         console.log(error);
//     });
// }
//
// function getAuthor(authorID, authorName) {
//     // Very similar pattern to onAuthorsButtonClicked, so I'm not
//     // repeating those comments here. Read through this code
//     // and see if it makes sense to you.
//     var url = getBaseURL() + '/books/author/' + authorID;
//
//     fetch(url, {method: 'get'})
//
//     .then((response) => response.json())
//
//     .then(function(booksList) {
//         var tableBody = '<tr><th>' + authorName + '</th></tr>';
//         for (var k = 0; k < booksList.length; k++) {
//             tableBody += '<tr>';
//             tableBody += '<td>' + booksList[k]['title'] + '</td>';
//             tableBody += '<td>' + booksList[k]['publication_year'] + '</td>';
//             tableBody += '</tr>';
//         }
//         var resultsTableElement = document.getElementById('results_table');
//         if (resultsTableElement) {
//             resultsTableElement.innerHTML = tableBody;
//         }
//     })
//
//     .catch(function(error) {
//         console.log(error);
//     });
// }
//
var planet_fields = ["Planet Discovery Method", "Planet Orbital Period (Days)",
                "Planet Orbital Period Semi-Major Axis (AU)", "Planet Orbital Eccentricity", "Planet Jupiter Mass",
                "Planet Mass Provenance", "Planet Jupiter Radius", "Planet Density (g/cm^3)", "Planet TTV Flag",
                "Planet Kepler Flag", "Planet Kepler 2 Flag", "Number of Notes on Planet", "Last Updated",
                "Planet Discovery Facility"];

var star_fields = ["First Planet in System", "Second Planet in System", "Third Planet in System",
              "Fourth Planet in System", "Fifth Planet in System", "Sixth Planet in System",
              "Seventh Planet in System", "Eighth Planet in System", "Distance From Earth (pc)",
              "Tempurature (K)", "Mass (Solar Masses)","Radius (Solar Radii)", "Last Updated"];

var planet_search_fields = {'Planet Name': 'pl_name', "Planet's Host Star Name": 'pl_hostname', 'Discovery Method': 'pl_discmethod',
    'Number of Planets Orbiting Same Star': 'pl_pnum', 'Max Number of Planets Orbiting Same Star': 'pl_pnummax',
    'Min Number of Planets Orbiting Same Star': 'pl_pnummin', 'Orbital Period (days)': 'pl_orbper',
    'Max Orbital Period (days)': 'pl_orbpermax', 'Min Orbital Period (days)': 'pl_orbpermin', 'Orbit Semi-Major Axis (AU)': 'pl_orbsmax',
    'Max Orbit Semi-Major Axis (AU)': 'pl_orbsmaxmax', 'Min Orbit Semi-Major Axis (AU)': 'pl_orbsmaxmin', 'Eccentricity': 'pl_eccen',
    'Max Eccentricity': 'pl_eccenmax', 'Min Eccentricity': 'pl_eccenmin', 'Mass (Jupiter Masses)': 'pl_massj',
    'Max Mass (Jupiter Masses)': 'pl_massjmax', 'Min Mass (Jupiter Masses)': 'pl_massjmin', 'Radius (Jupiter Radii)': 'pl_radj',
    'Max Radius (Jupiter Radii)': 'pl_radjmax', 'Min Radius (Jupiter Radii)': 'pl_radjmin', 'Density (g/cm^3)': 'pl_dens',
    'Max Density (g/cm^3)': 'pl_densmax', 'Min Density (g/cm^3)': 'pl_densmin', 'Orbit Exhibits TTV (Yes: 1; No: 0)': 'pl_ttvflag',
    'Found on Kepler Mission (Yes: 1; No: 0)': 'pl_kepflag', 'Found on Kepler2 Mission (Yes: 1; No: 0)': 'pl_k2flag',
    'Number of Notes': 'pl_nnotes', 'Max Number of Notes': 'pl_nnotesmax', 'Min Number of Notes': 'pl_nnotesmin', 'Discovery Facility': 'pl_facility'};

var star_search_feilds = {'Star Name': 'st_name', 'Number of Planets Orbiting': 'st_pnum', 'Max Number of Planets Orbiting': 'st_pnummax',
    'Min Number of Planets Orbiting': 'st_pnummin', 'Name of First Planet': 'st_planet_1_name', 'Name of Second Planet': 'st_planet_2_name',
    'Name of Third Planet': 'st_planet_3_name', 'Name of Fourth Planet': 'st_planet_4_name', 'Name of Fifth Planet': 'st_planet_5_name',
    'Name of Sixth Planet': 'st_planet_6_name', 'Name of Seventh Planet': 'st_planet_7_name', 'Name of Eighth Planet': 'st_planet_8_name',
    'Distance From Earth (pc)': 'st_dist', 'Max Distance From Earth (pc)': 'st_distmax', 'Min Distance From Earth (pc)': 'st_distmin',
    'Temperature (K)': 'st_teff', 'Max Temperature (K)': 'st_teffmax', 'Min Temperature (K)': 'st_teffmin',
    'Mass (Solar Masses)': 'st_mass', 'Max Mass (Solar Masses)': 'st_massmax', 'Min Mass (Solar Masses)': 'st_massmin',
    'Radius (Solar Radii)': 'st_rad', 'Max Radius (Solar Radii)': 'st_radmax', 'Min Radius (Solar Radii)': 'st_radmin'};
var planet_star_search_fields = {};
Object.assign(planet_star_search_fields, star_search_feilds, planet_search_fields);



window.onload = function() {
    make_table_right_side(["Planet Name", "Host Star Name"], planet_fields);
    make_table_left_side(planet_search_fields);
}

function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + api_port;
    return baseURL;
}

function remove_parent_display(current) {
    var parent = current.parentElement;
    current.parentElement.removeChild(current);

    var text = parent.textContent;

    var select = document.getElementById('add_feature');

    var option = document.createElement("option");
    option.text = text;
    select.add(option);
    parent.parentElement.removeChild(parent);
}

function remove_parent_criteria(current) {
    var parent = current.parentElement;
    current.parentElement.removeChild(current);

    var text = parent.textContent;

    var select = document.getElementById('add_criteria');

    var option = document.createElement("option");
    option.text = text;
    select.add(option);
    parent.parentElement.removeChild(parent);
}

function pick_option(option) {
    var text = option.value;

    var div = document.createElement('div');

    div.className = "inner_features_to_display small";

    div.innerHTML = text+"<button onclick='remove_parent_display(this)' type='button' class = 'x_button'>x</button>";

    document.getElementById('features_to_display').appendChild(div);

    for (var i=0; i<option.length; i++){
        if (option.options[i].text == text )
            option.remove(i);
  }
}

function pick_criteria(criteria) {
    var text = criteria.value;

    var div = document.createElement('div');

    div.className = "inner_features_to_display small";

    div.innerHTML = text+"<input type='text' class = 'text_box' name="+planet_star_search_fields[text]+"><button onclick='remove_parent_criteria(this)' type='button' class = 'x_button'>x</button>";

    document.getElementById('search_criteria').appendChild(div);

    for (var i=0; i<criteria.length; i++){
        if (criteria.options[i].text == text)
            criteria.remove(i);
  }
}

function make_table_right_side(selected, options) {
    var table = document.getElementById('features_to_display');
    table.innerHTML = "<div class = 'inner_features_to_display big'>Features To Display</div>";
    for (var index = 0; index < selected.length; index++) {
        var element = "";
        element+= "<div class = 'inner_features_to_display small'>";
        element+= selected[index];
        element+= "<button onclick='remove_parent_display(this)' type='button' class = 'x_button'>x</button></div>";
        table.innerHTML+=element;
    }

    var list = document.getElementById('add_feature');
    list.innerHTML = "<option>Add Feature</option>";
    for (var index = 0; index < options.length; index++) {
        var element = "";
        element+= "<option>";
        element+= options[index];
        element+= "</option>";
        list.innerHTML+=element;
    }
}

function make_table_left_side(options) {
    var table = document.getElementById('search_criteria');
    table.innerHTML = "<div class = 'inner_features_to_display big'>Search Criteria</div>";

    var list = document.getElementById('add_criteria');
    list.innerHTML = "<option>Add Criteria</option>";
    for (var key in options) {
        var element = "";
        element+= "<option>";
        element+= key;
        element+= "</option>";
        list.innerHTML+=element;
    }
}

function click_star() {
    var planet_button = document.getElementById("planet_buttton");
    var star_button = document.getElementById("star_button");
    star_button.setAttribute("class", "button button_selected");
    planet_button.setAttribute("class", "button button_not_selected");
    star_button.setAttribute("onClick", "");
    planet_button.setAttribute("onClick", "click_planet()");
    make_table_right_side(["Star Name", "Number of Planets In System"], star_fields);
    make_table_left_side(star_search_feilds);
    document.getElementById("get_results").innerText="Display Stars";
}

function click_planet() {
    var planet_button = document.getElementById("planet_buttton");
    var star_button = document.getElementById("star_button");
    planet_button.setAttribute("class", "button button_selected");
    star_button.setAttribute("class", "button button_not_selected");
    planet_button.setAttribute("onClick", "");
    star_button.setAttribute("onClick", "click_star()");
    make_table_right_side(["Planet Name", "Host Star Name"], planet_fields);
    make_table_left_side(planet_search_fields);
    document.getElementById("get_results").innerText="Display Planets"
}

function get_display_features() {
    var features_to_display = [];
    var children = document.getElementById("features_to_display").children;
    for (var index = 1; index < children.length; index++) {
        child = children[index];
        var text = child.innerText;
        features_to_display.push(text.substring(0,text.length-2));
    }
    return features_to_display

}

async function get_planet_name(value) {
    if (value == "None") {
        return "None"
    }
    query = getBaseURL() + "/planet/" + value;
    window.planet_name = "";
    await fetch(query, {method: 'get'}).then((response) => response.json()).then(function(planet_list) {
        var planet = planet_list[0];
        var planet_name = planet['Planet Name'];
        window.planet_name = planet_name;
    })
    console.log(window.planet_name)
    return window.planet_name
    // console.log("break")
    // console.log(window.planet_name)
    // return planet_name[[PromiseValue]]

}

function display(button) {
    var criteria = document.getElementById("search_criteria");
    var children = criteria.children;
    query = getBaseURL();
    if (button.innerText == "Display Planets"){
        query+="/planets?"
    }
    else {
        query+="/stars?"
    }
    for (var index = 1; index < children.length; index++) {
        textbox = children[index].children[0];
        query+=(textbox.name + "=" +textbox.value);
        if (index != children.length -1){
            query+="&"
        }
    }

    fetch(query, {method: 'get'}).then((response) => response.json()).then(function(planet_star_list) {
        display_features = get_display_features();
        var tableBody = "<tr class = 'table_row'>";
        for (var index = 0; index < display_features.length; index++) {
            tableBody+="<th class = 'table_header'>";
            tableBody+=display_features[index];
            tableBody+="</th>";
        }
        tableBody+="</tr>";

        for (var index = 0; index < planet_star_list.length; index++) {
            planet_star = planet_star_list[index];
            tableBody+="<tr class = 'table_row'>";
            for (var display_index = 0; display_index < display_features.length; display_index++) {
                tableBody+="<td class = 'table_data'>";
                var value = planet_star[display_features[display_index]];
                if (display_features[display_index].includes("Planet in System")){
                    test = get_planet_name(value)
                    console.log(test)
                }
                tableBody+=value;
                tableBody+="</td>";
            }
            tableBody+="</tr>"
        }

        document.getElementById('results_table').innerHTML=tableBody;

    })

}