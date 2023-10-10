#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int playerChoice, randomNumber;
    srand(time(0)); // Seed for random number generator

    printf("Welcome to the Jackpot Game!\n");
    printf("Choose an option:\n");
    printf("1. Low Risk, Low Reward\n");
    printf("2. Moderate Risk, Moderate Reward\n");
    printf("3. High Risk, High Reward\n");
    printf("Enter your choice: ");
    scanf("%d", &playerChoice);

    // Generating random number based on player's choice
    switch (playerChoice) {
        case 1:
            randomNumber = rand() % 10; // Low risk option (numbers between 0 and 9)
            break;
        case 2:
            randomNumber = rand() % 50; // Moderate risk option (numbers between 0 and 49)
            break;
        case 3:
            randomNumber = rand() % 100; // High risk option (numbers between 0 and 99)
            break;
        default:
            printf("Invalid choice. Please choose a valid option.\n");
            return 1;
    }

    printf("Random number generated: %d\n", randomNumber);

    // Determining the prize based on the player's choice and random number generated
    if (playerChoice == 1) {
        if (randomNumber <= 3) {
            printf("Congratulations! You've won a low-value prize!\n");
        } else {
            printf("Sorry, you didn't win this time. Better luck next time!\n");
        }
    } else if (playerChoice == 2) {
        if (randomNumber <= 25) {
            printf("Congratulations! You've won a moderate-value prize!\n");
        } else {
            printf("Sorry, you didn't win this time. Better luck next time!\n");
        }
    } else {
        if (randomNumber <= 70) {
            printf("Congratulations! You've won a high-value prize!\n");
        } else {
            printf("Sorry, you didn't win this time. Better luck next time!\n");
        }
    }

    return 0;
}
