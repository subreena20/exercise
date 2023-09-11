// #include <stdio.h>
// int main(){
//     int day;
//     printf("enter a day: ");
//     scanf("%d", &day);

//     switch (day)
//     {
//     case 1: printf("Monday \n");
//         break;
//     case 2: printf("Tuesday \n");
//         break;
//     case 3: printf("Wednesday \n");
//         break;
//     case 4:printf("Thursday \n");
//         break;
//     case 5: printf("friday \n");
//         break;    
//     case 6: printf("saturday \n");
//         break; 
//     case 7: printf("sunday \n");
//         break; 
//     default: printf("not a valid day \n");
//         break;
//     }
// }

#include<stdio.h>
int main(){
    int marks;
    printf("enter marks: ");
    scanf("%d", &marks);

    // if (marks>=0 && marks<=30){
    //     printf("FAIL \n");
    // }
    // else if (marks > 30 && marks <=100){
    //     printf("PASS \n");
    // }
    // else{
    //     printf("wrong marks.");
    // }
    marks<=30? printf("FAIL \n"):prinf("PASS \n");

    return 0;
}



#include <stdio.h>
int main(){
    int marks;
    printf("enter marks: ");
    scanf("%d", &marks);

    if (marks < 30){
        printf("C \n");
    }
    else if (marks >=30 && marks <70){
        printf("B \n");
    }
    else if (marks >=70 && marks <90){
        printf("A \n ");
    }
    else{
        printf("A+ \n");
    }

    return 0;
}