from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ATMApp(App):
    def build(self):
        self.balance = 5000
        self.transactions = []

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.info_label = Label(text="Welcome! Enter your ATM PIN:", font_size='20sp', size_hint=(1, 0.3))
        self.layout.add_widget(self.info_label)

        self.input_box = TextInput(hint_text="Enter PIN or Amount", multiline=False, font_size='20sp', size_hint=(1, 0.15))
        self.layout.add_widget(self.input_box)

        self.login_btn = Button(text="Submit PIN", font_size='20sp', size_hint=(1, 0.15), background_color=(0, 0.7, 0.3, 1))
        self.login_btn.bind(on_press=self.check_pin)
        self.layout.add_widget(self.login_btn)

        # Menu Buttons (Shuru me chhupe rahenge)
        self.menu_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.6))
        
        btn_bal = Button(text="1. Check Bank Balance", font_size='18sp')
        btn_bal.bind(on_press=self.check_balance)
        
        btn_with = Button(text="2. Withdraw Amount", font_size='18sp')
        btn_with.bind(on_press=self.withdraw)
        
        btn_dep = Button(text="3. Deposit Amount", font_size='18sp')
        btn_dep.bind(on_press=self.deposit)
        
        btn_mini = Button(text="4. Mini Statement", font_size='18sp')
        btn_mini.bind(on_press=self.mini_statement)
        
        btn_exit = Button(text="0. Exit", font_size='18sp', background_color=(0.8, 0.2, 0.2, 1))
        btn_exit.bind(on_press=self.stop)

        self.menu_layout.add_widget(btn_bal)
        self.menu_layout.add_widget(btn_with)
        self.menu_layout.add_widget(btn_dep)
        self.menu_layout.add_widget(btn_mini)
        self.menu_layout.add_widget(btn_exit)

        return self.layout

    def check_pin(self, instance):
        pin = self.input_box.text
        if pin == "9993400":
            self.info_label.text = "PIN Verified! Choose an option.\n(Enter amount in box for Withdraw/Deposit)"
            self.input_box.text = ""
            self.input_box.hint_text = "Enter Amount here"
            self.layout.remove_widget(self.login_btn)
            self.layout.add_widget(self.menu_layout)
        else:
            self.info_label.text = "Incorrect PIN! Try again."

    def check_balance(self, instance):
        self.info_label.text = f"Your Bank Balance is: Rs. {self.balance}"

    def withdraw(self, instance):
        try:
            amount = int(self.input_box.text)
            if amount <= 0:
                self.info_label.text = "Please enter a valid amount!"
            elif amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Withdrawn: -{amount}")
                self.info_label.text = f"Withdrawal Successful!\nNew Balance: Rs. {self.balance}"
                self.input_box.text = ""
            else:
                self.info_label.text = "Insufficient Balance!"
        except ValueError:
            self.info_label.text = "First type amount in the box above!"

    def deposit(self, instance):
        try:
            amount = int(self.input_box.text)
            if amount > 0:
                self.balance += amount
                self.transactions.append(f"Deposited: +{amount}")
                self.info_label.text = f"Deposit Successful!\nNew Balance: Rs. {self.balance}"
                self.input_box.text = ""
            else:
                self.info_label.text = "Please enter a valid amount!"
        except ValueError:
            self.info_label.text = "First type amount in the box above!"

    def mini_statement(self, instance):
        if not self.transactions:
            self.info_label.text = f"No transactions yet.\nBalance: Rs. {self.balance}"
        else:
            history = "\n".join(self.transactions[-3:]) # Last 3 transactions
            self.info_label.text = f"--- Mini Statement ---\n{history}\nBalance: Rs. {self.balance}"

if __name__ == "__main__":
    ATMApp().run()
