#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <vector>
#include <chrono>

using std::vector;

int main()
{

  // Problem 2:
  int n = 100000; //The number of steps
  double k = 0.0;
  double step = 1./n; //Step length
  double x[n+1]; //Storing the x-values
  double u[n+1]; //Storing the true values of u in the x-points
  std::ofstream myfile;
  myfile.open("data.txt");

  //Add all the values to the vectors x and u.
  for(int i = 0; i <= n; i++){
    x[i] = k;
    k += step;
    u[i] = 1-(1-exp(-10))*x[i]-exp(-10*x[i]);
    std::cout.precision(4);
    myfile << std::scientific << x[i] << " " << std::scientific << u[i] << "\n";
  }
  myfile.close();


  //Problem 7
  double a[n-1]; //Stores the sub-diagonal values
  double b[n-1]; //Stores the main-diagonal values
  double c[n-1]; //Stores the super-diagonal values
  double g[n-1]; //Stores the g values for problem 7a
  double g_special[n-1]; //Stores the g values for problem 9b

  //Add all the necessary values to the arrays above
  for(int i=0; i<=n-2; i++){
    g[i] = 100*exp(-10*x[i+1])*pow(1./n,2);
    g_special[i] = 100*exp(-10*x[i+1])*pow(1./n,2);
    a[i] = -1;
    b[i] = 2;
    c[i] = -1;
  }

  auto t1 = std::chrono::high_resolution_clock::now();
  double b_update[n-1];
  b_update[0] = b[0];
  //Update the main-diagonal values and the g-values
  for(int i=1; i<=n-2; i++){
      b_update[i] = b[i] - (a[i]/b_update[i-1])*c[i];
      g[i] = g[i]-(a[i]/b_update[i-1])*g[i-1];
  }


  double v[n-1]; //Stores the approx solution
  v[n-2] = g[n-2]/b_update[n-2];
  myfile.open("approx_with_" + std::to_string(n) + "_xes.txt");
  myfile << std::scientific << x[n] << " " << std::scientific << 0 << "\n";
  myfile << std::scientific << x[n-1] << " " << std::scientific << v[n-2] << "\n";

  //Find all the approx solutions
  for(int i=n-3; i>=0; i--){
    v[i] = (g[i] - c[i]*v[i+1])/b_update[i];
    std::cout.precision(4);
    myfile << std::scientific << x[i+1] << " " << std::scientific << v[i] << "\n";
  }
  myfile << std::scientific << x[0] << " " << std::scientific << 0 << "\n";
  myfile.close();
  auto t2 = std::chrono::high_resolution_clock::now();
  double duration_seconds = std::chrono::duration<double>(t2 - t1).count();
  std::cout << "The general algorithm takes " << duration_seconds << " seconds for n=" << n << "\n";

  //Problem 9c
  auto t3 = std::chrono::high_resolution_clock::now();
  //Update the g-values
  for(int i=1; i<=n-2; i++){
    g_special[i] = g_special[i]+( (double) i/(i+1))*g_special[i-1];
  }

  //Does the same as problem 7a but with a slithly different algorithm
  double v_special[n-1];
  v_special[n-2] = ((double) (n-2)/(n-1)) * g_special[n-2];
  myfile.open("special_algo_" + std::to_string(n) + "_xes.txt");
  myfile << std::scientific << x[n] << " " << std::scientific << 0 << "\n";
  myfile << std::scientific << x[n-1] << " " << std::scientific << v_special[n-2] << "\n";
  for(int i=n-3; i>=0; i--){
    v_special[i] = (g_special[i]  + v_special[i+1])*((double) (i+1)/(i+2));

    std::cout.precision(4);
    myfile << std::scientific << x[i+1] << " " << std::scientific << v_special[i] << "\n";
  }
  myfile << std::scientific << x[0] << " " << std::scientific << 0 << "\n";
  myfile.close();
  auto t4 = std::chrono::high_resolution_clock::now();
  double duration_seconds_special = std::chrono::duration<double>(t4 - t3).count();
  std::cout << "The special algorithm takes " << duration_seconds_special << " seconds for n=" << n << "\n";






  return 0;
}



// reneaas
