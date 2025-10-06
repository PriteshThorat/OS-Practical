#include<stdio.h>
int main(){
    int n=4,i,j,pos,temp,bt[4]={21,6,3,2},priority[4]={2,1,4,3},wt[4],tat[4];
    float awt=0,atat=0;
    for(i=0;i<n;i++){
        pos=i;
        for(j=i+1;j<n;j++)
            if(priority[j]<priority[pos]) pos=j;
        temp=bt[i]; bt[i]=bt[pos]; bt[pos]=temp;
        temp=priority[i]; priority[i]=priority[pos]; priority[pos]=temp;
    }
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