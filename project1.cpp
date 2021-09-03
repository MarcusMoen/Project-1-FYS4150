// Look, our first C++ program!

#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>

int main()
{
  // Print a message to screen

  // Problem 2:
  int n = 100;
  double k = 0.0;
  double x[n];
  double u[n];
  std::ofstream myfile;
  myfile.open("data.txt");
  for(int i = 0; i <= n; i++){
    x[i] = k;
    k += 1./n;
    u[i] = 1-(1-exp(-10))*x[i]-exp(-10*x[i]);
    std::cout.precision(4);
    myfile << std::scientific << x[i] << " " << std::scientific << u[i] << "\n";
  }
  myfile.close();


  //Problem x:

  return 0;
}
