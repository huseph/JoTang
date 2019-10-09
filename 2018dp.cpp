#include <cstdio>
#include <algorithm>

int main()
{
	int n1, n2, mon, year, d, stock[41][2];
	
	scanf("%d",&n1);      //��С���� 
	for(int i = 1; i <= n1; i ++)
	{

		scanf("%d %d", &mon, &year);      //monΪ�����֧���� 
		scanf("%d", &n2);    //n2Ϊ��Ʊ���� 
		for(int j = 1, temp; j <= n2; j ++)
		{
			scanf("%d %d", &temp, &stock[j][1]);
			stock[j][0] = temp / 1000;
		}
			
		for(int j = 1; j <= year; j ++)
		{
			int dp[46000] = {0};
			int temp = mon / 1000, maxx = 0;
			for(int x = 1; x <= n2; x ++)
				for(int y = stock[x][0]; y <= temp; y ++)
				{
					dp[y] = std::max(dp[y-stock[x][0]] + stock[x][1], dp[y]);

				}
			for(int x = 0; x <= mon; x ++)
				maxx = std::max(maxx, dp[x]);
			mon += maxx;
			 
		}
		printf("%d", mon);
	}
	return 0;
}
	
