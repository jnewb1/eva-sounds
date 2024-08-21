import os
import subprocess


with open("cm63002", "rb") as f:
    dat = f.read()


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


SOUNDS = {sound: int.from_bytes(dat[i*2:i*2+2], "little") for i, sound in enumerate(SOUNDS)}
SOUNDS = {sound: (offset, (list(SOUNDS.values())[i+1] - list(SOUNDS.values())[i]) if i < (len(SOUNDS) - 1) else len(dat)) for i, (sound, offset) in enumerate(SOUNDS.items())}


TI_LPC_CMD_VER_DIR = "../ti_lpc/cmd_line_vers"

os.makedirs("sounds", exist_ok=True)

for sound, (offset, size) in SOUNDS.items():
    sound_data = dat[offset:offset+size]
    hex_data = ','.join(sound_data.hex()[i:i+2].upper() for i in range(0, len(sound_data.hex()), 2))

    with open(f"sounds/{'_'.join(sound.split())}.wav", "wb") as f:
        cmd = f"./ti_lpc_cmd mode=render chip=tms5110.txt strhex={hex_data}"
        print(cmd)
        ret = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=TI_LPC_CMD_VER_DIR)

        if ret.returncode == 1 or ret.stderr:
            print(ret.stdout)
            print(ret.stderr)
            exit(1)
        else:
            f.write(open(os.path.join(TI_LPC_CMD_VER_DIR, "zzzout.wav"), "rb").read())
