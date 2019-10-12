/* 
this algorithm is from @1607-ÌÆÎ°Ïè 
*/

#include <cstdio>
#include <memory.h>
#include <algorithm>

int n, m, a[351], b[5], f[41][41][41][41];


int dp(int now, int n1, int n2, int n3, int n4)
{
	if(now == 1)
		return a[1];
	if(f[n1][n2][n3][n4])
		return f[n1][n2][n3][n4];
	int maxc = 0;
	if(n1 > 0) maxc = std::max(maxc, a[now] + dp(now-1, n1 - 1, n2, n3, n4));
	if(n2 > 0) maxc = std::max(maxc, a[now] + dp(now-2, n1, n2 - 2, n3, n4));
	if(n3 > 0) maxc = std::max(maxc, a[now] + dp(now-3, n1, n2, n3 - 3, n4));
	if(n4 > 0) maxc = std::max(maxc, a[now] + dp(now-4, n1, n2, n3, n4 - 4));
	f[n1][n2][n3][n4] = maxc;
	return maxc;
}


int main()
{

	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	memset(f, 0, sizeof(f));
	scanf("%d %d", &n, &m);
	for(int i = 1; i <= n; i ++)
		scanf("%d",&a[i]);
	for(int temp, i = 1; i <= m; i ++)
	{
		scanf("%d", &temp);
		b[temp] ++;
	}
	
	printf("%d", dp(n, b[1], b[2], b[3], b[4]));
}
	
