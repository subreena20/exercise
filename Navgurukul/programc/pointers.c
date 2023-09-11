#include<stdio.h>
// int main() {
//   int age = 22;
//   int *ptr= &age;
//   int _age= *ptr;
  
//   printf("%d", &_age);
//   return 0;
// }


// Call by value ... mtlb hum variable ki value ki copy pass krvata hai or original value vahi rhte hai.
//  call by reference... hum address pass krvata hai or value chnage ho jate hai. Address ka andr he hum na change value kr diye.
void square(int n);
void _square(int* n);

int main(){
    int number=4;
    square(number);      
    printf("%d\n",number);


    _square(number);   

    printf("%d\n",number);
    return 0;
}

void square(int n){
    n=n*n;
    printf("square = %d\n", n);
}
void _square(int* n){
    *n =(*n) * (*n);
    printf("address = %d\n", *n);
}

// Swap two numbers , a and b.

void swap(int a, int b);

int main(){
    int x=3, y=5;
    swap(x,y);
    printf("x = %d and y = %d\n",x,y);

    return 0;
}
void swap(int a , int b){
    int t =a;
    a=b;
    b=t;
    printf("a= %d and b= %d\n", a , b);
   
}