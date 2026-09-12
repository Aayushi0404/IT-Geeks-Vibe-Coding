import json
from app import analyze_rulebook

with open("rulebook.md", "r", encoding="utf-8") as f:
    rulebook = f.read()

TEST_QUESTIONS = [
    {"q": "What is the penalty for paying tuition late?", "expected": "CONTRADICTION"},
    {"q": "What is the attendance required if I have a medical issue?", "expected": "CONTRADICTION"},
    {"q": "What is the absolute latest time I can enter the hostel at night?", "expected": "CONTRADICTION"},
    {"q": "If I am a scholarship student, how much is my late fee?", "expected": "CONTRADICTION"},
    {"q": "Can a medical certificate lower my attendance requirement to 60%?", "expected": "CONTRADICTION"},
    {"q": "Is the hostel gate strictly locked at 10:00 PM for everyone?", "expected": "CONTRADICTION"},
    {"q": "I was studying in the Central Library till 11 PM, will I be allowed in the hostel?", "expected": "CONTRADICTION"},
    {"q": "What happens if I miss the exam because of a family wedding?", "expected": "NOT_COVERED"},
    {"q": "Is there a dress code for the final examinations?", "expected": "NOT_COVERED"},
    {"q": "How many days of leave do I get for a bereavement in the family?", "expected": "NOT_COVERED"},
    {"q": "Can I pay my tuition fees using a credit card?", "expected": "NOT_COVERED"},
    {"q": "What is the procedure to change my hostel room if my roommate is snoring?", "expected": "NOT_COVERED"},
    {"q": "Are pets allowed inside the hostel premises?", "expected": "NOT_COVERED"},
    {"q": "If I fail three subjects, do I have to repeat the entire year?", "expected": "NOT_COVERED"},
    {"q": "Who is the current head of the academic council?", "expected": "NOT_COVERED"},
    {"q": "What is the penalty if I am caught cheating in an internal test?", "expected": "NOT_COVERED"},
    {"q": "Can I bring my own personal cooler or AC to the hostel room?", "expected": "NOT_COVERED"},
    {"q": "Is there a grace period for Even Semester fees?", "expected": "ANSWERED"},
    {"q": "What is the exact due date for Odd Semester fee payment?", "expected": "ANSWERED"},
    {"q": "Who periodically reviews the university rules?", "expected": "ANSWERED"},
    {"q": "What is the grace period for odd semester fees?", "expected": "ANSWERED"},
    {"q": "What standards of conduct does the university expect?", "expected": "ANSWERED"},
    {"q": "What is the due date for Even sem?", "expected": "ANSWERED"},
    {"q": "How many days is the grace period for Even semester?", "expected": "ANSWERED"},
    {"q": "Does the university have an academic council?", "expected": "ANSWERED"}
]

def run_evals():
    score = 0
    print("Running Eval Suite...\n")
    for idx, test in enumerate(TEST_QUESTIONS):
        print(f"Q{idx+1}: {test['q']}")
        result = analyze_rulebook(test['q'], rulebook)
        actual = result.get('state')
        
        if actual == test['expected']:
            print(f"✅ PASS (Got {actual})")
            score += 1
        else:
            print(f"❌ FAIL (Expected {test['expected']}, Got {actual})")
        print("-" * 40)
        
    print(f"\n🏆 Final Accuracy: {score}/{len(TEST_QUESTIONS)}")

if __name__ == "__main__":
    run_evals()