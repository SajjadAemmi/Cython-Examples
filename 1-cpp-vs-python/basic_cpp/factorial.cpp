#include <iostream>
#include <chrono>

using namespace std;

int factorial(int n)
{
    int result = 1;
    for (int i = 1; i <= n; ++i)
    {
        result *= i;
    }
    return result;
}

void calculate_factorial_in_cpp()
{
    int test_values[] = {20, 200, 2000, 20000, 200000};
    cout << "C++ Results:" << endl;
    for (int n : test_values)
    {
        auto start_time = chrono::high_resolution_clock::now();
        int fact = factorial(n);
        auto end_time = chrono::high_resolution_clock::now();
        chrono::duration<double> elapsed_time = end_time - start_time;
        cout << "Factorial(" << n << "): " << elapsed_time.count() << " seconds" << endl;
    }
}

int main()
{
    calculate_factorial_in_cpp();
    return 0;
}
