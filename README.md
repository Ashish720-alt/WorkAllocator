This repository is designed to facilitate the distribution of grading tasks among course graders.

0. Run code
python3 main.py

1. Grader Configuration
Grader names and their associated workload weights are stored in graderConfigs.py.

2. Work Parameters
Ns: Total number of submissions.
qNames: Name of the questions could be 1,2,3, .. or A,B,C, .. or 0,1,2, ...
workWeights: A list of Nq elements where the ith element indicates how much work is required to grade the ith question typically the number of points
of that question

3. Optional Input from main.py
Sq (optional): Is a subset of [1..Nq]. Each question from the list of special question, SQ, is distributed to ALL graders in proportion to their assigned weights. For questions not in SQ, the system minimizes the number of distinct questions assigned to each grader, promoting task specialization.

4. Output
The system generates a dictionary mapping each grader's name to a list of question numbers and submission interval pairs assigned to them.

Example Output:
For the input Ns = 30, Nq = 3 , SQ = [1]; and grader configuration, graderNames = ["John", "Peter"] , graderWeights = [1 , 1]; the output will be:
{
    "John": [(1, (1, 15)), (2, (1, 30))]
    "Peter": [(1, (16, 30)), (3, (1, 30))]
}
This output indicates John is assigned Q1: Submission numbers 1–15 and Q2: Submission numbers 1–30; wheras Peter is assigned Q1: Submission numbers 16–30 and Q3: Submission numbers 1–30

