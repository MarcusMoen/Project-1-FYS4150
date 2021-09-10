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


  //Problem 6a:
  //Need to define a first matrix mat

  double mat[n-2][n-2];

  double g[n-2];
  for(int i=0; i<=n-3; i++){
    for(int j=0; j<=n-3; j++){
      if(i==j){
        mat[i][j] = 2;
      }
      else if(i==j-1){
        mat[i][j] = -1;
      }
      else if(i==j+1){
        mat[i][j] = -1;
      }
    }
    g[i] = 100*exp(-10*x[i+1])*pow(1./n,2);
    //std::cout << i << ' ' << g[i] << ' ' << x[i] << "\n";
  }

  double A_new[n-2][n-2];
  A_new[0][0] = mat[0][0];
  for(int i=1; i<=n-3; i++){
    for(int j=1; j<=n-3; j++){
      if(i<n-2 && j==i+1){
        A_new[i][j] = mat[i][j];
      }
      else if(i==j){
        A_new[i][j] = mat[i][j]-(mat[i-1][j]/A_new[i-1][j-1])*mat[i][j-1];
        std::cout << 'A'  << ' '<< i << ' ' << j << ' '<< A_new[i][j] << "\n";}
    }
      g[i] = g[i]-(mat[i][i-1]/A_new[i-1][i-1])*g[i-1];
      std::cout << 'g' << ' ' << mat[i][i-1] << ' ' << g[i] << ' ' << "Dette er g" << ' ' << g[i] << "\n";
  }


  double v[n-2];
  myfile.open("test.txt");
  for(int i=n-3; i>=0; i--){
    if(i==n-3){
      v[i] = g[i]/A_new[i][i];
    }
    else{
      v[i] = (g[i] - A_new[i][i+1]*v[i+1])/A_new[i][i];
      std::cout << "b tilda" << ' ' << A_new[i][i] << '\n';
      std::cout << "v_i+1" << ' ' << v[i+1] << '\n';
      std::cout << "g tilda" << ' ' << g[i] << '\n';
    }

    std::cout.precision(4);
    myfile << std::scientific << x[i+1] << " " << std::scientific << v[i] << "\n";
    std::cout << i << ' ' << v[i] << "\n";
  }

  std::cout << v[2];
  std::cout << '\n';
  std::cout << u[3];
  std::cout << '\n';


  return 0;
}



// reneaas
