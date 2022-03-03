// https://www.codewars.com/kata/5765870e190b1472ec0022a2/javascript

class Node {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
}

const invalidValue = (x, y, n) => {
  return x < 0 || x > n-1 || y < 0 || y > n-1;
}

const bfs = (x, y, n, graph, visited) => {
  const queue = [];
  const directions = [[-1, 0], [0, -1], [1, 0], [0, 1]];
  let isResult = false;
  
  const firstNode = new Node(x, y);
  visited[x][y] = true;
  
  queue.push(firstNode);
  while(queue.length > 0) {
    const curNode = queue.pop();
    directions.forEach(dir => {
      const [newX, newY] = [curNode.x + dir[0], curNode.y + dir[1]];
        
      if(newX === n-1 && newY === n-1) {
        isResult = true;
        return;
      }

      if(
        !invalidValue(newX, newY, n) // 올바른 배열 범위이어야 함
        && graph[newX][newY] // '벽'이 아니어야 함
        && !visited[newX][newY] // 방문안했어야 함
      ) {  
        visited[newX][newY] = true;
        const nextNode = new Node(newX, newY);
        queue.push(nextNode);        
      }
    })
  }
  return isResult;
}

const makeGraph = (maze) => {
  return maze.split('\n').map(row => row.split('').map(e => e === '.'))
}

const initVisited = (n) => {
  return new Array(n).fill(0).map(e => new Array(n).fill(false));
}

function pathFinder(maze){
  // 그래프 생성
  const graph = makeGraph(maze);
  const n = graph.length;
  
  // 노드를 방문했는지 확인하는 flag 값
  const visited = initVisited(n);
  
  const result = bfs(0, 0, n, graph, visited);
  return result;
}
