var arr = userData.checkups.checkups_sentences;

var options = {
  colors: ["#33AC83"],
  series: [
    {
      name: "Checkup",
      data: userData.checkups.checkups_answers,
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
    categories: userData.checkups.checkups_date,
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

if (
  userData.checkups.checkups_answers[0] &&
  userData.checkups.checkups_answers[1]
) {
  var chart = new ApexCharts(
    document.getElementById("myspace-main-metrics"),
    options
  );
  chart.render();
} else {
  document.getElementById("metrics-none").textContent =
    "There are currently no metrics to show. Keep answering your daily checkups 💪🏼";
}
