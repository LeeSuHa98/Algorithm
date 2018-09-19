#include <iostream>

using namespace std;

int main()
{
	double  x, y;
	double result;

	cin >> x >> y;

	result = x / y;

	cout << fixed;
	cout.precision(15);

	cout << result;

	return 0;
}