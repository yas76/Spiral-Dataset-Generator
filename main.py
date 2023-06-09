import numpy as np
import matplotlib.pyplot as plt

def spiral_maker(center_radius=None, data_size=None, number_of_spirals=None, number_of_spins=None, number_of_classes=None, noise=0.3):
    if not data_size:
        data_size = np.random.randint(100, 2000, 1)[0]
    if not number_of_spirals:
        number_of_spirals = 0 
        while True: 
            all_numbers = np.array(range(2, data_size))
            divisors = data_size % all_numbers
            divisors = all_numbers[divisors == 0]
            if not divisors.any():
                data_size = np.random.randint(100, 2000, 1)[0]
                continue
            number_of_spirals = np.random.choice(divisors)
            break

    if not number_of_spins:
        number_of_spins = 0
        while not number_of_spins:
            number_of_spins = round(np.random.uniform(0, 2, 1)[0], 2)
    if not center_radius:
        center_radius = 0
        while not center_radius:
            center_radius = round(np.random.uniform(0, 2, 1)[0], 2)

    if not number_of_classes:
        number_of_classes = 0
        while True: 
            all_numbers = np.array(range(2, number_of_spirals))
            divisors = number_of_spirals % all_numbers
            divisors = all_numbers[divisors == 0]
            if not divisors.any():
                number_of_spirals = np.random.randint(3, 101, 1)[0]
                continue
            number_of_classes = np.random.choice(divisors)
            break




    t = np.linspace(0, number_of_spins * np.pi, num=data_size, endpoint=False)
    spiral_theta = np.linspace(0, 2 * np.pi, num=number_of_spirals, endpoint=False)
    
    r = 2*t + center_radius

    spiral_theta = np.repeat(spiral_theta, data_size)
    t = np.tile(t, number_of_spirals)
    r = np.tile(r, number_of_spirals)

    x = r * np.cos(t + spiral_theta) + np.random.randn(data_size*number_of_spirals) * noise
    y = r * np.sin(t + spiral_theta) + np.random.randn(data_size*number_of_spirals) * noise 

    number_of_spiral_in_class = number_of_spirals // number_of_classes

    class_list = list(range(number_of_classes))
    class_list = [i for c in range(number_of_spiral_in_class) for i in range(number_of_classes)]
    class_list += [c for c in range(number_of_spirals % number_of_classes)]

    c = np.random.uniform([0, 0, 0, 0.5], [1, 1, 1, 0.6], size=(number_of_classes,4))
    c = [c[cls] for cls in class_list]
    data_class_color = np.repeat(c, data_size, axis=0)
    data_classes = np.repeat(class_list, data_size)
    
    # c[3] = 0.5

    all_vars = {
        "x":x,
        "y":y,
        "c":data_class_color,
        "target":data_classes,
        "data_size":data_size,
        "number_of_spirals":number_of_spirals,
        "number_of_spins":number_of_spins,
        "number_of_classes":number_of_classes,
        "noise":noise,
        "center_radius":center_radius,
    }
    return all_vars


inputs = {"data_size":150, 'number_of_spirals':24, 'number_of_spins':2, "number_of_classes":8, 'center_radius':0.5, "noise":0.1}

vars = spiral_maker(**inputs)
plt.scatter(x=vars['x'], y=vars['y'], c=vars['c']);

print(
    f"""
    data_size:{vars['data_size']}
    number_of_spirals:{vars['number_of_spirals']}
    number_of_spins:{vars['number_of_spins']}
    number_of_classes:{vars['number_of_classes']}
    """
)


import pandas as pd
data = pd.DataFrame(
    {
    "x1":vars["x"],
    "x2":vars["y"],
    "y":vars["target"],
    }
)

data.to_csv(f"Spiral_data_set_{vars['data_size']}_{vars['number_of_spirals']}_{vars['number_of_spins']}_{vars['number_of_classes']}_{vars['noise']}_{vars['center_radius']}.csv", index=False)
