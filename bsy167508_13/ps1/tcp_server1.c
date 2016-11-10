#include<stdio.h>
#include<netinet/in.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netdb.h>
#include<stdlib.h>
#include<string.h>

#define MAX 120
#define PORT 43454
#define SA struct sockaddr

void str_split(int sockfd, char* buff)
{
int i = 0;
int flag;
//char array[10][100];
char send[200]="";
char arr[5][20] = {"\nProtocol: ", "\nDomain name: ","\nFilepath: ","\nParameter: ", "\nAnchor: "};
//char *protocol = strtok (buff, "/"); //protocol
char param[2]="?";
char anchor[2]="#";
//char *retpar, *retanc;
//char *domain = strtok(&buff[0+protocol-buff],"/");
//char *filepath = strtok(&buff[0+domain-buff], "?");
printf("Hello");
//printf("%s %s %s", protocol, domain, filepath);
//break the url into two more parts

//for (i = 0; i<5 ; ++i) 
//{
//strcat(send, arr[i]);
//if(i<2)
//{
//	strcat(send, array[i]);
//}

//else
//{
//	switch(i)
//	{	case 2: strcat(send, arr[i]); //Filepath: 
//			retpar = strstr(array[i], param);
			//catenate into send until you find a '?' or the string terminates
//			strncat(send, array[i], retpar-array[i]);

//		case 3: strcat(send, arr[i]); //Parameter: 
//			retpar = strstr(array[i], param);
//			retanc = strstr(array[i], anchor);
//			//catenate into send after the ? and until you find # or string terminates
//			strncat(send, &array[i][1+retpar-array[i]], retanc-retpar-1);
//	
//		case 4: strcat(send, arr[i]); //Anchor
//			retanc = strstr(array[i], "#");
//			strncat(send, &array[i][retanc-array[i]+1], sizeof(array[i])-(retanc-array[i]));
		
//		default:; 
//	}
//}
//}
//printf("%s", send);
}

void func(int sockfd)
{
while(1)
{
char buff[MAX];
bzero(buff,MAX);
read(sockfd, buff, sizeof(buff));
printf("Received url %s\nSending the components...\n",buff);
str_split(sockfd, buff);
}
}

int main()
{
int sockfd, connfd, len;
struct sockaddr_in servaddr,cli;
sockfd=socket(AF_INET,SOCK_STREAM,0);
if(sockfd==-1)
{
printf("Socket creation failed...\n");
exit(0);
}
else
printf("Socket successfully created..\n");
bzero(&servaddr,sizeof(servaddr));
servaddr.sin_family=AF_INET;
servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
servaddr.sin_port=htons(PORT);
if((bind(sockfd,(SA*)&servaddr, sizeof(servaddr)))!=0)
{
printf("Socket bind failed...\n");
exit(0);
}
else
printf("Socket successfully binded..\n");
if((listen(sockfd,5))!=0)
{
printf("Listen failed...\n");
exit(0);
}
else
printf("Server listening..\n");
len=sizeof(cli);
connfd=accept(sockfd,(SA *)&cli,&len);
if(connfd<0)
{
printf("Server acccept failed...\n");
exit(0);
}
else
printf("Server acccept the client...\n");
func(connfd);
close(sockfd);
}
