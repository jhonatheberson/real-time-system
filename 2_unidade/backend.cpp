
#include <iostream>
#include <signal.h> // definição dos sinais de interrupções
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h> // system()
#include <string>		// Necessário para usar strings
#include <sys/time.h>     // getpriority(int which, int who)  setpriority(int which, int who, int prio);
#include <sys/resource.h>
// #define _GNU_SOURCE
#include <sched.h>   // para alocar CPU

using namespace std;

int options;
string filter;
int pid_vitima;
int cpu;
cpu_set_t  mask;


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
void function_aloc_cpu(int cpu,int pid){
  CPU_ZERO(&mask);
  CPU_SET(cpu-1, &mask);    // alocar na CPU 0
  int result = sched_setaffinity(pid, sizeof(mask), &mask);  // 0 --> Aqui é no próprio processo. No Geral deve ser o PID
  cout << "\nprocesso com o PID: " << pid << ",foi alocado na segunite cpu: " << cpu << "\n\n";
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
    cout << "Digite 5 para alocarum programa ao CPU definida\n";
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
    case 5:
      printf( "Digite qual CPU você que alocar o programa: ");
      cin >> cpu;
      printf( "Digite qual PID do processo que você quer alocar a CPU: ");
      cin >> pid_vitima;
      function_aloc_cpu(cpu, pid_vitima);
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