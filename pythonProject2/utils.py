from data import COMPATIBILITY_RULES

def check_compatibility(components):
    result_text = ""
    is_compatible = True
    if "cpu" in components and "motherboard" in components:
        cpu = components['cpu']
        motherboard = components['motherboard']
        if cpu not in COMPATIBILITY_RULES["cpu"] or motherboard not in COMPATIBILITY_RULES["cpu"][cpu]:
            result_text += "Несовместимость процессора и материнской платы.\n"
            is_compatible = False
    if "ram" in components and "motherboard" in components:
        ram = components['ram']
        motherboard = components['motherboard']
        if ram not in COMPATIBILITY_RULES["ram"] or motherboard not in COMPATIBILITY_RULES["ram"][ram]:
            result_text += "Несовместимость оперативной памяти и материнской платы.\n"
            is_compatible = False
    if is_compatible:
        result_text += "Все компоненты совместимы.\n"
    return result_text