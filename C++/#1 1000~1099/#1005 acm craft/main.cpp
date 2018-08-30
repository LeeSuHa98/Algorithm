#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T; //테스트 횟수

	cin >> T;

	for (int i = 0; i < T; i++) // 테스트 횟수만큼 반복
	{
		int N; //건물 수
		int K; //건물순서규칙 
		int W; //건물번호

		int time[1000]; //건설 시간
		int pre[1000] = { 0 }; // 후행자 갯수
		vector<int> post[1000]; //선행자 목록

		cin >> N >> K;
		for (int j = 0; j < N; j++)
		{
			cin >> time[j];
		}
		for (int s = 0; s < K; s++)
		{
			int X, Y; //건설 순서
			cin >> X >> Y;
			post[X - 1].push_back(Y - 1); // X라는 선행자에 Y 후행자를 추가
			pre[Y - 1]++;//후행자 추가
		}
		cin >> W; //건설할 건물 번호
		W--; // 번호 직전까지 총 시간 확인 위함

		int result[1000] = { 0 }; //건물을 짖는데 걸리는 최소 시간
		queue<int> Q; //큐 선언

		for (int a = 0; a < N; a++)
		{
			if (pre[a] == NULL)
			{
				Q.push(a); // 선행자가 없는 건물 번호 push
			}
		}
		while (pre[W] > 0)
		{
			int u = Q.front();
			Q.pop();

			for (int next : post[u])
			{
				result[next] = max(result[next], result[u] + time[u]);
				if (--pre[next] == 0)
					Q.push(next);
			}
		}
		cout << result[W] + time[W] << endl;
	}
	return 0;
}