#include <stdio.h>
#include <math.h>

#define N 8

int Correlation(int a[], int b[]) {
    double sum = 0;
    for (int i = 0; i < N; i++) {
        sum += a[i] * b[i];
    }
    return sum;
}

double NormalCorrelation(int a[], int b[]) {
    double sum_norm = 0;
    double sumA_squared = 0;
    double sumB_squared = 0;
    
    for (int i = 0; i < N; i++) {
        sum_norm += a[i] * b[i];
        sumA_squared += pow(a[i], 2);
        sumB_squared += pow(b[i], 2);
    }
    
    double normalization = sqrt(sumA_squared * sumB_squared);
    return sum_norm / normalization;
}

int main() {
    int a[] = {3, 4, 7, 8, -2, -4, 0};
    int b[] = {2, 5, 8, 10, 4, -3, -1, 2};
    int c[] = {-2, 0, 3, -7, 2, -3, 5, 9};

    int corrAB = Correlation(a, b);
    int corrAC = Correlation(a, c);
    int corrBC = Correlation(b, c);
    
    double normAB = NormalCorrelation(a, b);
    double normAC = NormalCorrelation(a, c);
    double normBC = NormalCorrelation(b, c);
    
    printf("\nКорреляция между a, b и c:\n");
    printf("   | a     | b     |c\n");
    printf("a  |   -   |  %d   | %d\n", corrAB, corrAC);
    printf("b  |  %d   |   -   | %d\n", corrAB, corrBC);
    printf("c  |  %d   |  %d   | -\n", corrAC, corrBC);
    
    printf("\nНормализованная корреляция между a, b и c:\n");
    printf("   | a       | b       | c\n");
    printf("a  |    -    | %.4f  | %.4f\n", normAB, normAC);
    printf("b  | %.4f  |    -    | %.4f\n", normAB, normBC);
    printf("c  | %.4f  | %.4f  |    -\n", normAC, normBC);

    return 0;
}
