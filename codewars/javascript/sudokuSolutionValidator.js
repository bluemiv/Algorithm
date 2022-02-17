// https://www.codewars.com/kata/529bf0e9bdf7657179000008

const getAllCase = (board) => {
  const columns = [[], [], [], [], [], [], [], [], []];
  const subGrids = [[], [], [], [], [], [], [], [], []];
  
  board.forEach((row, i) => row.forEach((column, j) => {
    subGrids[parseInt(i / 3) * 3 + parseInt(j / 3)].push(column); // sub-grids
    columns[j].push(column); // columns
  }));
  return [board, columns, subGrids];
}

const isValidDigit = (row) => {
  const oneToNine = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9]);
  const rowSet = new Set(row);
  if (rowSet.size !== 9) return false;
  
  let isValid = true;
  rowSet.forEach(c => {
    if(!isValid) return;
    isValid = oneToNine.has(c);
  })
  return isValid;
}

function validSolution(board) {
  const [rows, columns, subGrids] = getAllCase(board);

  return [
    ...rows,
    ...columns,
    ...subGrids,
  ].reduce((result, e) => {
    if (!result) return false;
    return isValidDigit(e);
  }, true);
}
