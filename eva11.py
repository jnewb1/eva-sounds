SOUNDS = [
    "dont_forget_your_keys",
    "headlights_are_on",
    "please_fasten_your_seatbelts",
    "a_door_is_ajar",
    "parking_brake_is_on",
    "fuel",
    "engine_oil_pressure",
    "washer_fluid",
    "prompt_service_is_required",
    "engine_is_overheating",
    "electrical_system_is_malfunctioning",
    "all_monitored_systems_are_functioning",
    "thank_you",
    "your",
    "is_low",
]

with open("cm73002", "rb") as f:
    dat = f.read()
    
    # for the eva 11, the offset table is at the end! move it to the front to match

    dat = dat[-32:] + dat[:-32]
