import random
import pandas as pd
from tqdm import tqdm

answers = [
    "An operating system is what lets you interact with the hardware on your computer.",
    "I think a process is like a program that's running on your computer.",
    "Virtual memory is something the computer uses when it runs out of RAM.",
    "I am not too sure, but I think threads are part of processes.",
    "Deadlocks happen when two programs are stuck waiting for each other.",
    "The kernel is the core part of the OS that manages everything.",
    "Multitasking allows the OS to run multiple programs at once.",
    "I think paging is a way to manage memory in the OS.",
    "The boot process is what happens when you turn on your computer.",
    "Inter-process communication is how processes talk to each other."
]

# Follow-up questions that a staff might ask based on the student's answers
follow_up_questions = [
    "Could you explain how the operating system interacts with the hardware?",
    "Can you give an example of a process you use daily?",
    "What are the advantages of using virtual memory?",
    "How do threads differ from processes?",
    "Can you think of a situation where a deadlock might occur?",
    "What specific tasks does the kernel handle?",
    "How does the OS switch between different programs?",
    "How does paging improve memory management?",
    "What are the main steps involved in the boot process?",
    "Why is inter-process communication important in an OS?"
]


def generate_follow_up(answer):
    index = answers.index(answer)
    return follow_up_questions[index]

dataset = []
for i in tqdm(range(1000), desc="Generating Follow-Up Dataset"):
    answer = random.choice(answers)
    follow_up = generate_follow_up(answer)
    dataset.append((answer, follow_up))

df = pd.DataFrame(dataset, columns=["Answer (Student)", "Follow-up Question (Staff)"])

df.to_csv("os_follow_up_dataset.csv",mode='a',header=False, index=False)

print("Dataset generated and saved as 'os_follow_up_conversation_dataset.csv'")
