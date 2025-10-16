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
    case OP_ADD:
        return x + y;
    case OP_SUB:
        return x - y;
    case OP_MUL:
        return (int16_t) x * (int16_t) y;
    case OP_AND:
        return x & y;
    case OP_OR:
        return x | y;
    case OP_XOR:
        return x ^ y;
    case OP_SHL:
        return x << y;
    case OP_SHR:
        return x >> y;
    case OP_SHRA:
        return (int16_t) x >> y;
    case OP_EQ:
        return x == y;
    case OP_NEQ:
        return x != y;
    case OP_LT:
        return (int16_t) x < (int16_t) y;
    case OP_LE:
        return (int16_t) x <= (int16_t) y;
    case OP_GT:
        return (int16_t) x > (int16_t) y;
    case OP_GE:
        return (int16_t) x >= (int16_t) y;
    case OP_LTU:
        return x < y;
    }
    return 0;
}

uint16_t exec_f1(struct CPU *cpu, uint16_t val, uint16_t new_pc) {
    uint8_t op = get_field(val, F1_OP_POS, F1_OP_SIZE);
    uint16_t imm13 = get_field(val, F1_IMM_POS, F1_IMM_SIZE);
    switch (op) {
    case OP_JMP:
        return imm13;
    case OP_JZ:
        return pop(cpu) ? new_pc : imm13;
    case OP_CALL:
        rpush(cpu, new_pc);
        return imm13;
    case OP_PUSH_ADDR: default:
        push(cpu, imm13);
        return new_pc;
    }
}

uint16_t exec_f2(struct CPU *cpu, uint16_t val, uint16_t new_pc) {
    uint8_t op = get_field(val, F2_OP_POS, F2_OP_SIZE);
    int has_imm = get_field(val, F2_I_POS, F2_I_SIZE);
    uint16_t simm9 = sext(get_field(val, F2_SIMM_POS, F2_SIMM_SIZE), F2_SIMM_SIZE);
    if (op <= OP_LTU) {
        push(cpu, exec_alu(cpu, op, has_imm, simm9));
        return new_pc;
    }
    switch (op) {
    case OP_LOAD: {
        uint16_t addr = has_imm ? (cpu->fp + simm9) : pop(cpu);
        cpu->mr = cpu->data[addr & (DATA_SIZE - 1)];
        break;
    }
    case OP_STORE: {
        uint16_t addr = has_imm ? (cpu->fp + simm9) : pop(cpu);
        cpu->data[addr & (DATA_SIZE - 1)] = pop(cpu);
        break;
    }
    case OP_LOCALS:
        cpu->fp -= simm9;
        break;
    case OP_RET:
        cpu->fp += simm9;
        return rpop(cpu);
    case OP_PUSH_INT:
        push(cpu, simm9);
        break;
    case OP_PUSH_MR:
        push(cpu, cpu->mr);
        break;
    case OP_SET_FP:
        cpu->fp = pop(cpu);
        break;
    case OP_WAIT:
        cpu->wait = 1;
        break;
    }
    return new_pc;
}

void step(struct CPU *cpu) {
    if (cpu->wait) {
        return;
    }
    uint16_t val = cpu->code[cpu->pc];
    uint16_t new_pc = (cpu->pc + 1) & (CODE_SIZE - 1);
    if (get_field(val, F1_F_POS, F1_F_SIZE)) {
        new_pc = exec_f1(cpu, val, new_pc);
    } else {
        new_pc = exec_f2(cpu, val, new_pc);
    }
    cpu->pc = new_pc;
}
