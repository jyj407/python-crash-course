def car(manufacturer, model, **others):
    """Summarize the car information"""
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model 

    for key, value in others.items():
        car_profile[key] = value 
    
    return car_profile

car_profile = car('Honda', 'CRV', year='2019')
print(car_profile)
car_profile = car('BMW', 'Hatchback', year='2020', color='red')
print(car_profile)
