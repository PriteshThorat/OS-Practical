#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
int n,q,i,j,time=0,finished_count=0;
printf("Number of processes: ");
scanf("%d",&n);
int burst[n],remaining[n],waiting[n],turnaround[n],finished[n];
printf("Enter %d burst times (space separated): ",n);
for(i=0;i<n;i++){
scanf("%d",&burst[i]);
remaining[i]=burst[i];
waiting[i]=0;
finished[i]=0;
}
printf("Time quantum: ");
scanf("%d",&q);
while(finished_count<n){
int made_progress=0;
for(i=0;i<n;i++){
if(remaining[i]>0){
made_progress=1;
if(remaining[i]>q){
time+=q;
remaining[i]-=q;
}else{
time+=remaining[i];
waiting[i]=time-burst[i];
remaining[i]=0;
finished[i]=1;
finished_count++;
}
}
}
if(!made_progress)break;
}
for(i=0;i<n;i++)
turnaround[i]=waiting[i]+burst[i];
float avg_wait=0,avg_turnaround=0;
for(i=0;i<n;i++){
avg_wait+=waiting[i];
avg_turnaround+=turnaround[i];
}
avg_wait/=n;
avg_turnaround/=n;
printf("\nPID\tBurst\tWaiting\tTurnaround\n");
for(i=0;i<n;i++)
printf("P%d\t%d\t%d\t%d\n",i+1,burst[i],waiting[i],turnaround[i]);
printf("\nAverage waiting time: %.2f\n",avg_wait);
printf("Average turnaround time: %.2f\n",avg_turnaround);
return 0;
}