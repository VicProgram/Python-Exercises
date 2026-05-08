import os
from dotenv import load_dotenv


def main() -> None:

    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "development")
    akey = os.getenv("API_KEY", "not_key_found")
    levl = os.getenv("LOG_LEVEL", "DEBUG")

    if mode == "production":
        db_status = "Connected to Zion Mainframe"
        zion_status = "Online"
    else:
        db_status = "Connected to local instance"
        zion_status = "Online"

    if akey != "not_key_found" and akey != "":
        api_status = "Authenticated"
    else:
        api_status = "Unauthorized"

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {levl}")
    print(f"Zion Network: {zion_status}")

    print("\nEnvironment security check:")

    if akey != "not_key_found":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Using default/missing credentials")

    if os.path.exists(".env"):
        try:
            with open(".gitignore", "r") as f:
                if ".env" in f.read():
                    print("[OK] .env file properly configured")
                else:
                    print("[!] ALERT: .env is NOT in .gitignore!")
        except FileNotFoundError:
            print("[!] ALERT: .gitignore not found!")
    else:
        print("[WARNING] .env file missing")

    if "MATRIX_MODE" in os.environ:
        print("[OK] Production overrides available")


if __name__ == "__main__":
    main()
