//creates a trace for the bar graph
//a trace is a bar on the bar graph
function create_trace(dates,values,name){
var trace = {
  x: dates,
  y: values,
  name: name,
  type: 'bar'
}
    return trace
};
//this creates the bar graph with the traces being inputed
function create_graph(traces){
var layout = {barmode: 'group'};

Plotly.newPlot('plotly_graph', traces, layout)
};
//this creates template for the average variable
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
var counting = 0;
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
                counting = counting + 1;

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
    return all
};
//a trace is required for every type (dancibility,tempo,ECT)
//this function just loops to creat multiple traces
function trace_loop(data){
traces = [];
for (var key in data[0]){
    if (key != 'count'){
        var array_to_pass_to_trace = []
            for(year of data){
                array_to_pass_to_trace.push(year[key])
            }
        traces.push(create_trace(['2020','2019','2018','2017','2016'],array_to_pass_to_trace,key));
    }
}
return traces
}

//this functions finds values that are in multiple years
function in_multiple_years(data){
    all = []
    for (song of JSON_data){
        count = 0
        var dates = [song['name']]
        for (i = 2020; i != 2015; i--) {
                dates.push(song[i])
                if(song[i]==true){
                count = count+1
            }
        }
        if (count != 1){
          dates.push(count)
          all.push(dates)
        }
        }
return all
}
//this creates the table
function create_table(data_values){
values_formated = []
//this basically roatates the array
for (i=0; i != 7; i++) {
    array = []
    for (data of data_values){
        array.push(data[i])
    }
    values_formated.push(array)
}
console.log(values_formated)
var data = [{
  type: 'table',
  header: {
    values: [["<b>id</b>"], ["<b>2020</b>"],["<b>2019</b>"], ["<b>2018</b>"], ["<b>2017</b>"],["<b>2016</b>"]],
    align: "center",
    line: {width: 1, color: 'black'},
    fill: {color: "grey"},
    font: {family: "Arial", size: 12, color: "white"}
  },
  cells: {
    values: values_formated,
    align: "center",
    line: {color: "black", width: 1},
    font: {family: "Arial", size: 11, color: ["black"]}
  }
}]
    Plotly.newPlot('plotly_table', data);
}
function main(JSON_data){
        var average_data = get_averags(JSON_data)
        traces = trace_loop(average_data)
        create_graph(traces);

        var table_data = in_multiple_years(JSON_data)
        create_table(table_data)
}