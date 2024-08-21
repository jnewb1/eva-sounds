SOUNDS = [
    "please close your right rear door",
    "please close your left rear door",
    "please close your passenger door",
    "please close your driver door",
    "please close your trunk lid",
    "please close yout rear hatch",
    "your engine oil pressure is critical engine damage may occur",
    "your engine is overheating prompt service is required",
    "please check your engine coolant level",
    "please check your fuel level",
    "please check your transmission fluid level",
    "your charging system is malfunctioning prompt service is required",
    "please check your brake fluid level",
    "please check your disc brake pads",
    "your washer fluid is low",
    "your rear washer fluid is low",
    "please check your engine oil level",
    "please check your headlands",
    "please check your brake lamps",
    "please check your tail lamps",
    "your parking brake is on",
    "your keys are in the ignition",
    "your headlamps are on",
    "your engine temperature is above normal",
    "all monitored systems are functioning",
    "please fasten your seatbelts",
    "thank you",
    "decay",
    "long beeps",
    "short beeps"
]

with open("cm63002", "rb") as f:
    dat = f.read()
    header = dat[:60]