#include <signal.h> // definição dos sinais de interrupções
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h> // system()
#include <iostream>

/* 
14 - primeiro filho
16 - segundo filho
26 - primeiro neto
30 - segundo neto
38 - primeiro neto morreu
44 - primeiro filho morreu
46 - segundo filho morreu
48 - segundo neto morreu
60 - pai morreu
*/
using namespace std;

int main()
{
  int pid = fork(); // fork para o filho 1

  if (pid == -1)
  {
    exit(1);
  }

  if (pid == 0)
  {
    //filho 1
    sleep(14);
    int pid3 = fork();
    if (pid3 == -1)
    {
      exit(1);
    }
    if (pid3 == 0)
    {
      //neto primeiro filho;
      sleep(12);
      cout << "neto primeiro filho nasce" << endl;
      sleep(12);
      cout << "primeiro neto morreu" << endl;
    }
    else
    {
      cout << "filho 1 nasce" << endl;
      sleep(30);
      cout << "primeiro filho morreu" << endl;
    }
  }
  else
  {
    int pid2 = fork(); // fork para o filho 2

    if (pid2 == -1)
    {
      exit(1);
    }

    if (pid2 == 0)
    {
      //filho 2
      sleep(16);

      int pid4 = fork(); //fork prara criar segundo neto;

      if (pid4 == -1)
      {
        exit(1);
      }
      if (pid4 == 0)
      {
        //neto segundo filho;
        sleep(14);
        cout << "neto segundo filho nasce" << endl;
        sleep(18);
        cout << "segundo neto morreu" << endl;
      }
      else
      {
        cout << "filho 2 nasce" << endl;
        sleep(30);
        cout << "segundo filho morreu" << endl;
      }
    }
    else
    {
      //pai
      sleep(60);
      cout << "pai morreu!" << endl;
    }
  }
}