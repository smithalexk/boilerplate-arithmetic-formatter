# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))


# Run unit tests automatically
main(module='test_module', exit=False)