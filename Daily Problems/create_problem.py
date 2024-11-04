import os
import requests


def fetch_problem_info(problem_id):
    """
    Fetch only the title and difficulty of a problem using problem ID
    """
    # Get problem info from LeetCode API
    response = requests.get('https://leetcode.com/api/problems/all/')
    if response.status_code != 200:
        raise Exception(f"Failed to fetch problems list: {response.status_code}")

    problems_data = response.json()
    problem_info = next(
        (p for p in problems_data['stat_status_pairs']
         if str(p['stat']['frontend_question_id']) == str(problem_id)),
        None
    )

    if not problem_info:
        raise Exception(f"Problem {problem_id} not found")

    # Extract only needed information
    return {
        'title': problem_info['stat']['question__title'],
        'difficulty': ['Easy', 'Medium', 'Hard'][problem_info['difficulty']['level'] - 1],
        'question_id': problem_id
    }


def create_problem_structure(problem_info, base_dir):
    """
    Create problem folder with solution files in appropriate difficulty subfolder
    """
    question_id = problem_info['question_id']
    title = problem_info['title']
    difficulty = problem_info['difficulty']

    # Create directory name in format "XXXX. Title"
    dir_name = f"{question_id}. {title}"

    # Full path to problem directory
    problem_dir = os.path.join(base_dir, difficulty, dir_name)

    if not os.path.exists(problem_dir):
        # Create problem directory
        os.makedirs(problem_dir, exist_ok=True)

        # Create solution files
        solution_py = os.path.join(problem_dir, 'solution.py')
        solution_r = os.path.join(problem_dir, 'solution.R')

        # Create solution.py with basic template
        with open(solution_py, 'w', encoding='utf-8') as f:
            f.write(f"# Solution for Problem {question_id}: {title}\n")

        # Create solution.R with basic template
        with open(solution_r, 'w', encoding='utf-8') as f:
            f.write(f"# Solution for Problem {question_id}: {title}\n")

        print(f"Created problem folder: {dir_name}")
        print(f"Location: {problem_dir}")
    else:
        print(f"Problem already exists: {dir_name}")


def main():
    # Base directory for all problems
    base_directory = r"Daily Problems"

    while True:
        problem_id = input("Enter the LeetCode problem ID (or 'q' to quit): ")
        if problem_id.lower() == 'q':
            break

        try:
            print(f"\nFetching problem {problem_id}...")
            problem_info = fetch_problem_info(problem_id)

            print(f"Found problem: {problem_id}. {problem_info['title']}")
            print(f"Difficulty: {problem_info['difficulty']}")

            create_problem_structure(problem_info, base_directory)

        except Exception as e:
            print(f"Error processing problem {problem_id}: {str(e)}")

        print("\nWould you like to fetch another problem?")


if __name__ == "__main__":
    main()