import re


def arithmetic_arranger(problems, answer_flag=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    illegal_operators = ["*", "/"]
    # Could also use regex here...
    if any(i_o in p for p in problems for i_o in illegal_operators):
        return "Error: Operator must be '+' or '-'."

    if any(re.search("[A-Za-z]+", x) for x in problems):
        return "Error: Numbers must only contain digits."

    if any(re.search("[0-9]{5,}", x) for x in problems):
        return "Error: Numbers cannot be more than four digits."

    first_number = [re.search("^([0-9]+)", x).group(0) for x in problems]
    operator = [re.search("[+-]", x).group(0) for x in problems]
    second_number = [re.search("([0-9]+)$", x).group(0) for x in problems]
    if answer_flag:
        answers = [
            str(int(x) + int(y)) if op == "+" else str(int(x) - int(y))
            for x, y, op in zip(first_number, second_number, operator)
        ]

        number_size = [
            max([len(idx), len(jdx), len(zdx)-2]) + 2
            for idx, jdx, zdx in zip(first_number, second_number, answers)
        ]

    else:
        number_size = [
            max([len(idx), len(jdx)]) + 2
            for idx, jdx in zip(first_number, second_number)
        ]

    last_line = []
    for idx, num in enumerate(first_number):
        first_number[idx] = f"{num:>{number_size[idx]}}"
        second_number[
            idx
        ] = f"{operator[idx]} {second_number[idx]:>{number_size[idx]-2}}"
        last_line.append("-" * number_size[idx])
        if answer_flag:
            answers[idx] = f"{answers[idx]:>{number_size[idx]}}"
    
    lines = [
        "    ".join(first_number),
        "    ".join(second_number),
        "    ".join(last_line),
    ]

    if answer_flag:
        lines.append("    ".join(answers))

    return "\n".join(lines)