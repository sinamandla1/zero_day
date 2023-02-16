#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int name=0,code=0;

    char username [] = "JohnDeer";
    char password [] = "NN2940";

    char aname[20];
    char apassword[8];

    name = strcmp(aname,username);
    code = strcmp(apassword,password);

    printf("Enter your username here\n: ");
    scanf("%s",aname);

    printf("Enter your password here\n: ");
    scanf("%s",apassword);

if (name == 0 && code == 0){
    printf("Login successful!");
}
else{
    printf("You have entered your password or username incorrectly!");
    }

    return (0);
}
