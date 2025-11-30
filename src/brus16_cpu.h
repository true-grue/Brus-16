#ifndef BRUS16_CPU_H
#define BRUS16_CPU_H

#include <stdint.h>
#include "brus16_cfg.h"

struct CPU {
    uint16_t code[CODE_SIZE];
    uint16_t data[DATA_SIZE];
    uint16_t stack[STACK_SIZE];
    uint16_t rstack[RSTACK_SIZE];
    uint16_t pc;
    uint16_t sp;
    uint16_t rp;
    uint16_t fp;
    uint16_t addr;
    int wait;
};

int16_t sext(uint16_t val, int bits);
void step(struct CPU *cpu);

#endif
