// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// calculate data 
prd01 = Math.round((Number(sum11530035)/totalSum)*100*100)/100;
prd02 = Math.round((Number(sum11060162)/totalSum)*100*100)/100;
prd03 = Math.round((Number(sum17010087)/totalSum)*100*100)/100;
prd04 = Math.round((Number(sum17010088)/totalSum)*100*100)/100;
prd05 = Math.round((Number(sum17010004)/totalSum)*100*100)/100;
prd06 = Math.round((Number(sum17010002)/totalSum)*100*100)/100;

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["正官庄活蔘28D高麗蔘活/力飲100ml*10瓶", "正官庄高麗蔘精EVERY/TIME-秘10ml*20入", "預購正官庄活蔘28D高麗/蔘活力飲禮盒100ml*8入", "預購正官庄高麗蔘石榴飲/50ml*9入", "預購正官庄高麗蔘野櫻莓飲", "預購正官庄高麗蔘精EVERY/TIME10ml*30入"],
    datasets: [{
      data: [prd01, prd02, prd03, prd04, prd05, prd06],
      // data: [55, 30, 15],
      backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#e4a11b', '#dc4c64', '#9fa6b2'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf', '#bf8819', '#b13d50', '#80858d'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    plugins: {
      labels: {
        fontColor: 'white',
        fontStyle: 'bold',
        overlap: false,
        showActualPercentages: true,
      }
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: true,
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, data) {
          let datasetLabel = data.labels[tooltipItem.index];
          let datasetData = data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
          return datasetData + " %";
        }
      }
    },
    legend: {
      display: false
    },
    cutoutPercentage: 65,
  },
});
