class vehicle:
    total=0
    def __init__(self,make, model, year):
        vehicle.total+=1
        self.make=make
        self.model=model
        self.year=year
        self.started=False

    def start(self):
        print("Starting engine")
        self.started=True

    def stop(self):
        print("stoping engine")
        self.stop=False

class car(vehicle):
    def __init__(self, make, model, year, noofseats):
        super().__init__(make,model,year)
        self.seats=noofseats

    def drive(s):
        s.start()
        print(f"Driving {s.make}, {s.model}, {s.year}, {s.seats} on the road")

class motocycle(vehicle):
    def __init__(self,make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels=num_wheels

    def ride(s):
        s.start()
        print(f"Driving {s.make}, {s.model}, {s.year}, {s.num_wheels} on the road")

class cycle(vehicle):
    def __init__(self,make,model,year,seats):
        super().__init__(make,model,year)
        self.seats=seats

    def start(s):                             #extend
        super().start()
        print("self-starting")

    def stop(s):                                 # over ride.
        print("self-stoping")