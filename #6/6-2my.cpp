#include <cstdio>
#include <memory.h>
#include <algorithm>

int n, m, start,a[351], b[5], dp[41][41][41][41];

int main()
{

	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	memset(dp, 0, sizeof(dp));
	scanf_s("%d %d", &n, &m);
	scanf_s("%d", &start);
	for (int i = 1; i <= n-1; i++)
		scanf_s("%d", &a[i]);
	for (int temp, i = 1; i <= m; i++)
	{
		scanf_s("%d", &temp);
		b[temp] ++;
	}
	int maxc = 0;
	dp[0][0][0][0] = start;
	for (int w = 0; w <= b[1]; w++)
		for (int x = 0; x <= b[2]; x++)
			for (int y = 0; y <= b[3]; y++)
				for (int z = 0; z <= b[4]; z++)
				{
					maxc = 0;
					if (w != 0)
						maxc = std::max(maxc, dp[w - 1][x][y][z] + a[w + x * 2 + y * 3 + z * 4]);
					if (x != 0)
						maxc = std::max(maxc, dp[w][x - 1][y][z] + a[w + x * 2 + y * 3 + z * 4]);
					if (y != 0)
						maxc = std::max(maxc, dp[w][x][y - 1][z] + a[w + x * 2 + y * 3 + z * 4]);
					if (z != 0)
						maxc = std::max(maxc, dp[w][x][y][z - 1] + a[w + x * 2 + y * 3 + z * 4]);
					dp[w][x][y][z] = maxc;
				}
	for (int w = 0; w <= b[1]; w++)
		for (int x = 0; x <= b[2]; x++)
			for (int y = 0; y <= b[3]; y++)
				for (int z = 0; z <= b[4]; z++)
					printf("%d %d %d %d %d\n",w,x,y,z, dp[w][x][y][z]);

	printf("%d", dp[b[1]][b[2]][b[3]][b[4]]);
	return 0;
}


