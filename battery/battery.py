"Battery class"
# battery and chaging control
#
#   220519  PLH Initial version

import hw_battery

class Battery():
    "Battery functions"
    # Battery model X.y
    BATTERY_CAPACITY = 3350 # mAh
    BATTERY_CAPACITY = 500 # mA
    BATTERY_MAX_TIME = BATTERY_CAPACITY / BATTERY_CAPACITY  # hours

    # voltage for battery chage percents
    V_100 = 4.1     # 100 %
    V_90 = 4.0      #  90 %
    V_10 = 3.6      #  10 %
    V_0 = 3.0       #   0 %

    voltage = None

    def get_voltage(self):
        "Get voltage from hw"
        self.voltage = hw_battery.get_voltage()
        return self.voltage

    def charge(self, myvoltage=None):
        "get the charge percent of the battery"
        if not myvoltage:
            myvoltage = self.voltage
        #print("Volt", myvoltage)
        if myvoltage > Battery.V_100:
            return 1.0
        if myvoltage > Battery.V_90:
            return 0.9 + (myvoltage-Battery.V_90)/(Battery.V_100-Battery.V_90)*0.1
        if myvoltage > Battery.V_10:
            return 0.1 + (myvoltage-Battery.V_10)/(Battery.V_90-Battery.V_10)*0.8
        if myvoltage > Battery.V_0:
            return 0.0 + (myvoltage-Battery.V_0)/(Battery.V_10-Battery.V_0)*0.1
        return 0

    def battery_time(self, charge=None, voltage=None):
        "get the ret time in minutes"
        # if parameter existing use it
        if not charge:
            if not voltage:
                voltage = self.get_voltage()
            charge= self.charge(voltage)
        rest_time = Battery.BATTERY_MAX_TIME * charge * 60
        return rest_time
