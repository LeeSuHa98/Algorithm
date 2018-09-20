#include <iostream>
#include <cmath>

using namespace std;

int A; // ¹Ø
int B; //Áö¼ö

int Distribute()
{
	int Bis10 = A % 10;
	//10ÀÇ °öÀº Ç×»ó 10
	if (!Bis10)
		return 10;
	else if (B == 1)
		return A;
	else if (A == 1 || A == 5 || A == 6) 
		return A;
	else if (A == 4 || A == 9)
	{
		if (!B % 2)
			return A == 4 ? 6 : 1;
		else
			return A;
	}
	else
	{
		B %= 4;
		if (!B)
			return (int)pow(A, 4) % 10;
		else
			return (int)pow(A, B) % 10;
	}
}
int main()
{
	int test_case;
	cin >> test_case;

	for (int i = 1; i <= test_case; i++)
	{
		cin >> A >> B;
		cout << Distribute() << endl;
	}
	return 0;
}