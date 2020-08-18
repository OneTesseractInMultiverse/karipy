# Uso de Format
import time

# --------------------------------------------------
# FUNCTION SOLARIZE
# --------------------------------------------------
def solarize(q: float, c: float) -> float:
    return (q ** 3)/c


letter = """
Dear {person}, 

I am excited to share with you that you have been admitted to the {university_program} at {university_name}. You 
have been selected from about {amount_of_candidates} since the skills shown are amazingdatetime A combination of a date and a time.

Go drink a lot of {alcoholic_beverage} to celebrate!

Thanks, 
{dean_name}
"""

print("===============================================================")
print(" LETTER OF ADMISION - TRINITY COLLEGE OF IRELEND")
print("===============================================================")
print(
    letter.format(
        person='Kari',
        university_program='Master Specialization in Distillation',
        university_name="Trinity College of Ireland", 
        amount_of_candidates=10000, 
        alcoholic_beverage='Whiskey',
        dean_name="Sir Peter Shelby"
        )
    )
print("================================================================")

name = 'Kari'
solarized_cfnt = solarize(30, 8)

print("Hola " + name + ", te has solarizado: " + str(solarized_cfnt))

print("Hola {}, te has solarizado: {}".format(name, solarized_cfnt))
print("Hola {person}, te has solarizado: {value}".format(person=name, value=solarized_cfnt))

def print_multiplication_entry(number_a, number_b):
    return "{a} X {b} = {result}".format(
        a=number_a, 
        b=number_b, 
        result=(number_a * number_b)
        )


# for a in range(0, 10):
#     for b in range(0, 10):
#         print(print_multiplication_entry(a, b))

def format_digits(value):
    if value < 10:
        return "0{}".format(value)
    return str(value)


for hours in range(0, 24):
    for minutes in range(0, 60):
        for seconds in range(0, 60):
            time.sleep(1)
            print("{hours}:{minutes}:{seconds}".format(
                hours=format_digits(hours), 
                minutes=format_digits(minutes), 
                seconds=format_digits(seconds))
                )


