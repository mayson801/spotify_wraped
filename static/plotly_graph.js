function create_trace(dates,values,name){
var trace = {
  x: dates,
  y: values,
  name: name,
  type: 'bar'
}
    return trace
};

function create_graph(traces){
var plotly_graph = document.getElementById('plotly_graph');
var data = traces;

var layout = {barmode: 'group'};

Plotly.newPlot('plotly_graph', traces, layout)
};
function average_constructor(){
        this.danceability = 0,
        this.energy = 0,
        this.loudness = 0,
        this.speechiness = 0,
        this.acousticness =  0,
        this.instrumentalness = 0,
        this.liveness = 0,
        this.valence = 0,
        this.tempo = 0,
        this.count = 0
};
//formats the data to group songs by year
function get_averags(JSON_data){
//create array by year with all song elements added together
var year_2020 = new average_constructor;
var year_2019 = new average_constructor;
var year_2018 = new average_constructor;
var year_2017 = new average_constructor;
var year_2016 = new average_constructor;
var counting = 0
var all = [year_2020,year_2019,year_2018,year_2017,year_2016];
//adds all the data into the correct year variable
for (song of JSON_data){
    i = 2020
    y = 0
    //while loop used to find which year song belongs to
    while (i != 2015){
        if(song[i]==true){
            //adds all the values together to be divided by count later to get average
            all[y]['danceability'] = all[y]['danceability']+song['danceability'];
            all[y]['energy'] = all[y]['energy']+song['energy'];
            all[y]['loudness'] = all[y]['loudness']+song['loudness'];
            all[y]['speechiness'] = all[y]['speechiness']+song['speechiness'];
            all[y]['acousticness'] = all[y]['acousticness']+song['acousticness'];
            all[y]['instrumentalness'] = all[y]['instrumentalness']+song['instrumentalness'];
            all[y]['liveness'] = all[y]['liveness']+song['liveness'];
            all[y]['valence'] = all[y]['valence']+song['valence'];
            all[y]['tempo'] = all[y]['tempo']+song['tempo'];
            all[y]['count'] = all[y]['count']+1;
            counting = counting + 1
            }
        i = i -1
        y= y + 1
        }
}
//this for loop coverts the totals to average
//for loop to get all year from all array
for (year of all) {
    //for loop to divide all values by count
    for (var key in year){
      year[key] = year[key] / year['count']
    }
}
console.log(counting)
return all
};

function trace_loop(data){
traces = [];
for (var key in data[0]){
    if (key != 'count'){
        var array_to_pass_to_trace = []
            for(year of data){
                //console.log(year['danceability']);
                array_to_pass_to_trace.push(year[key])
            }
        traces.push(create_trace(['2020','2019','2018','2017','2016'],array_to_pass_to_trace,key));
    }
}
return traces
}
function main(JSON_data){
        var average_data = get_averags(JSON_data)
        traces = trace_loop(average_data)
        console.log(traces);
        create_graph(traces);


}