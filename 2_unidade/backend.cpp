
#include <iostream>
#include <signal.h> // definição dos sinais de interrupções
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h> // system()
#include <string>		// Necessário para usar strings

using namespace std;

int options;
string filter;
int pid_vitima;

int function_kill(int pid){
  kill(pid, SIGKILL);
  cout  << "\nprocesso morto!.\n";
  return pid;
};

int function_suspem(int pid){
  kill(pid, SIGSTOP);
  cout << "\nprocesso suspenso!.\n";
  return pid;
};

int function_return(int pid){
  kill(pid, SIGCONT);
  cout <<"\nprocesso continuado!.\n";
  return pid;
};
void function_filter(string filter){
  cout << filter;
  string text = "ps -aux | grep ";
  text += filter;
  system(text.c_str());
  cout << "\nprocesso continuado!.\n";
};



int main()
{
  while(1){
    // cout << 'Digite opção a qual deseja realizar:' >> endl;
    cout << "Digite opção a qual deseja realizar: \n";
    cout << "Digite 1 para matar o processo\n";
    cout << "Digite 2 para suspender o processo\n";
    cout << "Digite 3 para continuar o processo\n";
    cout << "Digite 4 para filtrar pelo nome\n";
    cout << "==================================\n";
    cin >> options;
    switch (options)
    {
    case 1:
      printf( "Digite o PID do processo que deve morrer: ");
      cin >> pid_vitima;
      function_kill(pid_vitima);
      break;
    
    case 2:
      printf( "Digite o PID do processo que deve ser suspenso: ");
      cin >> pid_vitima;
      function_suspem(pid_vitima);
      break;
    case 3:
      printf( "Digite o PID do processo que deve continuar: ");
      cin >> pid_vitima;
      function_return(pid_vitima);
      break;
    case 4:
      printf( "Digite o nome do processo para filtrar: ");
      cin >> filter;
      function_filter(filter);
      break;
    
    default:
      exit(0); 
      break;
    }
    if (options == 0){
      break;
    }
  }
  exit(0);  
}