class Phone(): 
    """This is a phone class that can be used for inheritance purposes"""
    def __init__(self, phone_number, color):
        self.number = phone_number
        self.color = color

    def __str__(self):
        return f"This phone belongs to {self.number}"

    def call(self, other_number):
        print(f"Calling number: {other_number}")

    def text(self, other_number, message):
        print(f'Sending text to {other_number}')
        print(message)

    def open_app(self, app_name):
        print(f"Opening {app_name}")

class Android(Phone):
    def __init__(self, number, color):
        super().__init__(number, color)
        self.passcode = None
        self.battery = 50

    def __str__(self):
        return f"Android phone that belongs to number {self.number}"

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print("Phone unlocked")

    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")
    
    def charge_phone(self, charging_amount):
        self.battery += charging_amount
        if self.battery > 100:
            self.battery = 100
    
    def view_phone_number(self):
        print(f"Phone number: {self.number}")

frank_phone = Android('888-777-3333', 'Black')

frank_phone.view_battery_life()
frank_phone.charge_phone(40)
frank_phone.view_battery_life()
frank_phone.view_phone_number()
frank_phone.call("345-213-6344")
frank_phone.open_app('Zoom')

class IPhone(Phone):
    def __init__(self, number, color):
        super().__init__(number, color)
        self.charge = False
        self.bing = "Bing!"
    
    def __str__(self):
        return f"iPhone that belongs to number {self.number}"
    
    def face_time(self, person_number):
        return f"You are facetiming with: {person_number}"
    
    def lightning_charge(self):
        self.charge = True
        print(self.bing)
