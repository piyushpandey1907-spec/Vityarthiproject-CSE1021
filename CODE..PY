import datetime

def compute_priority(task):
    today = datetime.date.today()
    days_left = (task["deadline"] - today).days
    urgency = max(0, 1 - (days_left / 30))

    importance = task["importance"] / 5
    effort_score = 1 - (task["effort"] / 480)  # max 8 hours
    dep_score = task["dependencies"] / 5

    score = (0.4 * urgency +
             0.3 * importance +
             0.15 * effort_score +
             0.1 * dep_score)

    return score


def prioritize_tasks(task_list):
    for task in task_list:
        task["score"] = compute_priority(task)

    return sorted(task_list, key=lambda x: x["score"], reverse=True)
