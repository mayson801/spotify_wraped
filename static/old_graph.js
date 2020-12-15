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
                { label: "2016",  y: data[4]  },
                { label: "2017", y: data[3]  },
                { label: "2018", y: data[2]  },
                { label: "2019",  y: data[1]  },
                { label: "2020",  y: data[0]  }
            ]
        }
        ]
    });
    chart.render();

    }