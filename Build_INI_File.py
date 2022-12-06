import configparser

config=configparser.ConfigParser()

config.add_section("carlots")
config.add_section("empty_spots")
config.set("carlots","carparkedposition","{1: [[35, 20]], 2: [[65, 20]],3: [[35, 32]], 4: [[65, 32]],5: [[35, 44]], 6: [[65, 44]],7: [[35, 56]], 8: [[65, 56]],9: [[35, 68]], 10: [[65, 68]],11: [[35, 80]], 12: [[65, 80]],13: [[35, 92]], 14: [[65, 92]]}")
config.set("empty_spots","empty_spots_position","3,6")


with open("C:/Users/shubh/automatic-car-parking/configfile.ini",'w') as configfile:
    config.write(configfile)