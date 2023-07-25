from pathlib import Path

IS_POSITIVE_WORDS = True
MAX_NUM_STORIES = 100
MODEL = "gpt-3.5-turbo"
TEMPERATURE = 1
OUTPUT_DIR_PATH = Path("outputs")
STORIES_FILE_PATH = Path(f"{OUTPUT_DIR_PATH}/game_stories.json")
EVALUATION_FILE_PATH = Path(f"{OUTPUT_DIR_PATH}/evaluations.json")
SUMMARY_FILE_PATH = Path(f"{OUTPUT_DIR_PATH}/summary.json")