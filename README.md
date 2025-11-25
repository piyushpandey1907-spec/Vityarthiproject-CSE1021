#  Automatic Task Prioritizer

A simple console-based system that helps users *organize and prioritize tasks* based on urgency and importance.  
It reduces manual decision-making by automatically ranking tasks, allowing users to manage time more effectively.

---

##  Features

- Add tasks with:
  - task name
  - due date
  - priority level (High/Medium/Low)
  - estimated time
- Automatic priority scoring
- View tasks sorted from highest to lowest priority
- Mark tasks as completed
- Save and load tasks (optional extension)

---

##  System Modules

### 1. *Task Input Module*
- Accepts task details from the user  
- Validates inputs  
- Stores data in a list or file

### 2. *Processing & Prioritization Module*
- Calculates task score using factors like:
  - priority level
  - due date closeness
- Sorts tasks automatically

### 3. *Reporting / Output Module*
- Displays:
  - pending tasks in priority order
  - completed tasks (optional)
- Allows task status update

---

##  Workflow

1. User enters task details  
2. System calculates priority score  
3. Tasks are stored and sorted  
4. User views the recommended order  
5. User can update or complete tasks

---

## Technologies Used

- *Language:* Python (or any chosen language)
- *Concepts:*
  - Input/output operations
  - Conditional statements
  - Loops
  - Lists/arrays
  - Basic file handling (optional)

---

## Installation & Run

```bash
# Clone or download the project
cd automatic-task-prioritizer

# Run the program
python main.py
