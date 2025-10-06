#include<stdio.h>
int main(){
    int n,i,j,pos,temp,bt[4]={21,6,3,2},wt[4],tat[4];
    float awt=0,atat=0;
    for(i=0;i<4;i++){
        pos=i;
        for(j=i+1;j<4;j++)
            if(bt[j]<bt[pos]) pos=j;
        temp=bt[i];
        bt[i]=bt[pos];
        bt[pos]=temp;
    }
    wt[0]=0;
    for(i=1;i<4;i++)
        wt[i]=wt[i-1]+bt[i-1];
    for(i=0;i<4;i++)
        tat[i]=wt[i]+bt[i];
    for(i=0;i<4;i++){
        awt+=wt[i];
        atat+=tat[i];
    }
    printf("Average Waiting Time=%.2f\n",awt/4);
    printf("Average Turnaround Time=%.2f\n",atat/4);
    return 0;
}