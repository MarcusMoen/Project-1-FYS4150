// Look, our first C++ program!

#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>

int main()
{
  // Print a message to screen
  int n = 101;
  double k = 0.0;
  double x[n];
  double u[n];
  std::ofstream myfile;
  myfile.open("data.txt");
  for(int i = 0; i < n; i++){
    x[i] = k;
    k += 1./n;
    u[i] = 1-(1-exp(-10))*x[i]-exp(-10*x[i]);
    std::cout << k;
    std::cout << std::setprecision(4) << u[i] << "\n";
    myfile << std::setprecision(4) << x[i] << " " << std::setprecision(4) << u[i] << "\n";
  }
  myfile.close();

  return 0;
}
