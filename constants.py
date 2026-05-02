# Параметры выражений
MATH_OPERATORS: list[str] = ["+", "-", "%", "//"]
MIN_NUM_OPERANDS: int = 2
MAX_NUM_OPERANDS: int = 5
MIN_VALUE: int = -100
MAX_VALUE: int = 100

# Сообщения и значение счетчика жизней
NUM_LIVES: int = 5
EXCHANGE_RATE: int = 3
LIVES_EXCHANGE_MSG: str = (
    f"За каждые {EXCHANGE_RATE} правильных "
    "ответа начисляется дополнительная жизнь!"
)
LIVES_COUNT_TEXT: str = "Количество жизней:"
START_MSG: str = (
    "Тренажер вычисления выражений c // и % начинает свою работу!"
)
WRONG_INPUT_TYPE_MSG: str = "Введенное значение не является целым числом!"
CORRECT_ANSWER_MSG: str = "Верно!"
INCORRECT_ANSWER_MSG: str = "Неверно! Правильный ответ: "
PROMPT_MSG: str = "Посчитай в уме и напиши ответ: "
FORCED_END_COMMAND: str = "stop"
FORCED_END_MSG: str = (
    f"Чтобы закончить упражнение, набери {FORCED_END_COMMAND}."
)
RULES_MSG: str = (
    f"1) {LIVES_EXCHANGE_MSG}\n"
    f"2) {FORCED_END_MSG}"
)
END_MSG: str = "Итоги игры:"
TOTAL_ANSWERS_MSG: str = "Получено ответов: "
STATISTICS_MSG: str = "% правильных ответов."

# Разметка и визуал
LIFE_SYMBOL: str = "❤️"
NO_LIVES_MSG: str = "⭕️"
LINE_SYMBOL: str = "="
LINE_SIZE: int = 80
