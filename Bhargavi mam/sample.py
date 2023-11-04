def check_for_duplicates(preferences):
    for i, pref_list in enumerate(preferences):
        if len(pref_list) != len(set(pref_list)):
            print(f"Error: Duplicate numbers found in preferences for {'Task Givers' if i == 0 else 'Task Executors'}")
            return True
    return False

def find_stable_assignments(task_giver_preferences, task_executor_preferences):
    if check_for_duplicates(task_giver_preferences) or check_for_duplicates(task_executor_preferences):
        return

    n = len(task_giver_preferences)
    task_executors = [-1] * n
    task_givers_engaged = [False] * n
    free_count = n

    while free_count > 0:
        tg = 0
        while tg < n:
            if not task_givers_engaged[tg]:
                break
            tg += 1

        i = 0
        while i < n and not task_givers_engaged[tg]:
            te = task_giver_preferences[tg][i]
            if task_executors[te] == -1:
                task_executors[te] = tg
                task_givers_engaged[tg] = True
                free_count -= 1
            else:
                current_assignment = task_executors[te]
                if task_executor_preferences[te].index(tg) < task_executor_preferences[te].index(current_assignment):
                    task_executors[te] = tg
                    task_givers_engaged[tg] = True
                    task_givers_engaged[current_assignment] = False
            i += 1

    print("Task Giver\tTask Executor")
    for i in range(n):
        print(f"{i + 1}\t\t{task_executors[i] + 1}")

# Manually specify preferences for task givers and task executors
task_giver_preferences = [
    [2, 1, 0, 3],  # Task giver 1 preferences
    [0, 1, 2, 3],  # Task giver 2 preferences
    [0, 3, 2, 1],  # Task giver 3 preferences
    [0, 1, 2, 3],  # Task giver 4 preferences
]

task_executor_preferences = [
    [3, 1, 0, 2],  # Task executor 1 preferences
    [1, 3, 0, 2],  # Task executor 2 preferences
    [3, 2, 1, 0],  # Task executor 3 preferences
    [2, 0, 1, 3],  # Task executor 4 preferences
]

find_stable_assignments(task_giver_preferences, task_executor_preferences)
