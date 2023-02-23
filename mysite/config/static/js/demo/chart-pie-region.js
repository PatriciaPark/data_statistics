// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// calculate data 
rgn01 = Math.round((Number(sumNor)/totalSum2)*100*100)/100;
rgn02 = Math.round((Number(sumMid)/totalSum2)*100*100)/100;
rgn03 = Math.round((Number(sumSou)/totalSum2)*100*100)/100;
rgn04 = Math.round((Number(sumEas)/totalSum2)*100*100)/100;
rgn05 = Math.round((Number(sumIsl)/totalSum2)*100*100)/100;

// Pie Chart Example
var ctx = document.getElementById("myPieChart2");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["北部", "中部", "南部", "東部", "外島"],
    datasets: [{
      data: [rgn01, rgn02, rgn03, rgn04, rgn05],
      // data: [55, 30, 15],
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#e4a11b', '#dc4c64'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf', '#bf8819', '#b13d50'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, data) {
          let datasetLabel = data.labels[tooltipItem.index];
          let datasetData = data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
          return datasetLabel + ": " + datasetData + " %";
        }
      }
    },
    legend: {
      display: false
    },
    cutoutPercentage: 0,
  },
});
