import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Comentário - New Antecedent/Consequent objects hold universe variables and membership functions
temp = ctrl.Antecedent(np.arange(0, 101, 1), 'temp')
clock_speed = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'clock_speed')
fan_speed = ctrl.Consequent(np.arange(0, 6001, 1), 'fan_speed')

#Comentário - Auto-membership function population is possible with .automf(3, 5, or 7)
#quality.automf(3)
#service.automf(3)

#Comentário - Custom membership functions can be built interactively with a familiar, Pythonic API
temp['Cold'] = fuzz.trimf(temp.universe, [0, 0, 50])
temp['Warm'] = fuzz.trimf(temp.universe, [30, 50, 70])
temp['Hot'] = fuzz.trimf(temp.universe, [50, 100, 100])

clock_speed['Low'] = fuzz.trimf(clock_speed.universe, [0, 0, 1.5])
clock_speed['Normal'] = fuzz.trimf(clock_speed.universe, [0.5, 2, 3.5])
clock_speed['Turbo'] = fuzz.trimf(clock_speed.universe, [2.5, 4, 4])

fan_speed['Slow'] = fuzz.trimf(fan_speed.universe, [0, 0, 3500])
fan_speed['Fast'] = fuzz.trimf(fan_speed.universe, [2500, 6000, 6000])

#temp.view()
#clock_speed.view()
#fan_speed.view()
#plt.show()

rule1 = ctrl.Rule(temp['Cold'] & clock_speed['Low'], fan_speed['Slow'])
rule2 = ctrl.Rule(temp['Cold'] & clock_speed['Normal'], fan_speed['Slow'])
rule3 = ctrl.Rule(temp['Cold'] & clock_speed['Turbo'], fan_speed['Fast'])
rule4 = ctrl.Rule(temp['Warm'] & clock_speed['Low'], fan_speed['Slow'])
rule5 = ctrl.Rule(temp['Warm'] & clock_speed['Normal'], fan_speed['Slow'])
rule6 = ctrl.Rule(temp['Warm'] & clock_speed['Turbo'], fan_speed['Fast'])
rule7 = ctrl.Rule(temp['Hot'] & clock_speed['Low'], fan_speed['Fast'])
rule8 = ctrl.Rule(temp['Hot'] & clock_speed['Normal'], fan_speed['Fast'])
rule9 = ctrl.Rule(temp['Hot'] & clock_speed['Turbo'], fan_speed['Fast'])

#rule1.view()
#plt.show()

fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,rule6,rule7,rule8,rule9])
fan_speeding = ctrl.ControlSystemSimulation(fan_speed_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
fan_speeding.input['temp'] = 100
fan_speeding.input['clock_speed'] = 4

# Crunch the numbers
fan_speeding.compute()

print (fan_speeding.output['fan_speed'])
fan_speed.view(sim=fan_speeding)
plt.show()