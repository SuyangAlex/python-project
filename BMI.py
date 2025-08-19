def bmi(height, weight): 
    BMI = weight/(height)**2
    if BMI < 18.5:
        return "過輕"
    elif 18.5 <= BMI < 24:
        return "正常"
    elif 24 <= BMI < 27:
        return "過重"
    elif 27 <= BMI < 30:
        return "輕度肥胖"
    elif 30 <= BMI < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"