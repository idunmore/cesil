# Command Line Interface

import click
from .cesil import CESIL
from .cesil import CESILException

@click.command()
@click.option('-s', '--source',
              type=click.Choice(['t', 'text', 'c', 'card'],
                                case_sensitive=False),
              default='text', show_default=True, help='Text or Card input.')
@click.option('-d', '--debug',
              type=click.Choice(['0', '1', '2', '3', '4'],
                                case_sensitive=False),
              default='0', show_default=True,
              help='Debug mode/verbosity level.')
@click.option('-p', '--plus', is_flag=True, default=False,
              help='Enables "plus" mode language extensions.')
@click.version_option('0.9.5')
@click.argument('source_file', type=click.Path(exists=True))
def cesilplus(source: str, debug: int, plus: bool, source_file: str):
    """CESILPlus - CESIL Interpreter (w/ optional language extentions).
    
    \b
      CESIL: Computer Eduction in Schools Instruction Language

      "Plus" language extensions add a STACK, SUBROUTINE support, MODULO
    division, RANDOM number generation, integer INPUT, ASCII character output,
    and INC/DEC functions to the language, enabled with the -p | --plus options.
    Extensions are DISABLED by default.

      "Plus" Mode - Extension instructions:

    \b
        MODULO  operand - MODULO division of ACCUMULATOR by operand
                          (sets ACCUMULATOR to REMAINDER)
        RANDOM  operand - Generates a RANDOM number between 0 and the
                          value of operand and puts it in the ACCUMULATOR
    \b
        PUSH            - PUSHes the ACCUMULATOR value on to STACK
        POP             - POPs top value from STACK into the ACCUMULATOR
    \b
        INC             - Increments the ACCUMULATOR by 1
        DEC             - Decrements the ACCUMULATOR by 1
    \b
        INPUTN          - Accepts an INTEGER from the CONSOLE and places the
                          value in the ACCUMULATOR
    \b
        OUTCHAR         - Outputs the ACCUMULATOR value as an ASCII character
    \b
        JUMPSR  label   - Jumps to SUBROUTINE @ label
        JSIZERO label   - Jumps to SUBROUTINE @ label if ACCUMULATOR = 0
        JSINEG  label   - Jumps to SUBROUTINE @ label if ACCUMULATOR < 0
        RETURN          - Returns from SUBROUTINE and continues execution
    """

    try:
        cesil_interpreter = CESIL(plus, int(debug))
        cesil_interpreter.load(source_file, source)
        cesil_interpreter.run()
    except CESILException as err:
        err.print()
