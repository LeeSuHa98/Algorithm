#include <iostream>

using namespace std;

static int MAX_SIZE[41] = { 0 };

int fibo(int n)
{
	if (MAX_SIZE[n] > 0)
	{
		return MAX_SIZE[n];
	}
	if (n == 0)
	{
		return 0;
	}
	else if (n == 1 || n == 2)
	{
		return 1;
	}
	else
	{
		return MAX_SIZE[n] = fibo(n - 1) + fibo(n - 2);
	}
}

int main() 
{
	int T, N;

	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		cin >> N;
		if (N == 0)
			cout << "1 0" << endl;
		else
			cout << fibo(N - 1) << " " << fibo(N) << endl;
	}

	return 0;
}