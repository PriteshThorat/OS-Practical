#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_BLOCKS 100
#define MAX_FILES 20
#define MAX_NAME 50
typedef struct{
char name[MAX_NAME];
int start;
int size;
}FileEntry;
int total_blocks;
char blocks[MAX_BLOCKS][MAX_NAME];
FileEntry file_table[MAX_FILES];
int file_count=0;
int input_int(const char*prompt,int min_val,int max_val){
int v;
while(1){
printf("%s",prompt);
if(scanf("%d",&v)!=1){
while(getchar()!='\n');
printf("Please enter a valid integer.\n");
continue;
}
if((min_val!=-1&&v<min_val)||(max_val!=-1&&v>max_val)){
printf("Value out of allowed range.\n");
continue;
}
return v;
}
}
int find_contiguous_free(int size){
int i,run=0,start=0;
if(size<=0||size>total_blocks)return -1;
for(i=0;i<total_blocks;i++){
if(strlen(blocks[i])==0){
if(run==0)start=i;
run++;
if(run>=size)return start;
}else{
run=0;
}
}
return -1;
}
void create_file(){
char name[MAX_NAME],mode[10];
int size,start,i,valid=1;
printf("Enter file name: ");
scanf("%s",name);
if(strlen(name)==0){
printf("Invalid name.\n");
return;
}
for(i=0;i<file_count;i++){
if(strcmp(file_table[i].name,name)==0){
printf("File already exists.\n");
return;
}
}
size=input_int("Enter file size (number of contiguous blocks): ",1,-1);
printf("Allocate automatically? (y/n) [y]: ");
scanf("%s",mode);
if(mode[0]=='y'||mode[0]=='Y'||strlen(mode)==0){
start=find_contiguous_free(size);
if(start==-1){
printf("No contiguous region of size %d available.\n",size);
return;
}
}else{
char prompt[100];
sprintf(prompt,"Enter starting block index (0 to %d): ",total_blocks-1);
start=input_int(prompt,0,total_blocks-1);
if(start+size>total_blocks){
printf("Requested range exceeds disk size.\n");
return;
}
for(i=start;i<start+size;i++){
if(strlen(blocks[i])>0){
printf("Blocks not free in the requested range. Allocation failed.\n");
return;
}
}
}
for(i=start;i<start+size;i++)
strcpy(blocks[i],name);
strcpy(file_table[file_count].name,name);
file_table[file_count].start=start;
file_table[file_count].size=size;
file_count++;
printf("File '%s' allocated from block %d to %d.\n",name,start,start+size-1);
}
void delete_file(){
char name[MAX_NAME];
int i,j,found=-1,start,size;
printf("Enter file name to delete: ");
scanf("%s",name);
for(i=0;i<file_count;i++){
if(strcmp(file_table[i].name,name)==0){
found=i;
break;
}
}
if(found==-1){
printf("No such file.\n");
return;
}
start=file_table[found].start;
size=file_table[found].size;
for(i=start;i<start+size;i++){
if(strcmp(blocks[i],name)==0)
strcpy(blocks[i],"");
}
for(i=found;i<file_count-1;i++)
file_table[i]=file_table[i+1];
file_count--;
printf("File '%s' deleted (blocks %d..%d freed).\n",name,start,start+size-1);
}
void display_disk(){
int i,per_line=8;
printf("\nDisk Blocks:\n");
for(i=0;i<total_blocks;i++){
if(strlen(blocks[i])==0)
printf("  %d:.",i);
else
printf("  %d:%s",i,blocks[i]);
if((i+1)%per_line==0||i==total_blocks-1)
printf("\n");
else
printf(" |");
}
printf("\n");
}
void display_file_table(){
int i;
if(file_count==0){
printf("File table empty.\n");
return;
}
printf("\nFile Table:\n");
printf("  Name\tStart\tSize\tEnd\n");
for(i=0;i<file_count;i++)
printf("  %s\t%d\t%d\t%d\n",file_table[i].name,file_table[i].start,file_table[i].size,file_table[i].start+file_table[i].size-1);
printf("\n");
}
int main(){
int choice,i;
printf("Sequential File Allocation Simulator\n");
total_blocks=input_int("Enter total number of disk blocks: ",1,MAX_BLOCKS);
for(i=0;i<total_blocks;i++)
strcpy(blocks[i],"");
while(1){
printf("\nMenu:\n");
printf("  1. Create file (sequential allocation)\n");
printf("  2. Delete file\n");
printf("  3. Display disk blocks\n");
printf("  4. Display file table\n");
printf("  5. Exit\n");
printf("Choose an option (1-5): ");
scanf("%d",&choice);
if(choice==1)
create_file();
else if(choice==2)
delete_file();
else if(choice==3)
display_disk();
else if(choice==4)
display_file_table();
else if(choice==5){
printf("Exiting.\n");
exit(0);
}else
printf("Invalid option.\n");
}
return 0;
}