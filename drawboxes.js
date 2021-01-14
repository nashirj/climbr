var canvas = document.getElementById("canvas"),
    ctx = canvas.getContext("2d");



var background = new Image();
background.src = "https://imgur.com/EvWLWZl.png";

background.onload = function(){
    ctx.drawImage(background,0,0);   
    console.log(this.width + 'x' + this.height);
    drawBoxes();
}


canvas.width = background.width;
canvas.height = background.height;

var canvas = document.getElementById("canvas"),
    c = canvas.getContext("2d"),
    boxHeight = canvas.height/20,
    boxWidth = canvas.width/16,
    rows = 20,
    cols = 16;
canvas.addEventListener('click', handleClick);

var isSelected = new Array();
for(var i = 0; i <= rows; i++)
{
    isSelected[i] = new Array();
    for(var j = 0; j <= cols; j++)
        isSelected[i].push(false);
}

console.log(isSelected)

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
	// todo: redraw neighbors for canvas to all adjacent cells if they are selected
  if (!isOnMap(row, col)) {
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

function handleClick(e) {
  var row = Math.floor(e.offsetY / boxHeight);
	var col = Math.floor(e.offsetX / boxWidth);
  console.log(row, col)
  c.beginPath();
  
  if (isSelected[row][col]) {
  	drawBox(row, col, 'gray', 2);
    reDrawNeighbors(row,col);
  } else {
  	drawBox(row, col, 'black', 1);
  }
  
  isSelected[row][col] = !isSelected[row][col]
  console.log(isSelected[row][col])
}