// https://www.codewars.com/kata/5765870e190b1472ec0022a2/javascript

const dir = [[-1, 0], [0, -1], [1, 0], [0, 1]];

class Node {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
}

const bfs = (x, y, n, graph, visited) => {
  const queue = [];

  queue.push(new Node(x, y));
  visited[x][y] = true;
  
  while(queue.length > 0) {
    const curNode = queue.pop();

    for(let i = 0; i < dir.length; i++) {
     const [newX, newY] = [curNode.x + dir[i][0], curNode.y + dir[i][1]];
        
      if(newX === n - 1 && newY === n - 1) return true;

      if(!(newX < 0 || newX > n-1 || newY < 0 || newY > n - 1) && graph[newX][newY] && !visited[newX][newY]) {
        queue.push(new Node(newX, newY));
        visited[newX][newY] = true; 
      } 
    }
  }
  
  return false;
}

function pathFinder(maze){
  const graph = maze.split('\n').map(row => row.split('').map(e => e === '.'));
  const n = graph.length;
  const visited = new Array(n).fill(0).map(_ => new Array(n).fill(false));
  
  return bfs(0, 0, n, graph, visited);
}
