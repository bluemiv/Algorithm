const getColumnsAndSubGrids = (board) => {
  const columns = Array.from({ length: 9 }, () => []);
  const subGrids = Array.from({ length: 9 }, () => []);
  
  board.forEach((row, i) => row.forEach((column, j) => {
    // Put sub-grids
    const curIdx = parseInt(i / 3) * 3 + parseInt(j / 3);
    subGrids[curIdx].push(column);

    // Put columns
    columns[j].push(column);
  }));
  return [columns, subGrids];
}

const isValidDigit = (row) => {
  const oneToNine = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9]);
  const rowSet = new Set(row);
  if (rowSet.size !== 9) return false;
  
  let isValid = true;
  rowSet.forEach(c => {
    isValid = oneToNine.has(c);
  })
  return isValid;
}

function validSolution(board) {
  const rows = board;
  const [columns, subGrids] = getColumnsAndSubGrids(board);
  
  return rows
    .concat(columns)
    .concat(subGrids)
    .reduce((result, e) => {
      if (!result) return false;
      return isValidDigit(e);
    }, true);
}
