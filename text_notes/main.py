import pywhatkit as pw

def main():
    print("Text to handwritten notes in Python : ")
    text = "Python is a high-level, interpreted programming language known for its simplicity and readability. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability and syntax that allows programmers to express concepts in fewer lines of code compared to languages like C++ or Java."
    pw.text_to_handwriting(text, "python.png", [0, 45, 85])
    print("Ended.")

if __name__ == "__main__":
    main()
