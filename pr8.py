#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_PROC 10
#define MAX_RES 10
int n,m;
int alloc[MAX_PROC][MAX_RES],max_mat[MAX_PROC][MAX_RES],avail[MAX_RES];
int need[MAX_PROC][MAX_RES];
void compute_need(){
int i,j;
for(i=0;i<n;i++)
for(j=0;j<m;j++)
need[i][j]=max_mat[i][j]-alloc[i][j];
}
int is_safe(int safe_seq[]){
int work[MAX_RES],finish[MAX_PROC],i,j,count=0,found;
for(i=0;i<m;i++)work[i]=avail[i];
for(i=0;i<n;i++)finish[i]=0;
while(count<n){
found=0;
for(i=0;i<n;i++){
if(!finish[i]){
int can_alloc=1;
for(j=0;j<m;j++){
if(need[i][j]>work[j]){
can_alloc=0;
break;
}
}
if(can_alloc){
for(j=0;j<m;j++)
work[j]+=alloc[i][j];
finish[i]=1;
safe_seq[count++]=i;
found=1;
}
}
}
if(!found)break;
}
return count==n;
}
int request_resources(int pi,int req[]){
int i,j,safe_seq[MAX_PROC];
int alloc2[MAX_PROC][MAX_RES],avail2[MAX_RES],need2[MAX_PROC][MAX_RES];
if(pi<0||pi>=n){
printf("Invalid process index: %d\n",pi);
return 0;
}
for(i=0;i<m;i++){
if(req[i]>need[pi][i]){
printf("Error: process has exceeded its maximum claim.\n");
return 0;
}
if(req[i]>avail[i]){
printf("Resources not available; process must wait.\n");
return 0;
}
}
for(i=0;i<n;i++)
for(j=0;j<m;j++)
alloc2[i][j]=alloc[i][j];
for(i=0;i<m;i++)avail2[i]=avail[i];
for(i=0;i<m;i++){
avail2[i]-=req[i];
alloc2[pi][i]+=req[i];
}
for(i=0;i<n;i++)
for(j=0;j<m;j++)
need2[i][j]=max_mat[i][j]-alloc2[i][j];
int work[MAX_RES],finish[MAX_PROC],count=0,found;
for(i=0;i<m;i++)work[i]=avail2[i];
for(i=0;i<n;i++)finish[i]=0;
while(count<n){
found=0;
for(i=0;i<n;i++){
if(!finish[i]){
int can_alloc=1;
for(j=0;j<m;j++){
if(need2[i][j]>work[j]){
can_alloc=0;
break;
}
}
if(can_alloc){
for(j=0;j<m;j++)
work[j]+=alloc2[i][j];
finish[i]=1;
safe_seq[count++]=i;
found=1;
}
}
}
if(!found)break;
}
if(count==n){
printf("Request can be granted. Safe sequence: [");
for(i=0;i<n;i++){
printf("%d",safe_seq[i]);
if(i<n-1)printf(", ");
}
printf("]\n");
return 1;
}else{
printf("Request would lead to unsafe state; deny.\n");
return 0;
}
}
void read_matrix(int mat[MAX_PROC][MAX_RES],int rows,int cols,const char*name){
int i,j;
printf("Enter %s matrix (%d rows, %d columns), rows as space-separated integers:\n",name,rows,cols);
for(i=0;i<rows;i++){
printf("Row %d: ",i);
for(j=0;j<cols;j++)
scanf("%d",&mat[i][j]);
}
}
void read_vector(int vec[],int size,const char*name){
int i;
printf("Enter %s vector (%d values, space-separated): ",name,size);
for(i=0;i<size;i++)
scanf("%d",&vec[i]);
}
int main(){
int i,j,safe_seq[MAX_PROC],safe;
char ans[10];
printf("Number of processes: ");
scanf("%d",&n);
printf("Number of resource types: ");
scanf("%d",&m);
read_matrix(alloc,n,m,"Allocation");
read_matrix(max_mat,n,m,"Max");
read_vector(avail,m,"Available");
compute_need();
safe=is_safe(safe_seq);
if(safe){
printf("System is in a SAFE state.\n");
printf("Safe sequence: [");
for(i=0;i<n;i++){
printf("%d",safe_seq[i]);
if(i<n-1)printf(", ");
}
printf("]\n");
}else{
printf("System is in an UNSAFE state (no safe sequence).\n");
}
while(1){
printf("Do you want to try a resource request? (y/n): ");
scanf("%s",ans);
if(ans[0]=='n'||ans[0]=='N')break;
if(ans[0]!='y'&&ans[0]!='Y')continue;
int pi,req[MAX_RES];
printf("Process index (0..%d): ",n-1);
scanf("%d",&pi);
read_vector(req,m,"Request");
if(request_resources(pi,req)){
for(j=0;j<m;j++){
avail[j]-=req[j];
alloc[pi][j]+=req[j];
}
compute_need();
}
}
return 0;
}