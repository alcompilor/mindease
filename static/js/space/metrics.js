var arr = [
  "vimeo b",
  "messenger for talking",
  "facebook for socializing",
  "linkedin for socialicing professionally",
];

var options = {
  colors: ["#33AC83"],
  series: [
    {
      name: "Checkup",
      data: [1, 2, 3, 1, 5, 3, 5],
    },
  ],
  chart: {
    height: 300,
    type: "area",
  },
  dataLabels: {
    enabled: true,
  },
  stroke: {
    curve: "smooth",
  },
  xaxis: {
    type: "datetime",
    categories: [
      "2018-09-19",
      "2018-09-20",
      "2018-09-21",
      "2018-09-22",
      "2018-09-23",
      "2018-09-24",
      "2018-09-25",
    ],
  },
  tooltip: {
    style: {
      fontSize: "14px",
      fontFamily: undefined,
    },
    x: {
      format: "dd/MM",
    },
    y: {
      formatter: function (value, { dataPointIndex }) {
        //please look at the console to see the issue
        //this will work if static values are used
        //return value + " " + arr[0];
        return arr[dataPointIndex];
      },
    },
  },
};

var chart = new ApexCharts(
  document.getElementById("myspace-main-metrics"),
  options
);
chart.render();
