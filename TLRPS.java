// Tuan Le
// Assignment 3: Final Project -- RPS Java Version
// Purpose: Creates an instance of a Rock, Paper, Scissors program
// Extra Credit: Python

import java.util.*;

public class TLRPS {

    private static String playerInput;
    private static String CPUInput;
    private static String[] RPS = new String[] {"R", "P", "S"};
    private static int playerScore = 0;
    private static int CPUScore = 0;
        
    public static void main(String[] args) {
        start();
    } // end of main

    public static void start() { // intro to program
        System.out.println("Welcome to my program of \"Rock, Paper, Scissors\"!");
        System.out.println("Would you like to play a game with me?");
        menu();
    } // end of intro
    
    public static void menu() { // menu for player decision
        System.out.printf("%n(Y)es or (N)o?%n");
        Scanner inputScan = new Scanner(System.in);
        playerInput = inputScan.next();
        startOrQuit();
    } // end of menu

    public static void startOrQuit() { // path for whether to continue or end program
        if (playerInput.equalsIgnoreCase("y")) { // continues the program
            playerRPS();
        }
        else if (playerInput.equalsIgnoreCase("n")) { // closes the program
            unplayedQuit();
        }
        else { // invalid input catch
            System.out.printf("%n" + playerInput + " is not a valid input.");
            menu();
        }
    } // end of startOrQuit

    public static void CPURandom() { // randomizes the choice made by CPU
        CPUInput = RPS[new Random().nextInt(RPS.length)];
    } // end of CPURandom

    public static void playerRPS() { // player choice variation 1
        CPURandom();
        System.out.printf("%n(R)ock, (P)aper, or (S)cissors?%n");
        Scanner inputScan = new Scanner(System.in);
        playerInput = inputScan.next();
        if (playerInput.equalsIgnoreCase("r")) {
            rock();
        }
        else if (playerInput.equalsIgnoreCase("p")) {
            paper();
        }
        else if (playerInput.equalsIgnoreCase("s")) {
            scissors();
        }
        else {
            System.out.println(playerInput + "is not a valid input.");
            playerRPS();
        }
    } // end of playerRPS

    public static void playerRPSQuit() { // player choice variation 2
        CPURandom();
        System.out.printf("%n(R)ock, (P)aper, (S)cissors, or (Q)uit?%n");
        Scanner inputScan = new Scanner(System.in);
        playerInput = inputScan.next();
        if (playerInput.equalsIgnoreCase("r")) {
            rock();
        }
        else if (playerInput.equalsIgnoreCase("p")) {
            paper();
        }
        else if (playerInput.equalsIgnoreCase("s")) {
            scissors();
        }
        else if (playerInput.equalsIgnoreCase("q")) {
            scoredQuit();
        }
        else {
            System.out.println(playerInput + "is not a valid input.");
            playerRPS();
        }
    } // end of playerRPSQuit

    public static void rock() { // rock variation
        if (CPUInput == "R") {
            System.out.printf("%nIt's a Draw. We both picked Rock.");
        } 
        else if (CPUInput == "P") {
            System.out.printf("%nI Win! You picked Rock, while I picked Paper.");
            CPUScore += 1;
        }
        else {
            System.out.printf("%nYou Win! You picked Rock, while I picked Scissors.");
            playerScore += 1;
        }
        score();
    } // end of rock

    public static void paper() { // paper variation
        if (CPUInput == "R") {
            System.out.printf("%nYou Win! You picked Paper, while I picked Rock.");
            playerScore += 1;
        } 
        else if (CPUInput == "P") {
            System.out.printf("%nIt's a Draw. We both picked Paper.");
        }
        else {
            System.out.printf("%nI Win! You picked Paper, while I picked Scissors.");
            CPUScore += 1;
        }
        score();
    } // end of paper

    public static void scissors() { // scissors variation
        if (CPUInput == "R") {
            System.out.printf("%nI Win! You picked Scissors, while I picked Rock.");
            CPUScore += 1;
        } 
        else if (CPUInput == "P") {
            System.out.printf("%nYou Win! You picked Scissors, while I picked Paper.");
            playerScore += 1;
        }
        else {
            System.out.printf("%nIt's a Draw. We both picked Scissors.");
        }
        score();
    } // end of scissors

    public static void score() { // displays current scores
        System.out.printf("%n%nCurrent Scores:");
        System.out.printf("%nPlayer " + playerScore + " || " + CPUScore + " CPU%n");
        playerRPSQuit();
    } // end of score

    public static void unplayedQuit() { // quitting variation if player leaves without playing
        System.out.printf("%nQuitting Program...");
    } // end of unplayedQuit

    public static void scoredQuit() { // quitting variation if player leaves after playing
        System.out.printf("%nFinal Scores:");
        System.out.printf("%nPlayer " + playerScore + " || " + CPUScore + " CPU");
        System.out.printf("%n%nThanks for Playing!");
    } // end of scoredQuit

} // end of TLRPS
