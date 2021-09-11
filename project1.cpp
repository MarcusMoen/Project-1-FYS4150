#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <vector>

using std::vector;

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


  //Problem 7
  double a[n-2];
  double b[n-2];
  double c[n-2];
  double g[n-2];
  for(int i=0; i<=n-3; i++){
    g[i] = 100*exp(-10*x[i+1])*pow(1./n,2);
    a[i] = -1;
    b[i] = 2;
    c[i] = -1;
    //std::cout << i << ' ' << g[i] << ' ' << x[i] << "\n";
  }

  double b_update[n-2];
  b_update[0] = b[0];
  for(int i=1; i<=n-3; i++){
      b_update[i] = b[i] - (a[i]/b_update[i-1])*c[i];
      g[i] = g[i]-(a[i]/b_update[i-1])*g[i-1];
      //std::cout << 'g' << ' ' << mat[i][i-1] << ' ' << g[i] << ' ' << "Dette er g" << ' ' << g[i] << "\n";
  }


  double v[n-2];
  v[n-3] = g[n-3]/b_update[n-3];
  myfile.open("approx_with_" + std::to_string(n) + "_xes.txt");
  myfile << std::scientific << x[n-1] << " " << std::scientific << 0 << "\n";
  myfile << std::scientific << x[n-2] << " " << std::scientific << v[n-3] << "\n";
  for(int i=n-4; i>=0; i--){
    v[i] = (g[i] - c[i]*v[i+1])/b_update[i];
    //std::cout << "b tilda" << ' ' << A_new[i][i] << '\n';
    std::cout << "v_i+1" << ' ' << v[i+1] << '\n';
    std::cout << "g tilda" << ' ' << g[i] << '\n';


    std::cout.precision(4);
    myfile << std::scientific << x[i+1] << " " << std::scientific << v[i] << "\n";
    std::cout << i << ' ' << v[i] << "\n";
  }
  myfile << std::scientific << x[0] << " " << std::scientific << 0 << "\n";

  std::cout << v[2];
  std::cout << '\n';
  std::cout << u[3];
  std::cout << '\n';


  //Problem 9b




  return 0;
}



// reneaas
