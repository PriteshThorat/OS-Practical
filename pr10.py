#include<stdio.h>
#include<string.h>
int fifo_page_faults(int ref[],int ref_size,int frame_size,int preload){
int frames[frame_size],frame_count=0,faults=0,i,j,found,idx=0;
memset(frames,-1,sizeof(frames));
if(preload){
for(i=0;i<ref_size&&frame_count<frame_size;i++){
found=0;
for(j=0;j<frame_count;j++){
if(frames[j]==ref[i]){
found=1;
break;
}
}
if(!found){
frames[frame_count++]=ref[i];
}
}
}
for(i=0;i<ref_size;i++){
found=0;
for(j=0;j<frame_count;j++){
if(frames[j]==ref[i]){
found=1;
break;
}
}
if(!found){
faults++;
if(frame_count<frame_size){
frames[frame_count++]=ref[i];
}else{
frames[idx]=ref[i];
idx=(idx+1)%frame_size;
}
}
}
return faults;
}
int main(){
int ref[]={0,1,2,3,0,1,2,3,0,1,2,3,4,5,6,7};
int ref_size=16,frame_size=3,i;
int faults_empty=fifo_page_faults(ref,ref_size,frame_size,0);
int faults_preloaded=fifo_page_faults(ref,ref_size,frame_size,1);
printf("Reference string:");
for(i=0;i<ref_size;i++)
printf(" %d",ref[i]);
printf("\nFrame size: %d\n",frame_size);
printf("\nFIFO starting with empty frames -> page faults: %d\n",faults_empty);
printf("FIFO with first distinct pages preloaded -> page faults: %d\n",faults_preloaded);
return 0;
}