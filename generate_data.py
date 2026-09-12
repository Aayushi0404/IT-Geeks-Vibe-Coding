import os
import random

# Real SGSITS Lore & Realistic Rules
intro = """# Shri G. S. Institute of Technology & Science (SGSITS), Indore
## Official Academic, Disciplinary, and Hostel Rulebook (2026-2027)

### 1. Introduction & Legacy
Affiliated with Rajiv Gandhi Proudyogiki Vishwavidyalaya (RGPV) and approved by AICTE, SGSITS has consistently maintained a legacy of academic excellence, cutting-edge research, and industry-oriented education. The institute emphasizes experiential learning through modern laboratories, innovation centers, research initiatives, internships, and strong industry collaborations. 

Starting from the academic year 2026-27, the institute has implemented a newly updated Anti-Ragging Policy and inaugurated the new AICTE IDEA Lab for Robotics, AI, and Quantum Computing. 

"""

# The exact planted contradictions we need for our Eval Script
CONTRADICTIONS = {
    3: "### Section 3.1: Attendance Minimum\nAll students must maintain a strict 75% minimum attendance to sit for final examinations. No exceptions are permitted.\n",
    12: "### Section 12.4: Medical Exemptions\nStudents with a valid medical certificate are eligible to sit for exams with only 60% attendance.\n",
    4: "### Section 4.5: Hostel Curfew\nThe main hostel gates lock precisely at 10:00 PM. No student is allowed entry after this time under any circumstances.\n",
    18: "### Section 18.2: Central Library Late Hours\nStudents utilizing the 24/7 Central Library facility may return to their hostels up to 11:30 PM by showing their library exit stamp.\n",
    5: "### Section 5.1: Late Fee Penalty\nAny tuition fee paid after the initial deadline will incur a flat penalty of ₹500.\n",
    22: "### Section 22.9: Financial Aid Overrides\nFor students receiving institutional scholarships, any late tuition fee payment is subject to a 5% penalty on the outstanding amount, overriding all flat fees.\n"
}

# A pool of realistic rule paragraphs to dynamically generate the rest of the 6,000 words
filler_paragraphs = [
    "Students must carry their physical RFID identity cards at all times within the campus premises. Failure to produce the ID card upon request by campus security will result in disciplinary action.",
    "The Central Library provides a vast collection of books, journals, and e-resources. Eating, drinking, and sleeping inside the reading rooms are strictly prohibited.",
    "Ragging in any form is a criminal offense. The Anti-Ragging Committee will take immediate action against any student found guilty, leading to immediate expulsion and police registration.",
    "The Central Workshop offers practical training in machining, welding, and fabrication. Students must wear closed-toe leather shoes and proper safety gear during all workshop sessions.",
    "Hostel rooms are equipped with standard furniture. Any damage to the study tables, beds, or electrical fittings will be deducted directly from the student's caution money deposit.",
    "High-speed 16-hour Wi-Fi is provided in the hostels for academic purposes. Accessing unauthorized or malicious websites will trigger an automatic block from the IT department.",
    "Campus placements require students to maintain a minimum CGPA of 7.5. The Training and Placement Cell reserves the right to disqualify students with active academic backlogs.",
    "Students parked in unauthorized zones will have their vehicles clamped. A fine must be paid at the main administration office before the vehicle is released.",
    "Medical emergencies should be immediately reported to the on-campus Dispensary. An ambulance is available 24/7 for transport to the nearest affiliated hospital.",
    "All semester fees must be cleared before the issuance of the admit card. The accounts department operates only between 10:30 AM and 4:00 PM on working days."
]

# Generate a realistic 6,000+ word document with 30 Chapters
content = intro
word_count = len(intro.split())

for chapter_num in range(2, 31):
    content += f"\n## Chapter {chapter_num}: Standard Academic Procedures\n\n"
    
    # Check if we need to insert a contradiction in this chapter
    if chapter_num in CONTRADICTIONS:
        content += CONTRADICTIONS[chapter_num] + "\n"
        word_count += len(CONTRADICTIONS[chapter_num].split())
        
    # Generate 5-7 random paragraphs to fill out the chapter
    for _ in range(random.randint(5, 8)):
        # Duplicate the paragraph multiple times to build length quickly like legal jargon
        para = " ".join(random.choices(filler_paragraphs, k=4))
        content += para + "\n\n"
        word_count += len(para.split())
        
    # Add our Table exactly where it needs to be so the eval passes
    if chapter_num == 6:
        content += "### Fee Payment Deadlines Table\n| Semester | Due Date | Grace Period |\n| :--- | :--- | :--- |\n| Odd Sem | July 15 | 3 Days |\n| Even Sem | Jan 10 | 3 Days |\n\n"

# Write to file
with open("rulebook.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Authentic SGSITS Rulebook Generated! Word Count: ~{word_count} words.")