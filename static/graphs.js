function myFunction(name,data) {
    var chart = new CanvasJS.Chart(name, {
        theme: "light1", // "light2", "dark1", "dark2"
        animationEnabled: true, // change to true
        title:{
            text: name
        },
        data: [
        {
            // Change type to "bar", "area", "spline", "pie",etc.
            type: "column",
            dataPoints: [
                { label: "2016",  y: data.dancibilty[4]  },
                { label: "2017", y: data.dancibilty[3]  },
                { label: "2018", y: data.dancibilty[2]  },
                { label: "2019",  y: data.dancibilty[1]  },
                { label: "2020",  y: data.dancibilty[0]  }
            ]
        }
        ]
    });
    chart.render();

    }