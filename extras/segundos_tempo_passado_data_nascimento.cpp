/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/


#include <iostream> // para: cout
#include <time.h>   // para: time()
#include <unistd.h>
#include <stdlib.h>



using std::cout;
using std::cin;


int main ( )
{
    int ano;
    int dia;
    int mes;
  time_t tempo_real;
  time_t timer;
  time_t seconds;
  int numero;
  cout << "digite o dia [1-31] do seu nascimento: ";
  cin >> dia;
  cout << "digite o mes [0-11] do seu nascimento: ";
  cin >> mes;
  cout << "digite o ano do seu nascimento: ";
  cin >> ano;
    struct tm y2k = {0};
    //1900
    int dif_ano = ano - 1900;
      y2k.tm_hour = 0;   y2k.tm_min = 0; y2k.tm_sec = 0;
  y2k.tm_year  = dif_ano; y2k.tm_mon = mes; y2k.tm_mday = dia;
   /* get current time; same as: timer = time(NULL)  */

  time(&timer);
  tempo_real = time( (time_t *) 0);  // apontando o ponteiro para null.
  cout << "Ja se passaram  " << tempo_real << " segundos desde 0:00:00 de 01/01/1970 " << '\n';
  cout << "Ja se passaram  " << timer << " segundos desde 0:00:00 de 01/01/1970 " << '\n';
  cout << "Ja se passaram  " << mktime(&y2k) << " segundos desde 0:00:00 de 01/01/1970 até " << dia << "/" << mes+1 << "/" << ano << '\n';
  
  
  
  seconds = difftime(timer, mktime(&y2k));
  cout << "Ja se passaram  " << seconds << " segundos desde do seu nascimento " << '\n';

  exit(0);
}
