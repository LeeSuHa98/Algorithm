#include <iostream>
#include <cmath>

using namespace std;

double point_distance(double x1, double y1, double x2, double y2);

int main() 
{
	double x1, y1, x2, y2;
	double cx, cy, r;
	int planet;
	int count;
	int t;
	double distance_start, distance_end;

	cin >> count;

	while(count > 0)
	{
		cin >> x1 >> y1 >> x2 >> y2;
		cin >> planet;
		t = 0;

		while(planet > 0)
		{
			cin >> cx >> cy >> r;
			distance_start = point_distance(x1, y1, cx, cy);
			distance_end = point_distance(x2, y2, cx, cy);

			if (distance_start < r && distance_end > r)
			{
				t++;
			}
			else if (distance_start > r && distance_end < r)
			{
				t++;
			}
			planet--;
		}
		cout << t << endl;
		count--;
	}

	return 0;
}

double point_distance(double x1, double y1, double x2, double y2)
{
	double distance = 0;
	distance = sqrt(pow(x1 - x2, 2.0) + pow(y1 - y2, 2.0));
	return distance;
}