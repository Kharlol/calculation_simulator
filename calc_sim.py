from random import choices, randint

from constants import *


def generate_expression() -> str:
    """
    Генерирует выражение из случайных значений.
    Допустимые значения и операторы заданы константами.
    """
    num_operands = randint(MIN_NUM_OPERANDS, MAX_NUM_OPERANDS)
    operands = [
        str(randint(MIN_VALUE, MAX_VALUE)) for _ in range(num_operands)
    ]

    num_operators = num_operands - 1
    operators = choices(MATH_OPERATORS, k=num_operators)
    operators.append("")

    expression = (
        " ".join(
            f"{num} {symbol}" for num, symbol in zip(operands, operators)
        )
    )
    return expression


def compare_results(expression: str, user_input: str) -> bool:
    """Проверяет корректность введенного ответа."""
    res = eval(expression)

    try:
        answer = int(user_input)
    except ValueError:
        print(WRONG_INPUT_TYPE_MSG)
        return False

    if res == answer:
        print(CORRECT_ANSWER_MSG)
        return True
    else:
        print(f"{INCORRECT_ANSWER_MSG}{res}")
        return False


def calculation_simulator():
    total_answers: int = 0
    correct_answers: int = 0
    num_lives = NUM_LIVES
    print(LINE_SYMBOL * LINE_SIZE)
    print(
        START_MSG.center(LINE_SIZE), RULES_MSG,
        sep="\n" + LINE_SYMBOL * LINE_SIZE + "\n",
    )
    while num_lives >= 0:
        print(
            LINE_SYMBOL * LINE_SIZE,
            LIVES_COUNT_TEXT.center(LINE_SIZE),
            (LIFE_SYMBOL * num_lives or NO_LIVES_MSG).center(LINE_SIZE),
            sep="\n",
            end="\n\n",
        )
        task = generate_expression()
        # print(f"Подсмотреть ответ: {eval(task)}".rjust(LINE_SIZE))
        print(PROMPT_MSG, task.rjust(LINE_SIZE // 2), end=" = ".ljust(0))
        user_answer = input()
        if user_answer.strip().lower() == FORCED_END_COMMAND:
            break
        total_answers += 1
        if compare_results(task, user_answer):
            correct_answers += 1
            if not correct_answers % EXCHANGE_RATE:
                num_lives += 1
        else:
            num_lives -= 1

    print(LINE_SYMBOL * LINE_SIZE)
    print(f"{END_MSG.center(LINE_SIZE)}",
          f"{TOTAL_ANSWERS_MSG}{total_answers}.",
          sep="\n",
    )
    if total_answers > 0:
        print(
            f"{round(correct_answers / total_answers * 100, 2)}"
            f"{STATISTICS_MSG}"
        )
    print(LINE_SYMBOL * LINE_SIZE)


if __name__ == "__main__":
    calculation_simulator()
