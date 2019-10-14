#include <cstdio>
#include <queue>
#include <string.h>
using namespace std;
int sx, sy, fx, fy, n, m, paths = 0;
int map[11][11]; 
int vis[11][11];
int mov[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};

typedef struct
{
	int x, y;
}Node;
queue<Node> q;




void dfs(int nx, int ny)
{

	if(nx == fx && ny == fy)
	{
		paths ++;
		return;
	}
	
	for(int i = 0; i < 4; i ++)
		{
			int tx = nx + mov[i][0];
			int ty = ny + mov[i][1];
			if(tx>=1&&tx<=m&&ty>=1&&ty<=n&&!map[tx][ty]&&!vis[tx][ty])    //&&(a[tx][ty]!=a[now.x][now.y]) 然并卵的判断 
			{
				vis[tx][ty] = 1;
				dfs(tx,ty);
				vis[tx][ty] = 0;
			}
		}
}
		





void bfs()
{
	q.push({sx,sy});
	vis[sx][sy] = 1;

	while(!q.empty())
	{
		Node now = q.front(); 
		q.pop();
		for(int i = 0; i < 4; i ++)
		{
			int tx = now.x + mov[i][0];
			int ty = now.y + mov[i][1];
			if(tx>=1&&tx<=m&&ty>=1&&ty<=n&&!map[tx][ty]&&!vis[tx][ty])   //&&(a[tx][ty]!=a[now.x][now.y]) 然并卵的判断 
			{ 
				q.push({tx,ty});
				vis[tx][ty] = vis[now.x][now.y] + 1;
			}
		}
	}
	printf("%d\n ", vis[fx][fy]);
	/*for(int i = 1; i <= n; i ++)
	{
		for(int j = 1; j <= m; j ++)
			printf("%d,%d:%d ", j,i,vis[j][i]);
		printf("\n");
	}
	printf("%d", vis[5][6]);*/
}



int main()
{
	memset(map, 1, sizeof(map));
	memset(vis, 0, sizeof(vis));
	
	scanf("%d %d", &m, &n);  //m 为行数，n 为列数 
	scanf("%d %d", &sx, &sy);
	scanf("%d %d", &fx, &fy);
	for(int i = 1; i <= m; i ++)
		for(int j = 1; j <= n; j ++)
			scanf("%d", &map[i][j]);  //  地图的第一个参数为行号， 第二个为列号！ 


	dfs(sx,sy);
	printf("%d\n",  paths);
	memset(vis, 0, sizeof(vis));
	if(paths != 0)
		bfs();
	else
		printf("0\n");
	
	

	
}
	 
