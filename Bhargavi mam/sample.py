def find_stable_assignments(preferences):
    n = len(preferences) // 2  # Assuming equal numbers of task givers and task executors

    # Check for duplicate numbers in task giver preferences
    for tg in preferences[:n]:
        if len(tg) != len(set(tg)):
            print("Error: Duplicate numbers found in task giver preferences.")
            return

    # Check for duplicate numbers in task executor preferences
    for te in preferences[n:]:
        if len(te) != len(set(te)):
            print("Error: Duplicate numbers found in task executor preferences.")
            return

    # Initialize data structures to track assignments
    task_givers = [-1] * n  # To store the assignment for task givers
    task_executors = [-1] * n  # To store the assignment for task executors

    free_count = n  # Count of unassigned task givers

    while free_count > 0:
        tg = 0
        while tg < n:
            if task_givers[tg] == -1:
                break
            tg += 1

        if tg == n:
            break  # All task givers are assigned, exit the loop

        # Iterate through task givers' preferences
        for i in range(n):
            te = preferences[tg][i]

            if task_executors[te] == -1:  # task executor is unassigned
                task_givers[tg] = te
                task_executors[te] = tg
                free_count -= 1
                break

    # Print the stable assignments
    print("Task Giver\tTask Executor")
    for i in range(n):
        print(f"{i + 1}\t\t{task_givers[i] + 1}")

# Manually specify preferences for task givers and task executors
preferences = [
    [2, 2, 0, 3],  # Task giver 1 preferences
    [1, 0, 3, 2],  # Task giver 2 preferences
    [0, 3, 2, 1],  # Task giver 3 preferences
    [2, 0, 1, 3],  # Task giver 4 preferences
    [2, 1, 0, 3],  # Task executor 1 preferences
    [1, 0, 3, 2],  # Task executor 2 preferences
    [0, 3, 2, 1],  # Task executor 3 preferences
    [2, 0, 1, 3],  # Task executor 4 preferences
]

find_stable_assignments(preferences)
