// #include <iostream>
// using namespace std;

// int main(){

//     int num;
//     cout << "masukkan angka positif: ";
//     cin >> num;

//     if (num < 0 ){
//         cerr << "ERROR: please input possitive number";
//         return 1;
//     }
//     cout << " Angka yang kamu masukkan adalah: " <<  num << endl;
//     return 0;
// }

// #include <iostream>
// using namespace std;

// extern int m;

// int m;
// int main(){


//     cin >> m;
//     cout <<"you entered "<< m << endl;

//     return 0;
// }

#include <iostream>
using namespace std;

int main (){

    cout<< "ENTER YOUR FAVORITE NUMBER BETWEEN 1 AND 100: ";
    
    int m;
    cin >> m;
    if (m == 24){
    cout << "AMAZING!! That's my favorite number too!";
    } else {
        cout << "NO REALLY!! 24 is my favorite" << endl;
        cout << "NO REALLY!!" << m  << " is my favorite number";
    }
    
}

