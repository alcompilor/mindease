var arr = userData.checkups.checkups_sentences; // store checkups content in array

let checkups_answers = [];
let checkups_date = [];

userData.checkups.checkups_answers.forEach((element) => {
  element ? checkups_answers.push(element) : null;
}); // push fetched checkups answers to new array

userData.checkups.checkups_date.forEach((element) => {
  element ? checkups_date.push(new Date(element).toISOString()) : null;
}); // push fetched checkups dates to new array

var options = {
  colors: ["#33AC83"],
  series: [
    {
      name: "Checkup",
      data: checkups_answers,
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
    categories: checkups_date,
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
        return arr[dataPointIndex];
      },
    },
  },
}; // chart options

if (
  userData.checkups.checkups_answers[0] &&
  userData.checkups.checkups_answers[1]
) {
  // if there are at least 2 checkups
  var chart = new ApexCharts(
    document.getElementById("myspace-main-metrics"),
    options
  ); // construct chart
  chart.render(); // render chart in DOM
} else {
  document.getElementById("metrics-none").textContent =
    "There are currently no metrics to show. Keep answering your daily checkups 💪🏼"; // display msg
}
