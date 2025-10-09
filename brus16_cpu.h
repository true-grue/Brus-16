#ifndef BRUS16_CPU_H
#define BRUS16_CPU_H

#include <stdint.h>

#define CODE_SIZE 8192
#define DATA_SIZE 8192
#define STACK_SIZE 32
#define RSTACK_SIZE 16

enum {
    OP_JMP,
    OP_JZ,
    OP_CALL,
    OP_PUSH_ADDR
};

enum {
    OP_ADD,
    OP_SUB,
    OP_MUL,
    OP_AND,
    OP_OR,
    OP_XOR,
    OP_SHL,
    OP_SHR,
    OP_SHRA,
    OP_EQ,
    OP_NEQ,
    OP_LT,
    OP_LE,
    OP_GT,
    OP_GE,
    OP_LTU,
    OP_LOAD,
    OP_STORE,
    OP_LOCALS,
    OP_SET_FP,
    OP_ICALL,
    OP_RET,
    OP_PUSH_INT,
    OP_PUSH_MR,
    OP_POP,
    OP_WAIT
};

struct CPU {
    uint16_t code[CODE_SIZE];
    uint16_t data[DATA_SIZE];
    uint16_t stack[STACK_SIZE];
    uint16_t rstack[RSTACK_SIZE];
    uint16_t pc;
    uint16_t sp;
    uint16_t rp;
    uint16_t fp;
    uint16_t mr;
    int wait;
};

int16_t sext(uint16_t val, int bits);
void step(struct CPU * cpu);

#endif
