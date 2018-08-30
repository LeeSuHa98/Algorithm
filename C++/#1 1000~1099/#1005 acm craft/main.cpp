#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T; //�׽�Ʈ Ƚ��

	cin >> T;

	for (int i = 0; i < T; i++) // �׽�Ʈ Ƚ����ŭ �ݺ�
	{
		int N; //�ǹ� ��
		int K; //�ǹ�������Ģ 
		int W; //�ǹ���ȣ

		int time[1000]; //�Ǽ� �ð�
		int pre[1000] = { 0 }; // ������ ����
		vector<int> post[1000]; //������ ���

		cin >> N >> K;
		for (int j = 0; j < N; j++)
		{
			cin >> time[j];
		}
		for (int s = 0; s < K; s++)
		{
			int X, Y; //�Ǽ� ����
			cin >> X >> Y;
			post[X - 1].push_back(Y - 1); // X��� �����ڿ� Y �����ڸ� �߰�
			pre[Y - 1]++;//������ �߰�
		}
		cin >> W; //�Ǽ��� �ǹ� ��ȣ
		W--; // ��ȣ �������� �� �ð� Ȯ�� ����

		int result[1000] = { 0 }; //�ǹ��� ¢�µ� �ɸ��� �ּ� �ð�
		queue<int> Q; //ť ����

		for (int a = 0; a < N; a++)
		{
			if (pre[a] == NULL)
			{
				Q.push(a); // �����ڰ� ���� �ǹ� ��ȣ push
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