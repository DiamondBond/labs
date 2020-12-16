#include <iostream>
using namespace std;

class Box {
    public:
        double length;
        double width;
        double height;

        double volume(double length, double width, double height){
            return length * width * height;
        }
};

int main() {
    Box package;
    package.length = 2.0;
    package.width = 2.0;
    package.height = 4.0;
    cout << package.volume(package.length, package.width, package.height) << endl;
}
