new CircleType(document.getElementById('curvetest')).radius(600);

d3.json("static/grouped_JSON.json").then((data) => {
  let uniquevals = [...new Set(data.Make)]
  d3.select("#selDataset").selectAll("myOptions").data(data.Model).enter().append("option").text(function (d) { return d; }).attr("value", function (d) { return d; });
  d3.select("#selDataset2").selectAll("myOptions").data(uniquevals).enter().append("option").text(function (d) { return d; }).attr("value", function (d) { return d; })
    //  Create the Traces
    let trace1 = {
      labels: data.Model,
      values: data.count,
      type: "pie",
    };

    let layout = {
        title: "Number of Electric Vehicles by Model",
        height: 500,
        width: 700,
        paper_bgcolor:'rgba(0,0,0,0)'
      };
      
    // Create the data array for the plot.
    let plotData = [trace1];

    // Plot the chart to a div tag with an ID of "plot".
    Plotly.newPlot("simpleplot", plotData, layout);

    //  Create the Traces
    let trace2 = {
      x: data.Model,
      y: data.Msrp,
      type: "bar",
    
    };

    let layout2 = {
        title: "MSRP by Model",
        barmode: 'stack',
        paper_bgcolor:'rgba(0,0,0,0)',
        plot_bgcolor:'rgba(0,0,0,0)'
      };
      
    // Create the data array for the plot.
    let plotData2 = [trace2];

    // Plot the chart to a div tag with an ID of "plot".
    Plotly.newPlot("simpleplot1", plotData2, layout2);


  var trace4 = [
    {
      domain: { x: [0, 1], y: [0, 1] },
      value: data.Range[0],
      title: { text: "Range"},
      type: "indicator",
      mode: "gauge+number",
      gauge: {
        axis: {range: [0,400]},
        steps: [
          {range: [0,250], color: "lightgray"},
          {range: [250,350], color: "lightgreen"}
        ]
      }
    }
  ];
  var layout3 = { width: 600, height: 500, margin: { t: 0, b: 0 },paper_bgcolor:'rgba(0,0,0,0)'};

  Plotly.newPlot('myDiv', trace4, layout3)});
  

function optionChanged(data) {
  d3.json("static/grouped_JSON.json").then((data2) => {
    let newcount = []
    let newrange =[]
    let newmsrp = []
    for (let i=0; i < data2.Model.length; i++) {
      if (data == data2.Model[i]) {
        newcount.push(data2.count[i]);
        newrange.push(data2.Range[i]);
        newmsrp.push(data2.Msrp[i]);
        console.log(data2.Model[i]);
        console.log(data2.Msrp[i]);
        console.log(data2.Range[i])
      }
      
    }
    Plotly.restyle("myDiv","value",newrange);
    Plotly.restyle("myDiv","title","text" ["Range of " + data])
  
    
  });
}
function optionChanged2(data) {
  d3.json("static/grouped_JSON.json").then((data2) => {
    let newcount = []
    let newmsrp = []
    let models=[]
    for (let i=0; i < data2.Make.length; i++) {
      if (data == data2.Make[i]) {
        newcount.push(data2.count[i]);
        newmsrp.push(data2.Msrp[i]);
        models.push(data2.Model[i])
        console.log(data2.Model[i]);
        console.log(data2.Msrp[i]);
      }
      
    }
    Plotly.restyle("simpleplot","values",[newcount]);
    Plotly.restyle("simpleplot","labels",[models]);
    Plotly.restyle("simpleplot1","y",[newmsrp]);
    Plotly.restyle("simpleplot1","x",[models]);
  
    
  });
};

