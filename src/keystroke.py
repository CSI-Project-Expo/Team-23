import time

def capture_keystroke():
    print("\n--- Keystroke Behavior Capture ---")
    text = "securelogin"
    print(f"Type this word exactly: {text}")

    input("Press Enter when ready...")

    start_time = time.time()
    typed = input("Start typing: ")
    end_time = time.time()

    total_time = end_time - start_time

    if len(typed) > 0:
        avg_time = total_time / len(typed)
    else:
        avg_time = 0

    print("Average typing time per character:", avg_time)

    return [avg_time]


# IMPORTANT: This makes it run when executed directly
if __name__ == "__main__":
    pattern = capture_keystroke()
    print("Returned Pattern:", pattern)
