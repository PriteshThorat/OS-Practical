#include<stdio.h>
int main(){
int ref[]={0,1,2,3,0,1,2,3,0,1,2,3,4,5,6,7};
int capacity=3,ref_size=16,i,j,k,faults=0,frame_count=0,found,pos;
int frames[capacity];
for(i=0;i<ref_size;i++){
found=0;
pos=-1;
for(j=0;j<frame_count;j++){
if(frames[j]==ref[i]){
found=1;
pos=j;
break;
}
}
if(found){
int temp=frames[pos];
for(k=pos;k<frame_count-1;k++)
frames[k]=frames[k+1];
frames[frame_count-1]=temp;
printf("%2d: access %d -> hit   | frames =",i+1,ref[i]);
}else{
faults++;
if(frame_count<capacity){
frames[frame_count++]=ref[i];
}else{
for(k=0;k<capacity-1;k++)
frames[k]=frames[k+1];
frames[capacity-1]=ref[i];
}
printf("%2d: access %d -> fault | frames =",i+1,ref[i]);
}
printf(" [");
for(j=0;j<frame_count;j++){
printf("%d",frames[j]);
if(j<frame_count-1)printf(", ");
}
printf("]\n");
}
printf("\nTotal page faults (LRU, frames=%d): %d\n",capacity,faults);
return 0;
}