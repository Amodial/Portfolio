#include <iostream>
#include <string>
#include <fstream>
#include <map>

//Create functions to better display the menu with the given options

void printItemFrequencies(const std::map<std::string& word, const std::map<std::string, int>& inventory) { //Function for printing item count
	auto it = inventory.find(word);
	if (it != inventory.end()) {
		return it->second;
	}
	return 0;
}
int getWordFrequency(const std::string& word, const std::map<std::string, int>& inventory) { 		   // Setting up inventory of items
	auto it = inventory.find(word);
	if (it != inventory.end()) {
		return it->second;
	}
	return 0;
}
void printHistogram(const std::map<std::string, int>& inventory) {      //Setting up Histogram
	for (const auto& pair : inventory) {
		std::cout << pair.first << ": ";
		for (int  i = 0; i < pair.second; i++) {
			std::cout << "*";
		}
		std::cout << std::endl;
	}
}
int main() {
	std::ifstream file("inventory.txt");    			//File to open for reading
	if (!file) { 							//Catch if file did not open
		std::cerr << "Failed to open file." << std::endl;
		return 1;
	}
	int choice; //Menu options

	std::map<std::string, int> inventory;
	std::string item;
	while (file >> item) {
		inventory[item]++;
	}
	do {
		std::cout << "Select one of the following: \n";
		std:cout << "1) Search for item\n 2) Display all frequencies\n 3) Display histogram\n 4) Exit\n"; 	//4 different Menu options
		std::cin >> choice;

		switch (choice) {
		case 1: { 						// For the first option that prints item and frequency
			std::string word;
			std::cout << "Enter grocery item";
			std::cin >> word;
			int frequency = getWordFrequency(word, inventory);
			std::cout << word << frequency << std::endl;
		}
			break;
		
		case 2:  						// Prints all items and their respective number count
		{
			printItemFrequencies(inventory);
			break;
		}
		case 3:
			printHistogram(inventory); 			//Creates a histogram with a * for each unique item
			break;
		case 4: 						//Quits the program
			break;
		default: { //Catch if a number from 1-4 is not selected
			std::cout << "Invalid option." << std::endl;
			break;
		}
		}
	} 
	
	while (choice != 4);
	return 0;

	file.close(); 							//Close the file
}
