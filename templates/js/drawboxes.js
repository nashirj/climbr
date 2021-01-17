function drawBoxes() {
  c.beginPath();
  for (var row = 0; row < rows; row++) {
    for (var col = 0; col < cols; col++) {
      drawBox(row, col, 'gray', 2);
    }
  }
  c.closePath();
}

function drawBox(row, col, color, lineWidth) {
  c.strokeStyle = color;
  c.lineWidth = lineWidth;
  c.strokeRect(col * boxWidth, row * boxHeight, boxWidth, boxHeight);
}

const corners = 
[[-1,-1],[-1, 0],[-1, 1],
 [ 0,-1],        [ 0, 1], 
 [ 1,-1],[ 1, 0],[ 1, 1]];

function reDrawNeighbors(row, col) {
  if (!isOnMap(row, col)) {
    console.log("not on map")
    return;
  }
  for (const corner of corners) {
    var _row = row + corner[0], _col = col + corner[1];
    if (isOnMap(_row, _col) && isSelected[_row][_col]) {
      drawBox(_row, _col, 'black', 1);
    }
  }
}

function isOnMap(row, col) {
    return row >= 0 && col >= 0 && col < cols && row < rows;
}

function scaleClickCoordinates(e) {
  var x = e.offsetX * (canvas.width / e.target.clientWidth);
  var y = e.offsetY * (canvas.height / e.target.clientHeight);
  const targ = e.originalTarget;

  return [x, y]
}

function handleClick(e) {

  var coords = scaleClickCoordinates(e);
  var x = coords[0], y = coords[1];
  
  var row = Math.floor(y / boxHeight);
  var col = Math.floor(x / boxWidth);
  if (!isOnMap(row, col)) {
    console.log("row and col are out of bounds, not handling click")
  }
  c.beginPath();
  
  console.log(isSelected[row][col])
  if (isSelected[row][col]) {
    drawBox(row, col, 'gray', 2);
    reDrawNeighbors(row,col);
  } else {
    drawBox(row, col, 'black', 1);
  }
  
  isSelected[row][col] = !isSelected[row][col]
}