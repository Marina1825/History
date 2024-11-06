#include <stdio.h>
#include <omp.h>
double f(double y) {return(4.0/(1.0+y*y));}
int main()
{
#ifdef _OPENMP
   printf("OpenMP is supported!\n");
#endif
   double start_time, end_time;
   start_time = omp_get_wtime();
   double w, x, sum, pi;
   int i;
   int n = 100000000;
   w = 1.0/n;
   sum = 0.0;
   omp_set_num_threads(8);
#pragma omp parallel for private(x) shared(w)\
            reduction(+:sum)
   for(i=0; i < n; i++)
   {
      x = w*(i-0.5);
      sum = sum + f(x);
   }
   pi = w*sum;
   end_time = omp_get_wtime();
   printf("Время на замер времени %lf\n", end_time-start_time);
   printf("pi = %f\n", pi);
   
}

