
// calculate prize of a value...recursion
#include<stdio.h>

void calculateprize(float value);

int main() {
  float value = 100.0;
  calculateprize(value);

  return 0;
}

void calculateprize(float value){
  value = value + (0.18 * value);
  printf("Final prize is: %f", value);
}


// print the area of circle and rectnagle and square.. recursion
#include<stdio.h>
#include<math.h>
int main() {
    
    int n=4;
    printf("%f", pow(n,2));

  return 0;
}

#include<stdio.h>

float squareside(float side);

float circlearea(float radi);
float rectarea(float a, float b);


int main() {
  
  float a=5.0;
  float b=1.5;
  printf("area of rectnagle is: %f", rectarea(a , b));

  return 0;
}

float squareside(float side){
  return side * side;
}

float circlearea( float radi){
  return 3.14 * radi * radi;
}
  
float rectarea(float a, float b){
  return a*b;
}

// recursive sum of n numbers
#include<stdio.h>

int sum(int n);

int main() {
  printf("sum is: %d", sum(5));
  return 0;
}

int sum(int n){
  if (n==1){
    return 1;
  }
  int sumnum1= sum(n-1);  
  int sumn= sumnum1+ n;
  return sumn;
}

// factorial of n number...recursion
#include<stdio.h>

int fact(int n);

int main() {
  printf("fact is: %d", fact(5));
  return 0;
}

int fact(int n){
  if (n==1){
    return 1;
  }
  int factnum1= fact(n-1);
  int factn= factnum1 * n;
  return factn;

}

// convert celsius to farhenits temperature ... f = c * (9/5) + 32.

#include<stdio.h>
float converttemp(float celsius);

int main(){
    float far = converttemp(0);
    printf("far : %f", far);
    return 0;
}

float converttemp(float celsius){
    float far = celsius * (9.0/5.0) + 32;
    return far;
}


//  write a function to calculate percentage of a student from marks in science, math & sanskrit.

int calcpercentage( int science, int math, int sanskrti);

int main(){
    int science=98;
    int math = 95;
    int sanskrti=99;
    printf("percentage is : %d",calculatepercentage(science, math, sanskrti));
    return 0;
}
int calculatepercentage(int science, int math, int sanskrti){
    return ((science+math+sanskrti)/3);
}

// write a fibonacconi series 0,1,1,2,3,5,8,13,21,34,55,89,144,..
// recursive function.
int fibo(int n);

int main(){
    fibo(6);
    return 0;
}

int fibo(int n){
    if ( n==0){
        return 0;
    }
    if ( n==1){
        return 1;
    }
    int fibo1= fibo(n-1);
    int fib02= fibo(n-2);
    int fibon=fibo1 + fib02;
    printf("fibonacci of %d is: %d", n,fibon);
    return fibon;

}

int main(){
    int n=10;
    int m=0;
    int j=1;
    for (int i=1;i<=n;i++){
       int temp= m+j;
       printf("%d\n",temp);
       m=j;
       j=temp; 

    }

}