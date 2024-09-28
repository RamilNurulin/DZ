number_of_tasks: int = 12
number_of_hours: float = 1.5
course = "Python,"
time_per_job: float = number_of_hours / number_of_tasks

print("Курс:", course, "всего задач:", number_of_tasks, ', ' "затрачено часов:",
      number_of_hours, ' ,', "среднее время выполнения:", time_per_job, ", часа.")