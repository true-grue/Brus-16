// Author: Peter Sovietov
#include "brus16_cpu.h"

int16_t sext(uint16_t val, int bits) {
    uint16_t sign_mask = 1 << (bits - 1);
    return (val ^ sign_mask) - sign_mask;
}

uint16_t get_field(uint16_t val, uint16_t pos, int size) {
    return (val >> pos) & ((1 << size) - 1);
}

void push(struct CPU *cpu, uint16_t x) {
    cpu->stack[cpu->sp] = x;
    cpu->sp = (cpu->sp + 1) & (STACK_SIZE - 1);
}

uint16_t pop(struct CPU *cpu) {
    cpu->sp = (cpu->sp - 1) & (STACK_SIZE - 1);
    return cpu->stack[cpu->sp];
}

void rpush(struct CPU *cpu, uint16_t x) {
    cpu->rstack[cpu->rp] = x;
    cpu->rp = (cpu->rp + 1) & (RSTACK_SIZE - 1);
}

uint16_t rpop(struct CPU *cpu) {
    cpu->rp = (cpu->rp - 1) & (RSTACK_SIZE - 1);
    return cpu->rstack[cpu->rp];
}

uint16_t exec_alu(struct CPU *cpu, uint8_t op, int has_imm, int16_t simm9) {
    uint16_t y = has_imm ? (uint16_t) simm9 : pop(cpu);
    uint16_t x = pop(cpu);
    switch (op) {
    case OP2_ADD:
        return x + y;
    case OP2_SUB:
        return x - y;
    case OP2_MUL:
        return (int16_t) x * (int16_t) y;
    case OP2_AND:
        return x & y;
    case OP2_OR:
        return x | y;
    case OP2_XOR:
        return x ^ y;
    case OP2_SHL:
        return x << y;
    case OP2_SHR:
        return x >> y;
    case OP2_SHRA:
        return (int16_t) x >> y;
    case OP2_EQ:
        return x == y;
    case OP2_NEQ:
        return x != y;
    case OP2_LT:
        return (int16_t) x < (int16_t) y;
    case OP2_LE:
        return (int16_t) x <= (int16_t) y;
    case OP2_GT:
        return (int16_t) x > (int16_t) y;
    case OP2_GE:
        return (int16_t) x >= (int16_t) y;
    case OP2_LTU:
        return x < y;
    }
    return 0;
}

uint16_t exec_f1(struct CPU *cpu, uint16_t val, uint16_t new_pc) {
    uint8_t op = get_field(val, OP1_POS, OP1_SIZE);
    uint16_t imm13 = get_field(val, IMM_POS, IMM_SIZE);
    switch (op) {
    case OP1_JMP:
        return imm13;
    case OP1_JZ:
        return pop(cpu) ? new_pc : imm13;
    case OP1_CALL:
        rpush(cpu, new_pc);
        return imm13;
    case OP1_PUSHU: default:
        push(cpu, imm13);
        return new_pc;
    }
}

uint16_t exec_f2(struct CPU *cpu, uint16_t val, uint16_t new_pc) {
    uint8_t op = get_field(val, OP2_POS, OP2_SIZE);
    int has_imm = get_field(val, I_POS, I_SIZE);
    uint16_t simm9 = sext(get_field(val, SIMM_POS, SIMM_SIZE), SIMM_SIZE);
    if (op <= OP2_LTU) {
        push(cpu, exec_alu(cpu, op, has_imm, simm9));
        return new_pc;
    }
    switch (op) {
    case OP2_LOAD: {
        uint16_t addr = (has_imm ? cpu->fp : pop(cpu)) + simm9;
        cpu->mr = cpu->data[addr & (DATA_SIZE - 1)];
        break;
    }
    case OP2_STORE: {
        uint16_t addr = (has_imm ? cpu->fp : pop(cpu)) + simm9;
        cpu->data[addr & (DATA_SIZE - 1)] = pop(cpu);
        break;
    }
    case OP2_LOCALS:
        cpu->fp -= simm9;
        break;
    case OP2_RET:
        cpu->fp += simm9;
        return rpop(cpu);
    case OP2_PUSH:
        push(cpu, simm9);
        break;
    case OP2_PUSH_MR:
        push(cpu, cpu->mr);
        break;
    case OP2_SET_FP:
        cpu->fp = pop(cpu);
        break;
    case OP2_WAIT:
        cpu->wait = 1;
        break;
    }
    return new_pc;
}

void step(struct CPU *cpu) {
    if (!cpu->wait) {
        uint16_t val = cpu->code[cpu->pc];
        uint16_t new_pc = cpu->pc + 1;
        if (get_field(val, F_POS, F_SIZE)) {
            new_pc = exec_f1(cpu, val, new_pc);
        } else {
            new_pc = exec_f2(cpu, val, new_pc);
        }
        cpu->pc = new_pc & (CODE_SIZE - 1);
    }
}
