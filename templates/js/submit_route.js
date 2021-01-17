function mySubmit() {
  var out = new Array();
  var k = 0;
  for (i = 0; i < rows; i++) {
      for (j = 0; j < cols; j++) {
          if (isSelected[i][j] == true) {
              temp = new Array(i,j)
              k = k+1;
              out.push(temp);
          }
      }
  }

  var res = JSON.stringify(out);
  document.getElementById('holds').value = res;
}