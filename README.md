# eva-sounds
pulling sounds from the chrysler EVA alert system

based on work from [BrerDawg](https://github.com/BrerDawg) in [ti_lpc](https://github.com/BrerDawg/ti_lpc)

also uses ROM which was dumped by [plgDavid](https://www.youtube.com/@plgDavid) in [Preserving the Chrysler Electronic Voice Alert (EVA)](https://www.youtube.com/watch?v=8DwKqCZlKnw)

huge thanks to them!

[![demo video](https://img.youtube.com/vi/e0SVRuqicng/0.jpg)](https://www.youtube.com/shorts/e0SVRuqicng)


Notes:
- for eva11, the offset table is at the end of the ROM, where as in eva24, it's in the front.
- eva11 splits the messages up, so for example "is low" is a separate message from "fuel" and "washer_fluid". on eva24, they are combined into one message.
