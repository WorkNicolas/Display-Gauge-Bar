"""_summary_
Requirements
1.	You will pick a quantity that your value will mimic (such as earth tremors, 
temperature, cars passing through as intersection, humidity, barometric pressure, 
customers arriving at a mall, or just with an alternate descriptor). This will 
guide you when transforming the generated values to actual read-life data values 
to display on your diagram. You must have as idea on the range of value that will 
model your chosen quantity.

2.	Design and build a class that will model your sensor reasonably well. Notice 
how the peaks do not occur at regular interval, nor are they the same height. Even 
the squiggles are not the same shapes.

3.	Your class must have a fair amount of customization but at the same time should 
be easy to use, so provide a constructor with lots of default values.

4.	Make it so that you can generate your data by repeated calling a method or 
accessing a property of the class instance. The member will give values ONLY in the 
range [0, 1.0). Your generator must return a single float, not a list of floats. 

5.  Provide the code to display a diagram similar to the above which was done using 
matplotlib. You will have to convert the values obtained in step 4 to your range.
You will provide meaningful label for the axis's and the title.

See the appendix of this document for some code sample and possible directions to explore. You will need some combination of the last three examples.
•	Use generator_4() will give peaks and valleys
•	Use generator_3() to change the length (or frequency) of the peaks.
•	Use generator_2() and to get the squiggles.

Ali Asjid Muhammad
Michael Asfeha
Carl Nicolas Mendoza

"""
import matplotlib.pyplot as plt
import math
import random
import numpy as np

class RandomValueGenerator():
    value = {
        'base': 0.0,
        'min_val': 0.0,
        'max_val': 0.5,
        'delta': random.randint(1,10)/1000
    }
    trending = {
        'trend': 0,
        'trendCounter': 0,
        'trendResetter': False
    }
    def __init__(self, number_of_values = 500, **kwargs):
        for key in self.value:
            setattr(self, key, kwargs.get(key, self.value[key]))
            
        for key in self.trending:
            setattr(self, key, kwargs.get(key, self.trending[key]))
        self.number_of_values = number_of_values
        self.finalValue = 0.0
        self.peak = 0
    
    def squiggleGenerator(self) -> float:
        return random.randint(0, 10)/150.0

    def lengthGenerator(self) -> float:
        value = random.gauss(0.02, 0.001)
        while value < 0.0 or value > 1.0:  
            value = random.gauss(0.02, 0.001)
        return value


    def peaksAndValleysGenerator(self) -> float:
        if self.base + self.delta > self.max_val or self.base + self.delta < 0.0:
            self.delta *= -1
        self.base += self.delta
        self.base = max(0.0, self.base) 
        return self.base


    # Randomizes trend that generateTrend will add/subtract
    def generateTrendRandomizer(self):
        return random.randint(0, 10)/10000.0

    # Keep increasing until peak, then it will go down
    def generateTrend(self):
        if (self.finalValue < self.peak):
            self.trend = self.trend + self.generateTrendRandomizer()
            self.trendCounter += 1
        else:
            self.trend = self.trend - self.generateTrendRandomizer()
            self.trendCounter -= 1
        # Reset trend randomly
        if (random.randint(0,1) == 0):
            self.trendResetter = True
            print(self.trendResetter)
        if (self.trendResetter):
            self.trendCounter = 0
            self.trendResetter = False

    def getNext(self):
        self.finalValue += self.trend
        
        # Generate random squiggle value from 0.0 to 0.1
        squiggle = self.squiggleGenerator()
        
        # Choose peak to increase to
        if (self.trendCounter == 0):
            self.peak = self.peaksAndValleysGenerator()
            #print(self.peak)
        
        # Keep increasing until it reaches peak/Decrease once it reaches peak
        self.generateTrend()
            
        return self.finalValue + squiggle
        

# Initialize
rvg = RandomValueGenerator()
number_of_values = rvg.number_of_values

# Plot
# x = [rvg.getNext() for _ in range(number_of_values)]
x = [rvg.getNext() for _ in range(number_of_values)]
plt.title("Humidity Sensor at Progress Campus")
plt.xlabel('Time (seconds)')
plt.ylabel('Humidity')
plt.plot(x, color='green')
plt.show()
