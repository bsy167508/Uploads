#include <stdio.h>
#include <stdlib.h>

#include <netdb.h>
#include <netinet/in.h>

#include <string.h>

struct table
{
     int ip;
     char mac[30];
     int state;
};

struct table client[255];
void doprocessing (int sock);

int main( int argc, char *argv[] ) {
   
   /*Create a empty MAC vs IP table*/
   int i=2;
   while(i<255)
   {
	client[i].state=0;
	client[i].ip=0;
	strcpy(client[i++].mac, "");
   }


   int sockfd, newsockfd, portno, clilen;
   char buffer[256];
   struct sockaddr_in serv_addr, cli_addr;
   int n, pid;
   
   /* First call to socket() function */
   sockfd = socket(AF_INET, SOCK_STREAM, 0);
   
   if (sockfd < 0) {
      perror("ERROR opening socket");
      exit(1);
   }
   
   /* Initialize socket structure */
   bzero((char *) &serv_addr, sizeof(serv_addr));
   portno = 5001;
   
   serv_addr.sin_family = AF_INET;
   serv_addr.sin_addr.s_addr = INADDR_ANY;
   serv_addr.sin_port = htons(portno);
   
   /* Now bind the host address using bind() call.*/
   if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
      perror("ERROR on binding");
      exit(1);
   }
   
   /* Now start listening for the clients, here
      * process will go in sleep mode and will wait
      * for the incoming connection
   */
   
   listen(sockfd, 5);
   clilen = sizeof(cli_addr);
   


   while (1) {
      newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
		
      if (newsockfd < 0) {
         perror("ERROR on accept");
         exit(1);
      }
      
      /* Create child process */
      pid = vfork();
		
      if (pid < 0) {
         perror("ERROR on vfork");
         exit(1);
      }
      
      if (pid == 0) {
         /* This is the client process */
         close(sockfd);
         doprocessing(newsockfd);
         exit(0);
      }
      else {
         close(newsockfd);
      }
		
   } /* end of while */
}

void doprocessing (int sock) {
   int n;
   int i=2;
   char buffer[30];
   bzero(buffer,30);
   n = read(sock, buffer, 30);
   
   if(strstr(buffer, "SYS_DOWN")==NULL)
   {if (n < 0) {
      perror("ERROR reading from socket");
      exit(1);
   		}
   
   printf("Received MAC Address: %s\n",buffer);
   //assign ip address
   //run through all available ip address from 2 to 255 and pick first one available (with state =0)
   char a[2] = "0";
   char b = '0';
   while(i<255)
   {
	if( client[i].state < 1)
		{
			strcpy(client[i].mac, buffer);
			client[i].ip = i;
			client[i].state = 1;
			b = a[0] + i;
			break;
		}
	i++;
   }
   char c[2] = {b, '\0'};
   char ipaddr[30] = "192.168.1.";
   strcat(ipaddr, c);
   n = write(sock, ipaddr, sizeof(ipaddr));
   
   if (n < 0) {
      perror("ERROR writing to socket");
      exit(1);
   		}
   }
   else
	printf("Hello");
   else //change state of matching mac to zero and set state to 0 then print it also then print all mac vs ip for state = 1
   {
	if (n < 0) {
		perror("ERROR reading from socket");
      		exit(1);
   		   }
        //extract mac address
	char mac[30]="";
	char *ptr = strstr(buffer, " ");
	strncat(mac, &buffer[1+ptr-buffer], sizeof(buffer)-(ptr-buffer));
	printf("\nHello%s", mac);
	while(i<255)
	{
		printf("Hello");
		if(strcmp(mac, client[i].mac)==0)
		{
			client[i].state=0;
			printf("Deleted Entry %s 192.168.1.%d", client[i].mac, client[i].ip);
			break;
		}
		i++;
	}
	i=2;
	while(i<255)
	{
		if(client[i].state==1)
		{
			printf("\n%s 192.168.1.%d\n", client[i].mac, client[i].ip);
		}
	}
	n = write(sock, "", 2);
   }
	
}
