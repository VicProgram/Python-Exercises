import os
import dotenv
import sys


def main() -> None:

    dotenv.load_dotenv()

    mode = os.getenv("MATRIX_MODE")
    ddbb = os.getenv("DATABASE_URL")
    akey = os.getenv("API_KEY")
    levl = os.getenv("LOG_LEVEL")
    endp = os.getenv("ZION_ENDPOINT")
        



if __name__ == "__main__" :
    main()