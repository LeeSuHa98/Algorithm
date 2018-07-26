#include <iostream>
#include<math.h>

using namespace std;

int main() {

	int t, i, x1, y1, r1, x2, y2, r2;

	cin >> t;

	for (; t > 0; t--) {

		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

		double i = sqrt(pow(x1 - x2, 2.0) + pow(y1 - y2, 2.0));

		if (x1 == x2&&y1 == y2) {

			if (r1 == r2)

				cout << "-1\n";

			else
				cout << "0\n";

		}

		else {

			if ((r1 + r2) > i&&abs(r1 - r2) < i)
				cout << "2\n";

			else if ((r1 + r2) == i || abs(r1 - r2) == i)
				cout << "1\n";

			else
				cout << "0\n";

		}

	}

	return 0;
}