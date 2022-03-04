// https://www.codewars.com/kata/57658bfa28ed87ecfa00058a/javascript

function pathFinder(maze){
  const dir = [[-1, 0], [0, -1], [1, 0], [0, 1]];
  
  const g = maze.split('\n').map(r => r.split(''));
  const n = g.length;
  const cnt = Array(n).fill(0).map(_ => Array(n).fill(-1));
  
  const q = [];
  q.push({ x: 0, y: 0 });
  cnt[0][0] = 0;
  
  while(q.length > 0) {
    const node = q.pop();
    
    for(let i=0; i < dir.length; i++) {
      const [nx, ny] = [node.x + dir[i][0], node.y + dir[i][1]];
      const nCnt = cnt[node.x][node.y] + 1;
      
      if((nx >= 0 && nx <= n-1 && ny >= 0 && ny <= n-1) && g[nx][ny] === '.' && (cnt[nx][ny] === -1 || cnt[nx][ny] > cnt[node.x][node.y] + 1)) {
        q.push({ x: nx, y: ny });
        cnt[nx][ny] = nCnt;
      }
    }
  }

  return cnt[n-1][n-1] === -1 ? false : cnt[n-1][n-1];
}
