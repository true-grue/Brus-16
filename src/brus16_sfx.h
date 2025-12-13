#ifndef BRUS16_SFX_H
#define BRUS16_SFX_H

#include <stdint.h>
#include "brus16_cfg.h"

struct OSC {
    uint16_t amp;
    uint16_t target_amp;
    uint16_t decay;
    uint16_t step;
    uint16_t phase;
};

struct SFX {
    struct OSC oscs[OSC_NUM];
    int decay_counter;
};

void sfx_update(uint16_t *osc_addr, struct SFX *sfx);
int16_t sfx_process(struct SFX *sfx);

#endif
