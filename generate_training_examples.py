import random

code_structures = [
    "for i in range(10):",
    "if x > 0:",
    "def my_function():",
    "while condition:",
    "class MyClass:",
]

code_actions = [
    "verifique o código para erros.",
    "examine meu código em busca de problemas.",
    "há algum erro no meu código?",
]

num_examples = 10

generated_examples = []
while len(generated_examples) < num_examples:
    code_structure = random.choice(code_structures)
    code_action = random.choice(code_actions)
    generated_example = f"{code_structure}  # {code_action}"

    if generated_example not in generated_examples:
        generated_examples.append(generated_example)

with open("nlu_training_data.md", "a") as file:
    for example in generated_examples:
        file.write(f"- {example}\n")
