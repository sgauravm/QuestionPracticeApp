import streamlit as st
import os
import json


# Function to load questions from a JSON file
def load_questions_from_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def main():
    st.title("GMAT Practice Questions")

    # Path to the folder containing the question files
    questions_folder = "questions"

    # Get a list of all JSON files in the questions folder
    question_files = {
        os.path.splitext(f)[0].capitalize().replace("_", " "): f
        for f in os.listdir(questions_folder)
        if f.endswith(".json")
    }

    # Dropdown menu to select a file
    selected_file_name = st.selectbox("Select a question file", question_files)

    # Load questions from the selected file
    if selected_file_name:
        questions = load_questions_from_json(
            os.path.join(questions_folder, question_files[selected_file_name])
        )

        # Display questions
        for i, q in enumerate(questions):
            st.subheader(f"Question {i + 1}")
            st.write(q["question"])

            # Create a radio button for options
            selected_option = st.radio(
                "Select an option:",
                q["options"],
                index=None,
                key=f"question_{i}",  # No option is selected initially
            )

            # Button to show the solution
            if st.button(f"Show Solution for Question {i + 1}", key=f"solution_{i}"):
                if selected_option == q["correct"]:
                    st.success("Correct! \n\n" + q["solution"].replace("\n", " \n"))
                else:
                    st.error("Incorrect. \n\n" + q["solution"].replace("\n", " \n"))


if __name__ == "__main__":
    main()
