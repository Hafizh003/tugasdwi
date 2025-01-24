// #include <iostream>
// using namespace std;

// int main(){

//     int angka{0};

//     cout << "Input angka: ";
//     cin >> angka;

//     int jumlah{0};
//     for (int i=1; i<=angka; i++) 
//     {
//         jumlah +=i;
//     }

//     cout << jumlah;

// }

// pengulangan penambahkan bilangan ganjil hingga ke -n
// #include <iostream>
// using namespace std;

// int main(){

//     int angka{0};

//     cout << "Input angka: ";
//     cin >> angka;

//     int jumlah{0};
//     for (int i=1; i<=angka; i++) 
//     {
//        if (i % 2 != 0)
//         {
//         jumlah +=i;
//         }
//     }

//     cout << jumlah;

// }



#include <iostream>
using namespace std;

int main(){

    int angka{0};

    cout << "Input angka: ";
    cin >> angka;

    auto jumlah{0};
    for (int i=1; i<=angka; i++) 
    {
       if (i % 2 == 0)
        {
        jumlah +=i;
        }
    }

    cout << jumlah;

}