'''IMPLEMENT A CLASS CAR WITH METHODS TO START STOP AND CHANGE THE GEARS'''

class Car:

    def start(self):
        print("The car is starting ")
        print("Car Started")
        self.Gears()



    def stop(self):
        print("Stopping the car")
        print("Car Stopped")

    def Gears(self):

        gear_num = 0
        while 0 <= gear_num <= 5:
            shift = int(input("Enter 0 to shift down, 9 for neutral and stop and 1 to shift up"))
            print(shift)
            if shift == 1:
                gear_num += 1
                print(f"Shifting up, Gear: {gear_num}")

            elif shift == 0:
                gear_num-= 1
                print(f"Shifting down,  Gear: {gear_num}")

            elif shift == 9:
                gear_num = 0
                print("Making it neutral to stop")
                self.stop()
                break

            else:
                print("Wrong command enter, Enter again ")
                continue



my_car = Car()
my_car.start()