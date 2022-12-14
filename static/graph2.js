function order_by_year_repeate(json_data) {
    clear_webpage()
    year_multi=[]
    for (let i = 0; i < json_data.length; i++) {
        year_added = json_data[i]['year_added']
        if (year_added.length >  1){
            year_multi.push({years:year_added,track_name:json_data[i]['track_name'],artist:json_data[i]['artist'],images:json_data[i]['images']})
        }
    }
    year_multi.sort(function(a, b){return b.years.length - a.years.length});
    console.log(year_multi[0]['artist'][0]['name'])
    const HTMLDIV = document.getElementById("mainbox");
    for (let i = 0; i < year_multi.length; i++) {
        artists=""
        for (let x = 0; x < year_multi[i]['artist'].length; x++){
            if (x!=0) {
                artists = artists + "," + String(year_multi[i]['artist'][x]['name'])
            }
            else {
                artists = String(year_multi[i]['artist'][x]['name'])
            }
        }

        const media_div = document.createElement("div");
        media_div.setAttribute("class","media")
        HTMLDIV.appendChild(media_div);

        const img_div = document.createElement("div")
        img_div.setAttribute("class","media-left")
        media_div.appendChild(img_div)

        const img = document.createElement("img")
        last_image=year_multi[i]['images'].length-1
        img.setAttribute("src",year_multi[i]['images'][last_image]['url'])
        img_div.appendChild(img)

        const media_txt_div = document.createElement("div")
        media_txt_div.setAttribute("class","media-body")
        media_div.appendChild(media_txt_div)

        const track_name_h4 = document.createElement("h4");
        track_name_h4.setAttribute("class","media-heading")
        const track_name_txt = document.createTextNode(year_multi[i]["track_name"] + "-" + artists);
        media_txt_div.appendChild(track_name_h4);
        track_name_h4.appendChild(track_name_txt);

        const years_p = document.createElement("p");
        const years_txt = document.createTextNode(year_multi[i]["years"]);
        years_p.appendChild(years_txt);
        media_txt_div.appendChild(years_p)

    }
}
function group_by_artist(JSON_data) {
    clear_webpage()
    var result = JSON_data.reduce((x, y) => {
            for (let artist_no = 0; artist_no < y.artist.length; artist_no++) {
                (x[y.artist[artist_no].id] = x[y.artist[artist_no].id] || []).push({track_name:y['track_name'],main_artist:y.artist[artist_no],other_artists:y['artist'],years:y['year_added']});
            }
    return x;
    }, {})
    var result_keys = Object.keys(result);
    var as_array=[]
    for (let i = 0; i < result_keys.length; i++) {
        as_array.push(result[result_keys[i]])
    }
    as_array.sort(function(a, b){return b.length - a.length});
    display_by_artist(as_array)
}
function display_by_artist(display_array){
    create_accordion()
    console.log(display_array[9][0]['main_artist']['images'])
    for (let master_artist=0 ; master_artist < display_array.length; master_artist++) {
        var song_list = []
        for (let song = 0; song < display_array[master_artist].length; song++) {
            sub_artists = ""
            for (let sub_artist = 0; sub_artist < display_array[master_artist][song]['other_artists'].length; sub_artist++) {
                if (sub_artist != 0) {
                    sub_artists = sub_artists + "," + String(display_array[master_artist][song]['other_artists'][sub_artist]['name'])
                } else {
                    sub_artists = String(display_array[master_artist][song]['other_artists'][sub_artist]['name'])
                }
            }
            song_list.push(display_array[master_artist][song]['track_name'] + "-" + sub_artists+ "-" +display_array[master_artist][song]['years'].toString())
        }

        main_artist_img=display_array[master_artist][0]['main_artist']['images'][display_array[0][0]['main_artist']['images'].length-1]
        if (main_artist_img['width'] !=160){
            console.log(display_array[master_artist][0]['main_artist']['images']);
        }

        create_accordion_card((display_array[master_artist][0]['main_artist']['name'] + " appeares " + display_array[master_artist].length), song_list, display_array[master_artist][0]['main_artist']['id'],main_artist_img['url'])
    }
}

function clear_webpage(){
    const the_box = document.getElementById('mainbox');
    while (the_box.firstChild) {
        the_box.removeChild(the_box.firstChild);
    }
}

function create_accordion(){
        const HTMLDIV = document.getElementById("mainbox");
        const accordion_div = document.createElement("div");
        accordion_div.setAttribute("id", "accordion");
        HTMLDIV.appendChild(accordion_div)
}

function create_accordion_card(header_name,body_text,ids,img_link){
    const accordion = document.getElementById("accordion");

    const card = document.createElement("div")
    card.setAttribute("class","card media")
    accordion.appendChild(card)

    const art_img_div = document.createElement("div")
    art_img_div.setAttribute("class","media-left")
    card.appendChild(art_img_div)

    const art_img = document.createElement("img")
    art_img.setAttribute("src",img_link)
    art_img_div.appendChild(art_img)

    const card_header = document.createElement("div")
    card_header.setAttribute("class","card-header media-body")
    card_header.setAttribute("id","heading"+ids)
    card.appendChild(card_header)



    const header = document.createElement("h5")
    header.setAttribute("class","mb-0 media-heading")
    card_header.appendChild(header)

    const button =document.createElement("button")
    button.setAttribute("class","btn btn-link collapsed")
    button.setAttribute("data-toggle","collapse")
    button.setAttribute("data-target","#collapse_"+ids)
    button.setAttribute("aria-expanded","false")
    button.setAttribute("aria-controls","collapse_"+ids)
    const button_header_txt = document.createTextNode(header_name)
    button.appendChild(button_header_txt);
    header.appendChild(button)

    const collapseOne = document.createElement("div")
    collapseOne.setAttribute("id","collapse_"+ids)
    collapseOne.setAttribute("class","collapse")
    collapseOne.setAttribute("aria-labelledby","heading_"+ids)
    collapseOne.setAttribute("data-parent","#accordion")
    card.appendChild(collapseOne)

    const card_body = document.createElement("div")
    card_body.setAttribute("class","card-body")
    collapseOne.appendChild(card_body)

    for (let i = 0; i < body_text.length; i++) {
        const card_body_p = document.createElement("p")
        const card_body_txt = document.createTextNode(body_text[i]);
        card_body_p.appendChild(card_body_txt)
        card_body.appendChild(card_body_p)
    }
    }

function order_by_year(JSON_data){
    for (let song = 0; song < display_array[master_artist].length; song++) {

        console.log("tes")
    }
}

function main(JSON_data) {
    console.log(JSON_data)
    order_by_year_repeate(JSON_data)

}