/*
 *  ordenacao.cpp
 *  
 *
 *  Created by Luiz Affonso Guedes on 06/03/17.
 *  Copyright 2011 __MyCompanyName__. All rights reserved.
 *
 */

// UFRN-CT-DCA
// Programa: programa para ordenação de um vetor

// Manipulação de tempo em c,c++
// Programa: programa que usa manipuladores de tempo para 
// medir o desempenho de algoritmos de ordenação


#include <cstdlib>   //qsort
#include  <time.h>   // clock(),time()
#include <stdio.h>   // printf()
#include <stdlib.h>  // exit()
#include <fstream>
#include <iostream>

using namespace std;



//Vetores usados pelos métodos de ordenação
int *vetorQuickSort;
int *vetorBubbleSort;
int tamanho;





//Função usada pelo qsort para comparar dois numeros
int compare_ints( const void* a, const void* b ) {
	int* arg1 = (int*) a;
	int* arg2 = (int*) b;
	if( *arg1 < *arg2 ) return -1;
	else if( *arg1 == *arg2 ) return 0;
	else return 1;
}

//Algoritmos de ordenação bubble sort
void bubbleSort(int *vetor, int tamanho) {
	int aux;
	for (int i = 0; i < tamanho-1; i++) {
		for (int j = 0; j < tamanho-1; j++) {
			if (vetor[j] > vetor[j+1]) {
				aux = vetor[j];
				vetor[j] = vetor[j+1];
				vetor[j+1] = aux;
			}
		}
	}
}


//Observe que os números são gerados aleatoriamente baseados
//em uma semente. Se for passado a mesma semente, os 
//números aleatórios serão os mesmos
void criarVetor(int tamanhoVetor, int semente){
	srand (semente);
	vetorQuickSort = new int[tamanhoVetor];
	vetorBubbleSort = new int[tamanhoVetor];
	for (int i=0;i<tamanhoVetor;i++){
		vetorQuickSort[i] =  rand()%100000;
        vetorBubbleSort[i] = vetorQuickSort[i]; // utilizar os mesmos valores
		//vetorBubbleSort[i] = rand()%100000;
	}
}



int main ()
{
  ofstream out;
  out.open("results_long.dat"); // o arquivo que será criado;
	// int n = 100000;
  for (int n = 10; n < 100000; n=n*2){
    clock_t clock_1, clock_2, clock_3, clock_4;
    printf("valor de N: %lu \n", n);
    //Tamanho do vetor
    //Criar vetor com elementos aleatorios[0,100000] 
    criarVetor(n,23);
    //Ordenar utilizando quickSort
    clock_1 = clock();
    qsort (vetorQuickSort, n, sizeof(int), compare_ints);
    clock_2 = clock();
    //Ordenar utilizando bubleSort
    clock_3 = clock();
    bubbleSort(vetorBubbleSort,n);
    clock_4 = clock();
    printf("terminou");
    printf("Tempo de utilização de CPU em ticks QuickSort: %lu \n", (unsigned long)(clock_2-clock_1));
    printf("Tempo de utilização de CPU em segundos QuickSort: %f \n", (double)(clock_2-clock_1)/(double) CLOCKS_PER_SEC);
    printf("Tempo de utilização de CPU em ticks BubbleSort: %lu \n", (unsigned long)(clock_4-clock_3));
    printf("Tempo de utilização de CPU em segundos BubbleSort: %f \n", (double)(clock_4-clock_3)/(double) CLOCKS_PER_SEC);
    unsigned long ClockQuickSort;
    unsigned long ClockBubbleSort;
    ClockQuickSort = (clock_2-clock_1);
    ClockBubbleSort = (clock_4-clock_3);
    out << n << " " << ClockQuickSort;
    out << " " << ClockBubbleSort << endl;
  }
  out.close(); // nã oesqueça de fechar
  exit(0);

}


