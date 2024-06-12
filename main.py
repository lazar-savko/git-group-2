from temperature_converter import celsius_to_fahrenheit
from volume_convertor import liters_to_milliliters
from area_converter import square_meters_to_square_kilometers
from speed_converter import mps_to_kph

def main():

    # Length conversions
    meters = 1000
    print(f"{meters} meters is {meters_to_kilometers(meters)} kilometers")

    # Weight conversions
    grams = 1000
    print(f"{grams} grams is {grams_to_kilograms(grams)} kilograms")

    # Temperature conversions
    celsius = 25
    print(f"{celsius} degrees Celsius is {celsius_to_fahrenheit(celsius)} degrees Fahrenheit")

    # Volume conversions
    liters = 2
    print(f"{liters} liters is {liters_to_milliliters(liters)} milliliters")

    # Area conversions
    square_meters = 1000000
    print(f"{square_meters} square meters is {square_meters_to_square_kilometers(square_meters)} square kilometers")

    # Speed conversions
    meters_per_second = 10
    print(f"{meters_per_second} meters per second is {mps_to_kph(meters_per_second)} kilometers per hour")

    # Time conversions
    seconds = 3600
    print(f"{seconds} seconds is {seconds_to_minutes(seconds)} minutes")
    
    # Data conversions
    bytes_value = 1024
    print(f"{bytes_value} bytes is {bytes_to_kilobytes(bytes_value)} kilobytes")


if __name__ == "__main__":
    main()