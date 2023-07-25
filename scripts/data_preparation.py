import random
from pathlib import Path


def main():
    random.seed(42)

    positive_words_file_path = Path("../data/positive-words.txt")
    negative_words_file_path = Path("../data/negative-words.txt")

    with open(positive_words_file_path, "r") as f:
        positive_words = f.read().splitlines()
        positive_words = random.sample(positive_words, 2000)

        with open("../data/positive-words-sample.txt", "w") as f2:
            for word in positive_words:
                f2.write(word + "\n")

    with open(negative_words_file_path, "r") as f:
        negative_words = f.read().splitlines()
        negative_words = random.sample(negative_words, 2000)

        with open("../data/negative-words-sample.txt", "w") as f2:
            for word in negative_words:
                f2.write(word + "\n")


if __name__ == "__main__":
    main()
