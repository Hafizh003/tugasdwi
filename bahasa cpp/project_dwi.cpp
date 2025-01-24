#include <iostream>
using namespace std;

int main(){

    int angka{0};

    cout << "SELAMAT DATANG DI PROGRAM SAYA \n";
    
    cout << "Masukkan angka: ";
    cin >> angka; 

    if(angka %2 == 0){
        cout << "angka yang anda masukkan adalah angka genap\n";
    } else {
        cout << "angka yang anda masukkan adalah angka ganjil\n";
    }

    int jumlah{0};
    for (int i=1; i<= angka; i++) {
        jumlah +=i;
    }

    cout << "Jumlah dari 1 hingga " << angka << " adalah "<< jumlah << endl;
}

// #include <iostream>
// using namespace std;

// int main(){
    
//     cout << "Welcome to Fan Cleaning Service";
//     cout << "\nEntered amount your fan would cleaned: ";

//     int number_of_room{0};
//     int price;
//     cin >> number_of_room;

//     cout << "Numbers of room is "<< number_of_room;
//     cout << "\nPrice all of room " << 30 * number_of_room;


// }
