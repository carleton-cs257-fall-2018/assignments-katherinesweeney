// Authors: Owen Barnett and Katherine Sweeney

var planet_fields = ["Planet Discovery Method", "Planet Orbital Period (Days)",
                "Planet Orbital Period Semi-Major Axis (AU)", "Planet Orbital Eccentricity", "Planet Jupiter Mass",
                "Planet Mass Provenance", "Planet Jupiter Radius", "Planet Density (g/cm^3)", "Planet TTV Flag",
                "Planet Kepler Flag", "Planet Kepler 2 Flag", "Number of Notes on Planet", "Last Updated",
                "Planet Discovery Facility"];

var star_fields = ["First Planet in System Id", "Second Planet in System Id", "Third Planet in System Id",
              "Fourth Planet in System Id", "Fifth Planet in System Id", "Sixth Planet in System Id",
              "Seventh Planet in System Id", "Eighth Planet in System Id", "Distance From Earth (pc)",
              "Tempurature (K)", "Mass (Solar Masses)","Radius (Solar Radii)", "Last Updated"];

var planet_search_fields = {'Planet Id':"pl_id",'Planet Name': 'pl_name', "Planet's Host Star Name": 'pl_hostname', 'Discovery Method': 'pl_discmethod',
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
    return features_to_display;

}

function display(button) {
    var criteria = document.getElementById("search_criteria");
    var children = criteria.children;
    query = getBaseURL();
    if (button.innerText == "Display Planets"){
        query+="/planets?";
    }
    else {
        query+="/stars?";
    }
    for (var index = 1; index < children.length; index++) {
        textbox = children[index].children[0];
        query+=(textbox.name + "=" +textbox.value);
        if (index != children.length -1){
            query+="&";
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
                tableBody+=value;
                tableBody+="</td>";
            }
            tableBody+="</tr>";
        }

        document.getElementById('results_table').innerHTML=tableBody;

    })

}