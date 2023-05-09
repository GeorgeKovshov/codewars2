#include <iostream>
#include <cmath>
#include <string>

using namespace std;

void sayHi(string name, int age); // the declaration of function


void get_age() {
	int age;
	cout << "Enter your age: ";
	cin >> age;
	cout << "You are " << age << " years old" << endl;
}

void get_name() {
	string name;
	cout << "Enter your name: ";
	getline(cin, name);
	cout << "You are " << name<< endl;

}

void calculator() {
	int num1, num2;
	cout << "Enter first number: ";
	cin >> num1;

	cout << "Enter second number: ";
	cin >> num2;

	cout << num1 + num2; 

}

void lucky_nums() {
	int luckyNums[] = { 4,8,14,53,23 };
	int luckyNums2[20] = { 4,8,14,53,23 }; //number inside brackets is the declaration of the array length

	cout << luckyNums[2] << endl;
	luckyNums[2] = 119;
	cout << luckyNums[2] << endl;
}



double cube(double num) {
	double result = num * num * num;
	return result;

}

void isTall_male(bool isMale, bool isTall) {
	if (isMale && isTall) {
		cout << "You are a tall male";
	}
	else if (isMale || !isTall) {
		cout << "You are either male or NOT tall";
	}
	else {
		cout << "You are neither male nor tall";
	}

}

int getMax(int num1, int num2) {
	int result;

	if (num1 > num2) {
		result = num1;
	}
	else {
		result = num2;
	}
	return result;
}

int getMax(int num1, int num2, int num3) {
	int result;

	if (num1 > num2 && num1 >= num3) {
		result = num1;
	}
	else if(num2 > num1 && num2 >= num3){
		result = num2;
	}
	else {
		result = num3;

	}
	return result;
}

double calculator1() {
	int num1, num2, result;
	char op;

	cout << "Enter first number: ";
	cin >> num1;
	cout << "Enter operator: ";
	cin >> op;
	cout << "Enter second number: ";
	cin >> num2;

	if (op == '+') {
		result = num1 + num2;
	}
	else if (op == '-') {
		result = num1 - num2;
	}
	else if (op == '/') {
		result = num1 / num2;
	}
	else if (op == '*') {
		result = num1 * num2;
	}
	else {
		cout << "invalid operator";
		result = 0;
	}
	return result;
}


string getDayOfWeek(int dayNum) {
	string dayName;
	switch (dayNum) {
	case 0:
		dayName = "Sunday";
		break;
	case 1:
		dayName = "Monday";
		break;
	case 2:
		dayName = "Tuesday";
		break;
	case 3:
		dayName = "Wednesday";
		break;
	case 4:
		dayName = "Thursday";
		break;
	case 5:
		dayName = "Friday";
		break;
	case 6:
		dayName = "Saturday";
		break;
	default:
		dayName = "Invalid Day Number";
	}

	return dayName;
}

void looptry() {
	int index = 1;
	while (index <= 5) {
		cout << index << endl;
		index++;
	}
	do {
		cout << index << endl;
		index--;
	} while (index > 0);
}

void loopfor() {

	int nums[] = { 2,4,3,41,5 };
	for (int i = 0; i < 5; i++) {
		cout << nums[i] << endl;
	}

}

int main(void)
{	
	//lucky_nums();
	//sayHi("John", 32);

	//cout << cube(5.0) << endl;

	//bool isMale = true;
	//bool isTall = true;

	//cout << getMax(5, 32) << endl;
	//cout << getMax(5, 32, 64) << endl;

	///cout << calculator1();

	//cout << getDayOfWeek(1) << endl;
	
	loopfor();

	return 0;

}

void sayHi(string name, int age) {
	cout << "Hello " << name << endl << "You are " << age;

}