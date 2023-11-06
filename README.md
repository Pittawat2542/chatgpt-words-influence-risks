# Breaking Bad: Unraveling Influences and Risks of User Inputs on ChatGPT for Game Story Generation ([Paper](https://link.springer.com/chapter/10.1007/978-3-031-47658-7_27))

This repository contains the code for the paper "Breaking Bad: Unraveling Influences and Risks of User Inputs on ChatGPT for Game Story Generation" accepted at [ICIDS 2023](http://icids2023.ardin.online).

## Authors
Pittawat Taveekitworachai, Febri Abdullah, Mustafa Can Gursesli, Mury F. Dewantoro, Siyuan Chen, Antonio Lanata, Andrea Guazzini, and Ruck Thawonmas

## Abstract

This study presents an investigation into the influence and potential risks of using user inputs as part of a prompt, a message used to interact with ChatGPT. We demonstrate the influence of user inputs in a prompt through game story generation and story ending classification. To assess risks, we utilize a technique called adversarial prompting, which involves deliberately manipulating the prompt or parts of the prompt to exploit the safety mechanisms of large language models, leading to undesirable or harmful responses. We assess the influence of positive and negative sentiment words, as proxies for user inputs in a prompt, on the generated story endings. The results suggest that ChatGPT tends to adhere to its guidelines, providing safe and non-harmful outcomes, i.e., positive endings. However, malicious intentions, such as "jailbreaking", can be achieved through prompting injection. These actions carry significant risks of producing unethical outcomes, as shown in an example. As a result, this study also suggests preliminary ways to mitigate these risks: content filtering, rare token-separators, and enhancing training datasets and _alignment processes_.

## File structure
- `main.py`: The main script for story generation and ending evaluation.
- `requirements.txt`: The requirements file for the project.
- `output/`: The directory containing the generated results from ChatGPT.
- `src/`: The directory containing utility files for `main.py`
- `data/`: The directory containing word lists used for data generation process.
- `scripts/data_preparation.ipynb`: The Jupyter Notebook containing data preparation code for word lists.

## Installation and Usage
0. Create a virtual environment (if needed):
```bash
conda create -n chatgpt-risks python=3.11
```
and activate it:
```bash
conda activate chatgpt-risks
```
1. Copy `.env.example` and rename it to `.env.`. Follow instructions on [this page](https://platform.openai.com/docs/api-reference/authentication) to obtain your own OpenAI API key.
2. Install the requirements:
```bash
pip install -r requirements.txt
```
3. Change `src/config.py` as needed
4. Run the script for data generation and evaluation:
```bash
python main.py
```

## Citation
```bib
@InProceedings{10.1007/978-3-031-47658-7_27,
  author="Taveekitworachai, Pittawat and Abdullah, Febri and Gursesli, Mustafa Can and Dewantoro, Mury F. and Chen, Siyuan and Lanata, Antonio and Guazzini, Andrea and Thawonmas, Ruck",
  editor="Holloway-Attaway, Lissa and Murray, John T.",
  title={{"Breaking Bad: Unraveling Influences and Risks of User Inputs to ChatGPT for Game Story Generation"}},
  booktitle="Interactive Storytelling",
  year="2023",
  publisher="Springer Nature Switzerland",
  address="Cham",
  pages="285--296",
  abstract="This study presents an investigation into the influence and potential risks of using user inputs as part of a prompt, a message used to interact with ChatGPT. We demonstrate the influence of user inputs in a prompt through game story generation and story ending classification. To assess risks, we utilize a technique called adversarial prompting, which involves deliberately manipulating the prompt or parts of the prompt to exploit the safety mechanisms of large language models, leading to undesirable or harmful responses. We assess the influence of positive and negative sentiment words, as proxies for user inputs in a prompt, on the generated story endings. The results suggest that ChatGPT tends to adhere to its guidelines, providing safe and non-harmful outcomes, i.e., positive endings. However, malicious intentions, such as ``jailbreaking'', can be achieved through prompting injection. These actions carry significant risks of producing unethical outcomes, as shown in an example. As a result, this study also suggests preliminary ways to mitigate these risks: content filtering, rare token-separators, and enhancing training datasets and alignment processes.",
  isbn="978-3-031-47658-7"
}
```
