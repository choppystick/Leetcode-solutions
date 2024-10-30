import os
import re


def sanitize_folder_name(name):
    """
    Sanitize folder name by removing/replacing invalid Windows characters
    """
    # Replace colons, question marks, and other invalid characters
    sanitized = re.sub(r'[<>:"/\\|?*]', '', name)
    # Replace multiple spaces with single space
    sanitized = re.sub(r'\s+', ' ', sanitized)
    # Remove leading/trailing spaces and periods
    sanitized = sanitized.strip('. ')
    return sanitized


def create_folder_structure():
    # Main directory
    root_dir = "D:\\Daily_Problems"

    # Create main directory
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    # Structure organized by difficulty
    structure = {
        "Easy": [
            "344. Reverse String",
            "409. Longest Palindrome",
            "1002. Find Common Characters",
            "1051. Height Checker",
            "1122. Relative Sort Array",
            "2037. Minimum Number of Moves to Seat Everyone",
            "1791. Find Center of Star Graph",
            "1550. Three Consecutive Odds",
            "350. Intersection of Two Arrays II",
            "2582. Pass the Pillow",
            "1518. Water Bottles",
            "1598. Crawler Log Folder",
            "1380. Lucky Numbers in a Matrix",
            "2418. Sort the People",
            "1636. Sort Array by Increasing Frequency",
            "2678. Number of Senior Citizens",
            "1460. Make Two Arrays Equal by Reversing Subarrays",
            "2053. Kth Distinct String in an Array",
            "703. Kth Largest Element in a Stream",
            "860. Lemonade Change",
            "476. Number Complement",
            "145. Binary Tree Postorder Traversal",
            "590. N-ary Tree Postorder Traversal",
            "1. Two Sum",
            "2022. Convert 1D Array Into 2D Array",
            "1945. Sum of Digits of String After Convert",
            "2220. Minimum Bit Flips to Convert Number",
            "1684. Count the Number of Consistent Strings",
            "884. Uncommon Words from Two Sentences",
            "1331. Rank Transform of an Array",
            "2696. Minimum String Length After Removing Substrings"
        ],
        "Medium": [
            "2486. Append Characters to String to Make Subsequence",
            "846. Hand of Straights",
            "648. Replace Words",
            "523. Continuous Subarray Sum",
            "974. Subarray Sums Divisible by K",
            "75. Sort Colors",
            "945. Minimum Increment to Make Array Unique",
            "633. Sum of Square Numbers",
            "826. Most Profit Assigning Work",
            "1482. Minimum Number of Days to Make m Bouquets",
            "1552. Magnetic Force Between Two Balls",
            "1052. Grumpy Bookstore Owner",
            "1248. Count Number of Nice Subarrays",
            "1438. Longest Continuous Subarray With Absolute Diff Less",
            "1038. Binary Search Tree to Greater Sum Tree",
            "1382. Balance a Binary Search Tree",
            "2285. Maximum Total Importance of Roads",
            "2192. All Ancestors of a Node in a Directed Acyclic Graph",
            "1509. Minimum Difference Between Largest and Smallest",
            "2181. Merge Nodes in Between Zeros",
            "2058. Find the Minimum and Maximum Number of Nod",
            "1823. Find the Winner of the Circular Game",
            "1701. Average Waiting Time",
            "1190. Reverse Substrings Between Each Pair of Parentheses",
            "1717. Maximum Score From Removing Substrings",
            "2196. Create Binary Tree From Descriptions",
            "2096. Step-By-Step Directions From a Binary Tree Node to",
            "1110. Delete Nodes And Return Forest",
            "1530. Number of Good Leaf Nodes Pairs",
            "1605. Find Valid Matrix Given Row and Column Sums",
            "2191. Sort the Jumbled Numbers",
            "912. Sort an Array",
            "1334. Find the City With the Smallest Number of Neighbo",
            "2976. Minimum Cost to Convert String I",
            "1395. Count Number of Teams",
            "1653. Minimum Deletions to Make String Balanced",
            "1105. Filling Bookcase Shelves",
            "2134. Minimum Swaps to Group All 1's Together II",
            "1508. Range Sum of Sorted Subarray Sums",
            "3016. Minimum Number of Pushes to Type Word II",
            "885. Spiral Matrix III",
            "840. Magic Squares In Grid",
            "959. Regions Cut By Slashes",
            "624. Maximum Distance in Arrays",
            "1937. Maximum Number of Points with Cost",
            "264. Ugly Number II",
            "650. 2 Keys Keyboard",
            "1140. Stone Game II",
            "592. Fraction Addition and Subtraction",
            "1905. Count Sub Islands",
            "947. Most Stones Removed with Same Row or Column",
            "1514. Path with Maximum Probability",
            "1894. Find the Student that Will Replace the Chalk",
            "874. Walking Robot Simulation",
            "2028. Find Missing Observations",
            "3217. Delete Nodes From Linked List Present in Array",
            "1367. Linked List in Binary Tree",
            "725. Split Linked List in Parts",
            "2326. Spiral Matrix IV",
            "2807. Insert Greatest Common Divisors in Linked List",
            "1310. XOR Queries of a Subarray",
            "2419. Longest Subarray With Maximum Bitwise AND",
            "1371. Find the Longest Substring Containing Vowels in",
            "539. Minimum Time Difference",
            "179. Largest Number",
            "241. Different Ways to Add Parentheses",
            "386. Lexicographical Numbers",
            "2707. Extra Characters in a String",
            "3043. Find the Length of the Longest Common Prefix",
            "729. My Calendar I",
            "731. My Calendar II",
            "641. Design Circular Deque",
            "1381. Design a Stack With Increment Operation",
            "1497. Check If Array Pairs Are Divisible by k",
            "1590. Make Sum Divisible by P",
            "2491. Divide Players Into Teams of Equal Skill",
            "567. Permutation in String",
            "1813. Sentence Similarity III",
            "1963. Minimum Number of Swaps to Make the String",
            "921. Minimum Add to Make Parentheses Valid",
            "962. Maximum Width Ramp",
            "1942. The Number of the Smallest Unoccupied Chair",
            "2406. Divide Intervals Into Minimum Number of Groups",
            "2530. Maximal Score After Applying K Operations",
            "2938. Separate Black and White Balls",
            "1405. Longest Happy String",
            "670. Maximum Swap",
            "2044. Count Number of Maximum Bitwise-OR Subsets",
            "1545. Find Kth Bit in Nth Binary String",
            "1593. Split a String Into the Max Number of Unique",
            "2583. Kth Largest Sum in a Binary Tree",
            "2641. Cousins in Binary Tree II",
            "951. Flip Equivalent Binary Trees",
            "1233. Remove Sub-Folders from the Filesystem",
            "1277. Count Square Submatrices with All Ones",
            "2501. Longest Square Streak in an Array",
            "2684. Maximum Number of Moves in a Grid"
        ],
        "Hard": [
            "502. IPO",
            "330. Patching Array",
            "995. Minimum Number of K Consecutive Bit Flips",
            "1579. Remove Max Number of Edges to Keep Graph Fully",
            "2751. Robot Collisions",
            "726. Number of Atoms",
            "2392. Build a Matrix With Conditions",
            "2045. Second Minimum Time to Reach Destination",
            "273. Integer to English Words",
            "1568. Minimum Number of Days to Disconnect Island",
            "664. Strange Printer",
            "564. Find the Closest Palindrome",
            "2699. Modify Graph Edge Weights",
            "214. Shortest Palindrome",
            "440. K-th Smallest in Lexicographical Order",
            "2416. Sum of Prefix Scores of Strings",
            "432. All O'one Data Structure",
            "632. Smallest Range Covering Elements from K Lists",
            "1106. Parsing A Boolean Expression",
            "2458. Height of Binary Tree After Subtree Removal Queries"
        ]
    }

    # Create the folder structure
    for difficulty, problems in structure.items():
        # Create difficulty folder
        difficulty_path = os.path.join(root_dir, difficulty)
        if not os.path.exists(difficulty_path):
            os.makedirs(difficulty_path)

        # Create problem folders and solution files
        for problem in problems:
            sanitized_problem = sanitize_folder_name(problem)
            problem_path = os.path.join(difficulty_path, sanitized_problem)
            if not os.path.exists(problem_path):
                os.makedirs(problem_path)

            # Create solution files
            r_solution = os.path.join(problem_path, "solution.R")
            python_solution = os.path.join(problem_path, "solution.py")

            # Create empty solution files if they don't exist
            if not os.path.exists(r_solution):
                with open(r_solution, 'w') as f:
                    f.write("# R solution for " + problem + "\n")

            if not os.path.exists(python_solution):
                with open(python_solution, 'w') as f:
                    f.write("# Python solution for " + problem + "\n")


if __name__ == "__main__":
    try:
        create_folder_structure()
        print("Folder structure created successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
