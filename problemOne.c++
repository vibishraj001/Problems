#include<iomanip>
  #include<iostream>
  using namespace std;
  int main()
  {
      bool accountCreated;
    if (accountCreated) {
        double amount;
        cout << "\nEnter the amount to withdraw: $";
        cin >> amount;
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "\nWithdrawal successful. Your new balance is: $" << fixed << setprecision(2) << balance << endl;
        } else {
            cout << "\nInvalid amount or insufficient funds. Withdrawal failed.\n";
        }
    } else {
        cout << "\nNo account exists. Please create an account first.\n";
    }
}