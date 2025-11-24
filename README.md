# Brus-16

Brus-16 is an educational 16-bit game console with an original, minimalistic architecture.
Unlike fantasy consoles, Brus-16 was designed for FPGA implementation.

![](docs/images/fpga.jpg)

See in [action](https://github.com/true-grue/Brus-16-Apps).

![](docs/images/games.png)

## Architecture

Brus-16 consists of:

* **16-bit stack-based CPU**: Harvard architecture (8K words for code, 8K for data), two hardware stacks (values and return addresses), fixed instruction size. Designed to simplify compiler development.
* **Graphics processor**: Renders 64 filled rectangles per frame without a framebuffer. 640x480x16bpp, 60 fps.
* **Input controller**: Supports 16 buttons.

The ISA is described [here](https://true-grue.github.io/Brus-16/isa.html).

## Software Tools

There is a basic set of tool templates:

* Compiler (`brus16_dsl.py`): translates from a Python-like DSL to Brus-16 assembly.
* Assembler (`brus16_asm.py`): translates assembly into a binary image.
* Emulator (`brus16_cpu.c`, `brus16_emu.c`): software model of the console using the SDL3 library.

## Educational Projects

Brus-16 can be used for various educational projects. Examples:

- Develop a software emulator in another language (e.g., Rust, Go).
- Create an interactive debugger with stack and memory visualization.
- Write a full-featured assembler with macros and directives.
- Extend the existing compiler (for-loops, multiple return values).
- Implement new compiler optimizations (e.g., value numbering).
- Develop a compiler for another language (e.g., a subset of C or Forth).
- Create a graphics editor for drawing game assets with rectangles.
- Develop a tool to approximate a raster image with 64 rectangles.
- Design a new architectural variant of Brus-16 on an FPGA.
- And, of course, develop your own game!

A Verilog hardware implementation by Kirill Pavlov is available [here](https://github.com/Papr1ka/brus16).

---

# Брус-16

Брус-16 — это учебная 16-битная игровая приставка с оригинальной, минималистичной архитектурой.
В отличие от существующих fantasy consoles, Брус-16 проектировался с прицелом на аппаратную реализацию на ПЛИС.

## Архитектура

В состав Брус-16 входят:

* **16-битный стековый процессор**: гарвардская архитектура (8К слов для кода, 8К слов для данных), два аппаратных стека (для значений и адресов возврата), фиксированная длина команд. Архитектура процессора спроектирована для удобства написания простых компиляторов. 
* **Графический процессор**: обрабатывает 64 закрашенных прямоугольника на кадр без использования видеобуфера. Характеристики графики: 640x480x16bpp, 60 fps.
* **Контроллер ввода**: поддерживает 16 кнопок.

Система команд oписана [здесь](https://true-grue.github.io/Brus-16/isa.html).

## Программные инструменты

Имеется базовый набор инструментов-заготовок:

* Компилятор (`brus16_dsl.py`): Транслирует код с Python-подобного DSL в язык ассемблера Брус-16.
* Ассемблер (`brus16_asm.py`): Транслирует ассемблерный код в бинарную прошивку.
* Эмулятор (`brus16_cpu.c`, `brus16_emu.c`): Программная модель приставки с использованием библиотеки SDL3.

## DSL для разработки игр

Краткое описание DSL находится [здесь](docs/dsl_ru.md).

## Учебные проекты

Брус-16 может быть основой учебных проектов различной сложности. Вот несколько примеров задач для студентов:

* Разработать программный эмулятор на другом языке (например, Rust или Go).
* Создать интерактивный отладчик с визуализацией стеков и памяти.
* Написать полноценный ассемблер с поддержкой макросов и директив.
* Доработать существующий компилятор (цикл for, несколько возвращаемых значений).
* Добавить новые оптимизации в компилятор (например, value numbering).
* Разработать компилятор для другого языка (например, подмножества C или Forth).
* Создать графический редактор для рисования игровых объектов прямоугольниками.
* Разработать инструмент, аппроксимирующий растровое изображение 64 прямоугольниками.
* Разработать новый архитектурный вариант Брус-16 на ПЛИС.
* И, конечно же, разработать свою игру!

Аппаратная реализация приставки на Verilog от Кирилла Павлова находится [здесь](https://github.com/Papr1ka/brus16).
