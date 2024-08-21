import os
import subprocess


def read_offsets_from_pointers(sounds, dat):
    sounds_offsets = {sound: int.from_bytes(dat[i*2:i*2+2], "little") for i, sound in enumerate(sounds)}
    return {sound: (offset+32, (list(sounds_offsets.values())[i+1] - list(sounds_offsets.values())[i])) for i, (sound, offset) in enumerate(sounds_offsets.items()) if i < len(sounds_offsets) - 1}


def generate_sounds(sounds, dat, name):
    sounds_offsets_and_sizes = read_offsets_from_pointers(sounds, dat)

    print(sounds_offsets_and_sizes)
    
    TI_LPC_CMD_VER_DIR = "../ti_lpc/cmd_line_vers"

    os.makedirs(f"sounds_{name}", exist_ok=True)

    for sound, (offset, size) in sounds_offsets_and_sizes.items():
        sound_data = dat[offset:offset+size]
        hex_data = ','.join(sound_data.hex()[i:i+2].upper() for i in range(0, len(sound_data.hex()), 2))

        with open(f"sounds_{name}/{'_'.join(sound.split())}.wav", "wb") as f:
            cmd = f"./ti_lpc_cmd mode=render chip=tms5110.txt strhex={hex_data}"
            print(cmd)
            ret = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=TI_LPC_CMD_VER_DIR)

            if ret.returncode == 1 or ret.stderr:
                print(ret.stdout)
                print(ret.stderr)
                exit(1)
            else:
                f.write(open(os.path.join(TI_LPC_CMD_VER_DIR, "zzzout.wav"), "rb").read())


import eva11
import eva24

generate_sounds(eva11.SOUNDS, eva11.dat, "eva11")
generate_sounds(eva24.SOUNDS, eva24.dat, "eva24")