var chartConfig_word = {
  type: 'mixed',
  title: {
    align: 'left',
    fontColor: '#c4c4c4'
  },
  plot: {
    tooltip: {
      visible: true
    },
    aspect: 'spline',
    marker: {
      visible: false
    }
  },
  plotarea: {},
  scaleX: {
    values: [],
    itemsOverlap: true,
    lineWidth: '0px',
    tick: {
      alpha: 1,
      lineColor: '#2196F3',
      lineWidth: '2px'
    },
    zooming: true,
    zoomTo: [0, 30]
  },
  scaleY: {
    values: '0:1000:125',
    guide: {
      visible: false
    }
  },
  scaleY2: {},
  crosshairX: {
    lineColor: '#2196F3',
    lineStyle: 'dashed',
    lineWidth: '2px',
    marker: {
      type: 'triangle',
      size: '5px',
      visible: true
    },
    plotLabel: {
      visible: false
    }
  },
  preview: {
    live: true
  },
  series: [/*{
      type: 'line',
      values: [156, 54, 43, 124, 49],
      backgroundColor: '#FFEB3B',
      scales: 'scale-x, scale-y-2'
    },*/
    {
      type: 'line',
      values: [],
      lineColor: '#2196F3',
      scales: 'scale-x, scale-y-2'
    }
  ]
};

zingchart.render({
  id: 'myChart_word',
  data: chartConfig_word,
  width: '100%',
});

function chart_word(){
  zingchart.render({
    id: 'myChart_word',
    data: chartConfig_word,
    width: '100%',
  });
};


/**
 * As we are moving the guide, we want to update the items outside
 * of the chart. We could do this inside the chart, but since JS
 * is single threaded we don't want to block UI with a chart
 * update. A chart update is more expensive than a node update.
 * You may see no performance gains on a dataset this size, but
 * with some increase its possible to see a discrepancy for the
 * user. This is why I chose to contstruct the items outside
 * of the graph.
 */
/*zingchart.guide_mousemove = (e) => {
  document.getElementById('day').innerHTML = 'Day: ' + e['scale-label']['scale-x'];
}*/

/*********** Functions ***********/

/**
 * ZingChart defined event listener. Will capture ZoomEvent and related
 * Zooming Information.
 */
zingchart.zoom = (e) => {
  displayZoomValues(e.kmin, e.kmax);
}


/**
 * Apply dates to display current zoomed dates
 */
let displayZoomValues_word = (sFrom_word, sTo_word) => {
  let dateFrom_word = document.getElementById('date-from_word');
  let dateTo_word = document.getElementById('date-to_word');

  // If viewall is clicked show the default dates
  if (!sFrom_word) {
    sFrom_word = '00:00';
  }
  if (!sTo_word) {
    sTo_word = '00:00';
  }

  dateFrom_word.innerHTML = sFrom_word;
  dateTo_word.innerHTML = sTo_word;
}

/**
 * Apply zoom to graph.
 */
let zoomToIndex_word = (max) => {

  // ZingChart api automated zoom. Have to be careful
  // not to zoom past the end of the graph
  zingchart_word.exec('myChart_word', 'zoomto', {
    xmax: max,
    xmin: 0
  });
}

/**
 * Capture the spans clicks with data-period attribute.
*/
/*document.getElementById('date-picker-container').addEventListener('click', (e) => {
  let target = e.target;

  // Only capture spans with data-period attribute
  if (target.dataset['period']) {
    // Toggle classes
    removeActiveClass();
    e.target.classList.toggle('active');

    switch (target.dataset['period']) {
      case '1':
        zoomToIndex(30);
        break;
      case '2':
        zoomToIndex(60);
        break;
      default:
        zingchart.exec('myChart', 'viewall');
        break;
    }
  }
});*/

let removeActiveClass_word = () => {
  let activeElement_word = document.querySelector('[data-period].active');
  activeElement_word.classList.toggle('active');
}
