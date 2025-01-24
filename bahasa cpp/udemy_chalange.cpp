#include <iostream>
using namespace std;

int main(){


    int small_rooms{0};
    int large_rooms{0};
    long int price_small_rooms{25}; // tax 10%
    long int price_large_rooms{35}; // tax 10%
    int cost{0};
    float tax{0.066};
    float cost_tax{0};

    // Question for clients
    cout << "\nHow many small rooms would you like cleaned? ";
    cin >> small_rooms;

    cout << "How many large rooms would you like cleaned? ";
    cin >> large_rooms;
    
    // Display input clients
    cout << "\nNumber of small rooms: " << small_rooms;
    cout << "\nNumber of large rooms: " << large_rooms;
    cout << "\nPrice per small room: " << price_small_rooms << " usd";
    cout << "\nPrice per large room: " << price_large_rooms << " usd";

    // Amount of price and tax
    cost = (price_small_rooms*small_rooms)+(price_large_rooms*large_rooms);
    cost_tax =  tax*cost;
    
    // Display total estimate 
    cout << "\nCost: " << cost;
    cout << "\nTax: " << tax;
    cout << "\n=============================================";
    cout << "\nTotal estimate: " << cost+cost_tax;
    cout << "\nThis estimate is valid for 30 days";
}