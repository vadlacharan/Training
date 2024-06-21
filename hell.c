int main()
{
int a[5]={5,9,2,1,3},*b;
b=a+2;
printf("%d %d %d",*(b+1),a[*(a+3)],*b+2);
}