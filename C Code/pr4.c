#include<stdio.h>
int main(){
    int n=4,bt[4]={21,6,3,2},wt[4],tat[4],i;
    float awt=0,atat=0;
    wt[0]=0;
    for(i=1;i<n;i++)
        wt[i]=wt[i-1]+bt[i-1];
    for(i=0;i<n;i++)
        tat[i]=wt[i]+bt[i];
    for(i=0;i<n;i++){
        awt+=wt[i];
        atat+=tat[i];
    }
    printf("Average Waiting Time=%.2f\n",awt/n);
    printf("Average Turnaround Time=%.2f\n",atat/n);
    return 0;
}