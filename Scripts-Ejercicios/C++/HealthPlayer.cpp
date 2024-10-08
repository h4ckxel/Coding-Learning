#include<iostream>
#include<stdio.h>

int main(){
	int health=55;
	bool player_healed = 100; //tambien puede ser, "player_healed = true"
	
	if (health<100 && player_healed){
	// health<100 = T, player_healed = T
	// T && T = health=100; 
	health=100;
	printf("health of player is: %d", health);
	}
	
	return 0;
}
